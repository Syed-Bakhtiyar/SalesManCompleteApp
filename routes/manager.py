from flask import request, json
from services.manager import createManager, updateManager
from services.user import createUser
from roles import ROLES

def manager(app):
    @app.route('/admin/<admin_id>/manager', methods=['POST', 'GET'])
    def saveManager(admin_id):
        if request.method == 'POST':
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            email = request.form['email']
            password = request.form['password']
            user = createManager(admin_id, first_name, last_name, email, password, ROLES['MANAGER'])
            return user
        else:
            return "hello"

    @app.route('/admin/<id>/manager', methods=['POST', 'GET'])
    def editManager(id):
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