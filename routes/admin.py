from flask import request, json
from services.admin import createAdmin

def admin(app):
    @app.route('/admin', methods=['POST', 'GET'])
    def addAdmin():
        if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']
            password = request.form['password']
            isOnline = request.form['isOnline']
            createAdmin(name, email, password,isOnline)
            return name
        else:
            return "hello"
