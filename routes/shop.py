from flask import request, json
from services.shop import createShop

def shop(app):
    @app.route('/shop', methods=['POST', 'GET'])
    def addShop():
        if request.method == 'POST':
            manager_id = request.form['manager_id']
            area_manager_id = request.form['area_manager_id']
            merch_id = request.form['merch_id']
            shop_name = request.form['shop_name']
            createShop(manager_id, area_manager_id, merch_id, shop_name)
            return shop_name
        else:
            return "hello"
