import os
from os.path import abspath
from typing import Dict

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sharp import Sharp, naming

from pdf_printer import print_pdf, print_three_pdf

app = Flask('applicant', static_url_path='',
            static_folder='static',
            template_folder='templates')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///applicants.db'
with open('database.txt') as database_file:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://' + database_file.read().strip()

db = SQLAlchemy(app)
api_generator = Sharp(app, prefix="/api", naming=naming.file_based)

from car_applicant import new_applicant, update_applicant, search_applicant

db.create_all()


@api_generator.function()
def new_form(form_data: Dict[str, any]):  # put application's code here

    id = new_applicant()
    update_form(id, form_data)
    return {"success": True, 'id': id}


@app.route('/generate_pdf/<id>')
def generate_pdf(id: int):  # put application's code here
    found = search_applicant({'id': id})
    if len(found) == 0:
        return "No such file"
    data = found[0]
    return print_pdf(data)


@app.route('/generate3_pdf/<id>')
def generate_pdf3(id: int):  # put application's code here
    found = search_applicant({'id': id})
    if len(found) == 0:
        return "No such file"
    data = found[0]
    return print_three_pdf(data)


@api_generator.function()
def search_form(filter: Dict[str, any]):  # put application's code here
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
def update_form(id: int, form_data: Dict[str, any]):  # put application's code here
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
