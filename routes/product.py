from flask import request, json
from database_connection import connection

def product(app):
    @app.route('/createproduct', methods=['POST', 'GET'])
    def createProduct():
        if request.method == 'POST':
            manager_id = request.form['manager_id']
            product_type_title = request.form['product_type_title']
            product_sub_type_title = request.form['product_sub_type_title']
            product_title = request.form['product_title']
            image = request.form['image']
            connection.createProductType(manager_id, product_type_title, product_sub_type_title, product_title, image)
            return manager_id
        else:
            return "hello"
