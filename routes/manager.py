from flask import request, json
from database_connection import connection
from services.manager import createManager

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
    def updateManager():
        if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']
            password = request.form['password']
            company_name = request.form['company_name']
            connection.createManager(name, email, password, company_name, True)
            return name
        else:
            return "hello"
