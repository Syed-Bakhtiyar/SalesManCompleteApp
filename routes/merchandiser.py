from flask import request, json
from database_connection import connection

def merchandiser(app):
    @app.route('/createmerchandiser', methods=['POST', 'GET'])
    def createMerchandiser():
        if request.method == 'POST':
            area_manager_id = request.form['area_manager_id']
            shop_id = request.form['shop_id']
            name = request.form['name']
            email = request.form['email']
            passord = request.form['password']
            company_name = request.form['company_name']
            time_stamp = request.form['date_today']
            connection.createMerchandiser(area_manager_id, shop_id, name, email, passord, company_name, True, time_stamp)
            return name
        else:
            return "hello"