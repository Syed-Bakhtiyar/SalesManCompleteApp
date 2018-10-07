from flask import request, json
from services.merchandiser import createMerchandiser
from roles import ROLES

def merchandiser(app):
    @app.route('/area-manager/<am_id>/merchandiser', methods=['POST', 'GET'])
    def addMerchandiser(am_id):
        if request.method == 'POST':
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            email = request.form['email']
            password = request.form['password']
            user = createMerchandiser(am_id, first_name, last_name, email, password, ROLES['MERCHANDISER'])
            return user
        else:
            return "hello"

# def merchandiser(app):
#     @app.route('/merchandiser', methods=['POST', 'GET'])
#     def addMerchandiser():
#         if request.method == 'POST':
#             area_manager_id = request.form['area_manager_id']
#             shop_id = request.form['shop_id']
#             name = request.form['name']
#             email = request.form['email']
#             passord = request.form['password']
#             company_name = request.form['company_name']
#             time_stamp = request.form['date_today']
#             createMerchandiser(area_manager_id, shop_id, name, email, passord, company_name, True, time_stamp)
#             return name
#         else:
#             return "hello"