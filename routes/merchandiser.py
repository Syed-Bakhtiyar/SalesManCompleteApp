from flask import request, json
from services.merchandiser import createMerchandiser

def merchandiser(app):
    @app.route('/merchandiser', methods=['POST', 'GET'])
    def addMerchandiser():
        if request.method == 'POST':
            area_manager_id = request.form['area_manager_id']
            shop_id = request.form['shop_id']
            name = request.form['name']
            email = request.form['email']
            passord = request.form['password']
            company_name = request.form['company_name']
            time_stamp = request.form['date_today']
            createMerchandiser(area_manager_id, shop_id, name, email, passord, company_name, True, time_stamp)
            return name
        else:
            return "hello"