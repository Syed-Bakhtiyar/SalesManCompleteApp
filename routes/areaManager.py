from flask import request, json
from services.areaManager import addAreaManager
from roles import ROLES

def areaManager(app):
    @app.route('/manager/<manager_id>/area-manager', methods=['POST', 'GET'])
    def createAreaManager(manager_id):
        if request.method == 'POST':
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            email = request.form['email']
            password = request.form['password']
            user = addAreaManager(manager_id, first_name, last_name, email, password, ROLES['AREAMANAGER'])
            return user
        else:
            return "hello"

# def areaManager(app):
#     @app.route('/areaManager', methods=['POST', 'GET'])
#     def createAreaManager():
#         if request.method == 'POST':
#             manager_id = request.form['manager_id']
#             name = request.form['name']
#             password = request.form['password']
#             time_stamp = request.form['date_today']
#             latitude = request.form['latitude']
#             longitude = request.form['longitude']
#             addAreaManager(manager_id, name, password, time_stamp, latitude, longitude)
#             return name
#         else:
#             return "hello"
