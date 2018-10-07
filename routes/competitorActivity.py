from flask import request, json
from database_connection import connection

def competitorActivity(app):    
    @app.route('/competitorActivity', methods=['POST', 'GET'])
    def createCompActivity():
        if request.method == 'POST':
            shop_id = request.form['shop_id']
            product_type_id = request.form['product_type_id']
            product_sub_type_id = request.form['product_sub_type_id']
            comments = request.form['comments']
            image = request.form['image']
            date_today = request.form['date_today']
            connection.creatrCompActivity(shop_id, product_type_id, product_sub_type_id, comments, image, date_today)
            return shop_id
        else:
            return "hello"