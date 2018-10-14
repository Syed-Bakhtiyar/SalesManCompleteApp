from flask import request, json
# from services.admin import createAdmin
from roles import ROLES
from services.admin import createAdmin

def admin(app):
    @app.route('/admin', methods=['POST', 'GET'])
    def addAdmin():
        if request.method == 'POST':
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            email = request.form['email']
            password = request.form['password']
            user = createAdmin(first_name, last_name, email, password, ROLES['ADMIN'])
            print(user)
            return user
        else:
            return "hello"
