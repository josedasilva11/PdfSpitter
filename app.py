import os
import secrets
from os.path import abspath

import flask_login
from typing import Dict
from flask import Flask
from flask_login import login_user, login_required, current_user
from flask_sqlalchemy import SQLAlchemy
from sharp import Sharp, naming
from sqlalchemy_serializer import SerializerMixin

from pdf_printer import print_pdf, print_three_pdf
from user_session import UserSession

app = Flask('applicant', static_url_path='',
            static_folder='static',
            template_folder='templates')
app.config.update(SECRET_KEY=secrets.token_hex() )
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///applicants.db'
with open('database.txt') as db:
    app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql+psycopg2://'  + db.read().strip()
app.config['SQLALCHEMY_POOL_SIZE'] = 2
login_manager = flask_login.LoginManager()
login_manager.init_app(app)
db = SQLAlchemy(app)


api_generator = Sharp(app, prefix="/api", naming=naming.file_based)
from car_applicant import new_applicant, update_applicant, search_applicant


class User(db.Model, SerializerMixin):
    serialize_rules = ()
    serialize_only = ()
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50))
    password = db.Column(db.String(100))


db.create_all()


with db.session.begin():
    User.query.filter_by().delete()
    db.session.add(User(user_name='manager', password='57b1a089d6a882eec1a9f4a5a'))
    db.session.add(User(user_name='employee', password='71ff37448c6f8da9f79e4305f56bb'))


@login_manager.user_loader
def load_user(user_id):
    with db.session.begin():
        user = User.query.filter_by(id=user_id).first()
        if user is None:
            return None
        user_session = UserSession(id=user.id, user_name=user.user_name)
    return user_session


def find_user_by_username(user_name, password):
    with db.session.begin():
        user = User.query.filter_by(user_name=user_name, password=password).first()
        if user is None:
            return None
        user_session = UserSession(id=user.id, user_name=user.user_name)
    return user_session


@api_generator.function()
def login(username: str, password: str):
    user_session = find_user_by_username(user_name=username, password=password)
    if user_session is None:
        return {'success': False, 'error_message': 'Invalid password or login'}
    login_user(user_session)
    return {'success': True}


@login_manager.unauthorized_handler
def unauthorized():
    return {'success': False, 'error_message': 'You are not Logged In'}


@api_generator.function()
def is_login():
    if current_user.is_authenticated:
        return {'success': True}
    return {'success': False}


@api_generator.function()
def new_form(form_data: Dict[str, any]):  # put application's code here
    if not current_user.is_authenticated:
        return unauthorized()
    id = new_applicant()
    update_form(id, form_data)
    return {"success": True, 'id': id}


@app.route('/generate_pdf/<id>')
def generate_pdf(id: int):  # put application's code here
    if not current_user.is_authenticated:
        return unauthorized()
    found = search_applicant({'id': id})
    if len(found) == 0:
        return "No such file"
    data = found[0]
    return print_pdf(data)


@app.route('/generate3_pdf/<id>')
def generate_pdf3(id: int):
    if not current_user.is_authenticated:
        return unauthorized()
    found = search_applicant({'id': id})
    if len(found) == 0:
        return "No such file"
    data = found[0]
    return print_three_pdf(data)


@api_generator.function()
def search_form(filter: Dict[str, any]):
    if not current_user.is_authenticated:
        return unauthorized()
    search = {}
    for a in filter:
        if isinstance(filter[a], str) and len(filter[a].strip()) == 0:
            continue
        if a == 'id':
            search['id'] = int(filter[a])
        else:
            search[a] = filter[a]
    found = search_applicant(search)
    return {"success": True, 'items': found}


@api_generator.function()
def update_form(id: int, form_data: Dict[str, any]):
    if not current_user.is_authenticated:
        return unauthorized()
    update_applicant(id, form_data)
    return {"success": True}


@app.errorhandler(404)
def not_found(e):
    if os.path.exists('./static/index.html'):
        return app.send_static_file("index.html")
    else:
        return "The app didn't install error"


# _s = abspath("./front_end/src/api/")
# output_js_filename = f'{_s}{os.sep}api.js'
# api_generator.generate(output_js_filename)
if __name__ == '__main__':
    app.run()
