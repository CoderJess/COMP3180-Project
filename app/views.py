from flask import Flask, request, jsonify, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Allow frontend access

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jamdate.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'super-secret-key'
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)


# ---------- AUTH ----------
@app.route('/api/register', methods=['POST'])
def register():
    data = request.json
    user = User(username=data['username'], password=data['password'], name=data['name'], email=data['email'])
    db.session.add(user)
    db.session.commit()
    return jsonify(message="User registered successfully"), 201


@app.route('/api/auth/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data['username'], password=data['password']).first()
    if user:
        token = create_access_token(identity=user.id, expires_delta=timedelta(days=1))
        return jsonify(token=token, user_id=user.id)
    return jsonify(message="Invalid credentials"), 401


@app.route('/api/auth/logout', methods=['POST'])
@jwt_required()
def logout():
    return jsonify(message="Logged out")


# ---------- PROFILES ----------
@app.route('/api/profiles', methods=['GET'])
@jwt_required()
def get_profiles():
    profiles = Profile.query.order_by(Profile.id.desc()).limit(4).all()
    result = []
    for p in profiles:
        result.append({
            'id': p.id,
            'user_id_fk': p.user_id_fk,
            'birth_year': p.birth_year,
            'sex': p.sex,
            'race': p.race,
            'description': p.description,
            'parish': p.parish,
            'biography': p.biography,
            'height': p.height,
            'fav_cuisine': p.fav_cuisine,
            'fav_colour': p.fav_colour,
            'fav_school_subject': p.fav_school_subject,
            'political': p.political,
            'religious': p.religious,
            'family_oriented': p.family_oriented,
            'name': User.query.get(p.user_id_fk).name
        })
    return jsonify(result)


@app.route('/api/profiles', methods=['POST'])
@jwt_required()
def add_profile():
    data = request.json
    current_user = get_jwt_identity()
    if Profile.query.filter_by(user_id_fk=current_user).count() >= 3:
        return jsonify(message="Profile limit reached"), 400
    profile = Profile(user_id_fk=current_user, **data)
    db.session.add(profile)
    db.session.commit()
    return jsonify(message="Profile added successfully")


@app.route('/api/profiles/<int:profile_id>', methods=['GET'])
@jwt_required()
def get_profile(profile_id):
    p = Profile.query.get(profile_id)
    return jsonify({
        'id': p.id,
        'user_id_fk': p.user_id_fk,
        'birth_year': p.birth_year,
        'sex': p.sex,
        'race': p.race,
        'description': p.description,
        'parish': p.parish,
        'biography': p.biography,
        'height': p.height,
        'fav_cuisine': p.fav_cuisine,
        'fav_colour': p.fav_colour,
        'fav_school_subject': p.fav_school_subject,
        'political': p.political,
        'religious': p.religious,
        'family_oriented': p.family_oriented,
        'name': User.query.get(p.user_id_fk).name
    })


@app.route('/api/profiles/<int:user_id>/favourite', methods=['POST'])
@jwt_required()
def favourite_user(user_id):
    current_user = get_jwt_identity()
    fav = Favourite(user_id_fk=current_user, fav_user_id_fk=user_id)
    db.session.add(fav)
    db.session.commit()
    return jsonify(message="User favourited")


# ---------- FAVOURITES ----------
@app.route('/api/users/<int:user_id>/favourites', methods=['GET'])
@jwt_required()
def get_user_favourites(user_id):
    favs = Favourite.query.filter_by(user_id_fk=user_id).all()
    return jsonify([f.fav_user_id_fk for f in favs])


@app.route('/api/users/favourites/<int:N>', methods=['GET'])
@jwt_required()
def get_top_favourites(N):
    favs = db.session.query(Favourite.fav_user_id_fk, db.func.count(Favourite.id).label('total')).group_by(Favourite.fav_user_id_fk).order_by(db.desc('total')).limit(N).all()
    return jsonify([{"user_id": f[0], "total": f[1]} for f in favs])


# ---------- SEARCH ----------
@app.route('/api/search', methods=['GET'])
@jwt_required()
def search():
    query = Profile.query

    # Search User name
    name = request.args.get('name')
    if name:
        users = User.query.filter(User.name.ilike(f"%{name}%")).all()
        user_ids = [u.id for u in users]
        query = query.filter(Profile.user_id_fk.in_(user_ids))

    for field in ['birth_year', 'sex', 'race']:
        value = request.args.get(field)
        if value:
            query = query.filter(getattr(Profile, field) == value)

    result = []
    for p in query.all():
        result.append({
            'id': p.id,
            'user_id_fk': p.user_id_fk,
            'birth_year': p.birth_year,
            'sex': p.sex,
            'race': p.race,
            'description': p.description,
            'parish': p.parish,
            'biography': p.biography,
            'height': p.height,
            'fav_cuisine': p.fav_cuisine,
            'fav_colour': p.fav_colour,
            'fav_school_subject': p.fav_school_subject,
            'political': p.political,
            'religious': p.religious,
            'family_oriented': p.family_oriented,
            'name': User.query.get(p.user_id_fk).name
        })

    return jsonify(result)


# ---------- MATCHING ----------
@app.route('/api/profiles/matches/<int:profile_id>', methods=['GET'])
@jwt_required()
def match(profile_id):
    main_profile = Profile.query.get(profile_id)
    profiles = Profile.query.filter(Profile.user_id_fk != main_profile.user_id_fk).all()
    matches = []
    for p in profiles:
        age_diff = abs((datetime.now().year - p.birth_year) - (datetime.now().year - main_profile.birth_year))
        height_diff = abs(p.height - main_profile.height)
        common = sum([
            p.fav_cuisine == main_profile.fav_cuisine,
            p.fav_colour == main_profile.fav_colour,
            p.fav_school_subject == main_profile.fav_school_subject,
            p.political == main_profile.political,
            p.religious == main_profile.religious,
            p.family_oriented == main_profile.family_oriented,
        ])
        if age_diff <= 5 and 3 <= height_diff <= 10 and common >= 3:
            matches.append({
                'id': p.id,
                'name': User.query.get(p.user_id_fk).name,
                'birth_year': p.birth_year,
                'sex': p.sex,
                'race': p.race
            })
    return jsonify(matches)


# ---------- FILE UPLOAD ----------
@app.route('/uploads/<filename>')
def uploads(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


# ---------- RUN ----------
if __name__ == '__main__':
    app.run(debug=True)
