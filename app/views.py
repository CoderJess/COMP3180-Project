"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from app import app, db
from app.models import User, Profile, Favourite
from flask import Flask, render_template, request, jsonify, send_file
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import os
from functools import wraps
from datetime import datetime

# Token Authentication
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = User.query.filter_by(id=data['user_id']).first()
        except:
            return jsonify({'message': 'Token is invalid!'}), 401
        
        return f(current_user, *args, **kwargs)
    
    return decorated

def has_complete_profile(user_id):
    profiles = Profile.query.filter_by(user_id=user_id).all()
    if not profiles:
        return False
    
    # Check if at least one profile is complete
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

###
# Routing for your application.
###

@app.route('/')
def index():
    return jsonify(message="This is the beginning of our API")

@app.route('/api/register', methods=['POST'])
def register():
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

@app.route('/api/auth/login', methods=['POST'])
def login():
    data = request.get_json()

    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'message': 'Could not verify'}), 401
    
    user = User.query.filter_by(username=data['username']).first()

    if not user:
        return jsonify({'message': 'User not found'}), 404
    
    if check_password_hash(user.password, data['password']):
        token = jwt.encode(
            {'user_id': user.id},
            app.config['SECRET_KEY'],
            algorithm="HS256"
        )

        return jsonify({'token': token})
    return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/api/auth/logout', methods=['POST'])
@token_required
def logout(current_user):
     # To be  completed to include blacklisted tokens
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
            profile_data = {
                'id': profile.id,
                'user_id': profile.user_id,
                'description': profile.description,
                'parish': profile.parish,
                'sex': profile.sex,
                'race': profile.race,
                'birth_year': profile.birth_year
            }
            result.append(profile_data)
    return jsonify(result)

@app.route('/api/profiles', methods=['POST'])
@token_required
def create_profile(current_user):
    data = request.get_json()

    existing_profiles = Profile.query.filter_by(user_id=current_user.id).count()
    if existing_profiles >= 3:
        return jsonify({'message': 'Maximum of 3 profiles allowed per user'}), 400
    
    required_fields = [
        'description', 'parish', 'biography', 'sex', 'race', 'birth_year',
        'height', 'fav_cuisine', 'fav_colour', 'fav_school_subject',
        'political', 'religious', 'family_oriented'
    ]

    for field in required_fields:
        if field not in data:
            return jsonify({'message': f'Missing required field: {field}'}), 400
        
    new_profile = Profile(
        user_id=current_user.id,
        description=data['description'],
        parish=data['parish'],
        biography=data['biography'],
        sex=data['sex'],
        race=data['race'],
        birth_year=data['birth_year'],
        height=data['height'],
        fav_cuisine=data['fav_cuisine'],
        fav_colour=data['fav_colour'],
        fav_school_subject=data['fav_school_subject'],
        political=data['political'],
        religious=data['religious'],
        family_oriented=data['family_oriented']
    )

    db.session.add(new_profile)
    db.session.commit()
    
    return jsonify({'message': 'Profile created successfully!', 'profile_id': new_profile.id}), 201

app.route('/api/profiles/<int:profile_id>', methods=['GET'])
@token_required
def get_profile(current_user, profile_id):
    if not has_complete_profile(current_user.id):
        return jsonify({'message': 'You need to complete a profile first'}), 403
    
    profile = Profile.query.get_or_404(profile_id)
    user = User.query.get(profile.user_id)

    current_year = datetime.now().year
    age = current_year - profile.birth_year

    profile_data = {
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
    }

    return jsonify(profile_data)

@app.route('/api/profiles/<int:user_id>/favorite', methods=['POST'])
@token_required
def add_favorite(current_user, user_id):
    if not has_complete_profile(current_user.id):
        return jsonify({'message': 'You need to complete a profile first'}), 403
     
    if current_user.id == user_id:
        return jsonify({'message': 'You cannot favorite yourself'}), 400

    user = User.query.get_or_404(user_id)

    existing_favorite = Favourite.query.filter_by(
        user_id=current_user.id, 
        fav_user_id=user_id
    ).first()
    
    if existing_favorite:
        return jsonify({'message': 'Already in favorites'}), 400
    
    new_favorite = Favourite(
        user_id=current_user.id,
        fav_user_id=user_id
    )

    db.session.add(new_favorite)
    db.session.commit()
    
    return jsonify({'message': 'Added to favorites successfully'}), 201

@app.route('/api/profiles/matches/<int:profile_id>', methods=['GET'])
@token_required
def get_matches(current_user, profile_id):
    if not has_complete_profile(current_user.id):
        return jsonify({'message': 'You need to complete a profile first'}), 403
    
    # Ensure the profile belongs to the current user
    profile = Profile.query.get_or_404(profile_id)
    if profile.user_id != current_user.id:
        return jsonify({'message': 'You can only get matches for your own profiles'}), 403
    
    # Find all profiles and calculate match percentage
    all_profiles = Profile.query.filter(Profile.user_id != current_user.id).all()
    matches = []
    
    for other_profile in all_profiles:
        match_score = 0
        total_fields = 0
        
        # Parish match
        if profile.parish == other_profile.parish:
            match_score += 1
        total_fields += 1
        
        # Favorite cuisine match
        if profile.fav_cuisine == other_profile.fav_cuisine:
            match_score += 1
        total_fields += 1
        
        # Favorite color match
        if profile.fav_colour == other_profile.fav_colour:
            match_score += 1
        total_fields += 1
        
        # Favorite school subject match
        if profile.fav_school_subject == other_profile.fav_school_subject:
            match_score += 1
        total_fields += 1
        
        # Political views match
        if profile.political == other_profile.political:
            match_score += 1
        total_fields += 1
        
        # Religious views match
        if profile.religious == other_profile.religious:
            match_score += 1
        total_fields += 1
        
        # Family oriented match
        if profile.family_oriented == other_profile.family_oriented:
            match_score += 1
        total_fields += 1
        
        # Calculate percentage
        match_percentage = (match_score / total_fields) * 100
        
        # Add to matches if above 50%
        if match_percentage >= 50:
            user = User.query.get(other_profile.user_id)
            matches.append({
                'profile_id': other_profile.id,
                'user_id': other_profile.user_id,
                'name': user.name,
                'match_percentage': match_percentage,
                'parish': other_profile.parish,
                'birth_year': other_profile.birth_year,
                'age': datetime.now().year - other_profile.birth_year
            })
    
    # Sort by match percentage (highest first)
    matches.sort(key=lambda x: x['match_percentage'], reverse=True)
    
    return jsonify(matches)

@app.route('/api/search', methods=['GET'])
@token_required
def search_profiles(current_user):
    if not has_complete_profile(current_user.id):
        return jsonify({'message': 'You need to complete a profile first'}), 403
    
    name = request.args.get('name', '')
    birth_year = request.args.get('birth_year', type=int)
    sex = request.args.get('sex', '')
    race = request.args.get('race', '')

    query = db.session.query(Profile).join(User)

    # Filter by name
    if name:
        query = query.filter(User.name.ilike(f'%{name}%'))
    
    # Filter by birth year
    if birth_year:
        query = query.filter(Profile.birth_year == birth_year)
    
    # Filter by sex
    if sex:
        query = query.filter(Profile.sex == sex)
    
    # Filter by race
    if race:
        query = query.filter(Profile.race == race)
    
    # Exclude current user
    query = query.filter(Profile.user_id != current_user.id)
    
    profiles = query.all()

    result = []
    for profile in profiles:
        user = User.query.get(profile.user_id)
        profile_data = {
            'id': profile.id,
            'user_id': profile.user_id,
            'name': user.name,
            'description': profile.description,
            'parish': profile.parish,
            'sex': profile.sex,
            'race': profile.race,
            'birth_year': profile.birth_year,
            'age': datetime.now().year - profile.birth_year
        }
        result.append(profile_data)
    
    return jsonify(result)

@app.route('/api/users/<int:user_id>', methods=['GET'])
@token_required
def grt_user(current_user, user_id):
    if not has_complete_profile(current_user.id):
        return jsonify({'message': 'You need to complete a profile first'}), 403
    
    user = User.query.get_or_404(user_id)

    user_data = {
        'id': user.id,
        'username': user.username,
        'name': user.name,
        'email': user.email,
        'photo': user.photo,
        'date_joined': user.date_joined.strftime('%Y-%m-%d %H:%M:%S')
    }

    return jsonify(user_data)

@app.route('/api/users/user_id/favourites', methods=['GET'])
@token_required
def get_user_favourites(current_user, user_id):
    if current_user.id != user_id:
        return jsonify({'message': 'You can only view your own favorites'}), 403
    
    if not has_complete_profile(current_user.id):
        return jsonify({'message': 'You need to complete a profile first'}), 403
    
    sort_by = request.args.get('sort_by', 'name')

    favorites = Favourite.query.filter_by(user_id=user_id).all()

    result = []
    for favorite in favorites:
        fav_user = User.query.get(favorite.fav_user_id)

        profile = Profile.query.filter_by(user_id=favorite.fav_user_id).first()

        if profile and fav_user:
            fav_data = {
                'user_id': fav_user.id,
                'name': fav_user.name,
                'parish': profile.parish if profile else '',
                'age': datetime.now().year - profile.birth_year if profile else 0,
                'date_added': favorite.date_added.strftime('%Y-%m-%d %H:%M:%S')
            }
            result.append(fav_data)

    if sort_by == 'name':
        result.sort(key=lambda x: x['name'])
    elif sort_by == 'parish':
        result.sort(key=lambda x: x['parish'])
    elif sort_by == 'age':
        result.sort(key=lambda x: x['age'])
    
    return jsonify(result)

@app.route('/api/users/<int:user_id>/<int:n>', methods=['GET'])
@token_required
def get_top_favourites(current_user, n):
    if not has_complete_profile(current_user.id):
        return jsonify({'message': 'You need to complete a profile first'}), 403
    
    sort_by = request.args.get('sort_by', 'count')

    fav_counts = db.session.query(
        Favourite.fav_user_id, 
        db.func.count(Favourite.fav_user_id).label('count')
    ).group_by(Favourite.fav_user_id).order_by(db.desc('count')).limit(n).all()

    result = []
    for fav_user_id, count in fav_counts:
        user = User.query.get(fav_user_id)
        
        profile = Profile.query.filter_by(user_id=fav_user_id).first()

        if user and profile:
            fav_data = {
                'user_id': user.id,
                'name': user.name,
                'parish': profile.parish,
                'age': datetime.now().year - profile.birth_year,
                'favorite_count': count
            }
            result.append(fav_data)

    if sort_by == 'name':
        result.sort(key=lambda x: x['name'])
    elif sort_by == 'parish':
        result.sort(key=lambda x: x['parish'])
    elif sort_by == 'age':
        result.sort(key=lambda x: x['age'])
    # Default is already sorted by count
    
    return jsonify(result)
    

###
# The functions below should be applicable to all Flask apps.
###

# Here we define a function to collect form errors from Flask-WTF
# which we can later use
def form_errors(form):
    error_messages = []
    """Collects form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            message = u"Error in the %s field - %s" % (
                    getattr(form, field).label.text,
                    error
                )
            error_messages.append(message)

    return error_messages

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404