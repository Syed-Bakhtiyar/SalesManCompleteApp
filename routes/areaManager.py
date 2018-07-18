from flask import request, json
from database_connection import connection

def areaManager(app):
    @app.route('/createareamanager', methods=['POST', 'GET'])
    def createAreaManager():
        if request.method == 'POST':
            manager_id = request.form['manager_id']
            name = request.form['name']
            password = request.form['password']
            time_stamp = request.form['date_today']
            latitude = request.form['latitude']
            longitude = request.form['longitude']
            connection.createAreaManager(manager_id, name, password, time_stamp, latitude, longitude)
            return name
        else:
            return "hello"
