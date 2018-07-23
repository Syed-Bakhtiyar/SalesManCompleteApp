from flask import request, json
from services.product import createProduct, createProductType, createProductSubType

def product(app):
    @app.route('/createproduct', methods=['POST', 'GET'])
    def addProduct():
        if request.method == 'POST':
            manager_id = request.form['manager_id']
            product_type_id = request.form['product_type_id']
            product_sub_type_id = request.form['product_sub_type_id']
            product_title = request.form['product_title']
            image = request.form['image']
            createProduct(manager_id, product_sub_type_id, product_title, image)
            return manager_id
        else:
            return "hello"
    
    @app.route('/productType', methods = ['POST', 'GET'])
    def addProductType():
        if request.method == 'POST':
            manager_id = request.form['manager_id']
            product_title = request.form['title']:
            createProductType(manager_id, product_title)
        else:
            return 'hello'

    @app.route('/createProductSubType', methods=['POST', 'GET'])
    def addProductSubType():
        if request.method == 'POST':
            product_type_id = request.form['product_type_id']
            product_title = request.form['title']:
            createProductSubType(product_type_id, product_title)
        else:
            return 'hello'