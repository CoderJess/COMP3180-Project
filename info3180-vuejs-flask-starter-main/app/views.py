"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from flask import current_app as app, render_template, request, jsonify, send_file, send_from_directory
from app.models import User, Profile, Favourite
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import os
from functools import wraps
from datetime import datetime

# --- Token Authentication ---
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('x-access-token')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = User.query.filter_by(id=data['user_id']).first()
        except:
            return jsonify({'message': 'Token is invalid!'}), 401
        return f(current_user, *args, **kwargs)
    return decorated

# --- Helper Functions ---
def has_complete_profile(user_id):
    profiles = Profile.query.filter_by(user_id=user_id).all()
    for profile in profiles:
        if all([
            profile.description, profile.parish, profile.biography, profile.sex,
            profile.race, profile.birth_year, profile.height, profile.fav_cuisine,
            profile.fav_colour, profile.fav_school_subject,
            profile.political is not None, profile.religious is not None,
            profile.family_oriented is not None
        ]):
            return True
    return False

# --- Main Routes ---

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/api/register', methods=['POST'])
def register():
    from app import db
    data = request.get_json()
    if not all(k in data for k in ('username', 'password', 'name', 'email')):
        return jsonify({'message': 'Missing required fields'}), 400
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'message': 'Username already exists'}), 400
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'message': 'Email already exists'}), 400

    hashed_password = generate_password_hash(data['password'])
    new_user = User(
        username=data['username'],
        password=hashed_password,
        name=data['name'],
        email=data['email'],
        photo=data.get('photo', '')
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/api/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'message': 'Could not verify'}), 401

    user = User.query.filter_by(username=data['username']).first()
    if not user:
        return jsonify({'message': 'User not found'}), 404

    if check_password_hash(user.password, data['password']):
        token = jwt.encode({'user_id': user.id}, app.config['SECRET_KEY'], algorithm="HS256")
        return jsonify({'token': token})

    return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/api/auth/logout', methods=['POST'])
@token_required
def logout(current_user):
    return jsonify({'message': 'Logged out successfully'})

@app.route('/api/profiles', methods=['GET'])
@token_required
def get_profiles(current_user):
    if not has_complete_profile(current_user.id):
        return jsonify({'message': 'You need to complete a profile first'}), 403
    profiles = Profile.query.all()
    result = []
    for profile in profiles:
        if profile.user_id != current_user.id:
            result.append({
                'id': profile.id,
                'user_id': profile.user_id,
                'description': profile.description,
                'parish': profile.parish,
                'sex': profile.sex,
                'race': profile.race,
                'birth_year': profile.birth_year
            })
    return jsonify(result)

@app.route('/api/profiles', methods=['POST'])
@token_required
def create_profile(current_user):
    from app import db
    data = request.get_json()

    if Profile.query.filter_by(user_id=current_user.id).count() >= 3:
        return jsonify({'message': 'Maximum of 3 profiles allowed'}), 400

    required_fields = [
        'description', 'parish', 'biography', 'sex', 'race', 'birth_year',
        'height', 'fav_cuisine', 'fav_colour', 'fav_school_subject',
        'political', 'religious', 'family_oriented'
    ]
    for field in required_fields:
        if field not in data:
            return jsonify({'message': f'Missing field: {field}'}), 400

    profile = Profile(user_id=current_user.id, **data)
    db.session.add(profile)
    db.session.commit()

    return jsonify({'message': 'Profile created successfully', 'profile_id': profile.id}), 201

@app.route('/api/profiles/<int:profile_id>', methods=['GET'])
@token_required
def get_profile(current_user, profile_id):
    if not has_complete_profile(current_user.id):
        return jsonify({'message': 'You need to complete a profile first'}), 403

    profile = Profile.query.get_or_404(profile_id)
    user = User.query.get(profile.user_id)
    age = datetime.now().year - profile.birth_year

    return jsonify({
        'id': profile.id,
        'user_id': profile.user_id,
        'name': user.name,
        'description': profile.description,
        'parish': profile.parish,
        'biography': profile.biography,
        'sex': profile.sex,
        'race': profile.race,
        'birth_year': profile.birth_year,
        'age': age,
        'height': profile.height,
        'fav_cuisine': profile.fav_cuisine,
        'fav_colour': profile.fav_colour,
        'fav_school_subject': profile.fav_school_subject,
        'political': profile.political,
        'religious': profile.religious,
        'family_oriented': profile.family_oriented
    })

@app.route('/api/profiles/<int:user_id>/favorite', methods=['POST'])
@token_required
def add_favorite(current_user, user_id):
    from app import db
    if current_user.id == user_id:
        return jsonify({'message': 'You cannot favorite yourself'}), 400
    if Favourite.query.filter_by(user_id=current_user.id, fav_user_id=user_id).first():
        return jsonify({'message': 'Already favorited'}), 400

    fav = Favourite(user_id=current_user.id, fav_user_id=user_id)
    db.session.add(fav)
    db.session.commit()
    return jsonify({'message': 'Added to favorites successfully'}), 201

@app.route('/api/search', methods=['GET'])
@token_required
def search_profiles(current_user):
    if not has_complete_profile(current_user.id):
        return jsonify({'message': 'You need to complete a profile first'}), 403

    name = request.args.get('name', '')
    birth_year = request.args.get('birth_year', type=int)
    sex = request.args.get('sex', '')
    race = request.args.get('race', '')

    query = Profile.query.join(User).filter(Profile.user_id != current_user.id)
    if name:
        query = query.filter(User.name.ilike(f'%{name}%'))
    if birth_year:
        query = query.filter(Profile.birth_year == birth_year)
    if sex:
        query = query.filter(Profile.sex == sex)
    if race:
        query = query.filter(Profile.race == race)

    profiles = query.all()
    result = []
    for profile in profiles:
        user = User.query.get(profile.user_id)
        result.append({
            'id': profile.id,
            'user_id': profile.user_id,
            'name': user.name,
            'description': profile.description,
            'parish': profile.parish,
            'sex': profile.sex,
            'race': profile.race,
            'birth_year': profile.birth_year,
            'age': datetime.now().year - profile.birth_year
        })
    return jsonify(result)

# --- Utility Routes ---

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    return app.send_static_file(file_name + '.txt')

@app.after_request
def add_header(response):
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

@app.errorhandler(404)
def page_not_found(error):
    return "Page not found", 404
