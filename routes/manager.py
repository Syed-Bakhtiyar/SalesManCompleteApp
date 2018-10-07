from flask import request, json
from services.manager import createManager, updateManager

def manager(app):
    @app.route('/manager', methods=['POST', 'GET'])
    def saveManager():
        if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']
            password = request.form['password']
            company_name = request.form['company_name']
            createManager(name, email, password, company_name, True)
            return name
        else:
            return "hello"

    @app.route('/manager/<id>', methods=['POST', 'GET'])
    def editManager():
        if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']
            password = request.form['password']
            company_name = request.form['company_name']
            updateManager(name, email, password, company_name, True)
            return name
        else:
            return "hello"
# raise Exception('x should not exceed 5. The value of x was: {}'.format(x))