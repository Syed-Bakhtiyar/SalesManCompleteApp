from flask import request, json
from services.shop import createShop

def shop(app):
    @app.route('/company/<company_id>/shop', methods=['POST', 'GET'])
    def addShop(company_id):
        if request.method == 'POST':
            shop_name = request.form['shop_name']
            latitude = request.form['latitude']
            longitude = request.form['longitude']
            createShop(company_id, shop_name, latitude, longitude)
            return shop_name
        else:
            return "hello"
