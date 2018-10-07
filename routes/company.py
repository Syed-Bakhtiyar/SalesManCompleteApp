from flask import request, json
from services.company import createCompany

def company(app):
    @app.route('/admin/company', methods=['POST', 'GET'])
    def addCompany():
        if request.method == 'POST':
            adminId = request.form['adminId']
            name = request.form['name']
            createCompany(adminId,name)
            return name
        else:
            return "hello"
