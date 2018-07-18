from flask import request, json
from database_connection import connection

def shop(app):
    @app.route('/createshop', methods=['POST', 'GET'])
    def createShop():
        if request.method == 'POST':
            manager_id = request.form['manager_id']
            area_manager_id = request.form['area_manager_id']
            merch_id = request.form['merch_id']
            shop_name = request.form['shop_name']
            connection.createShop(manager_id, area_manager_id, merch_id, shop_name)
            return shop_name
        else:
            return "hello"
