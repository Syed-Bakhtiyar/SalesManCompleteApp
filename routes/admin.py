from flask import request, json, jsonify
from roles import ROLES
from services.admin import createAdmin, authenticateUser

def admin(app):
    @app.route('/admin', methods=['POST'])
    def addAdmin():
        try:
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            email = request.form['email']
            password = request.form['password']
            user = createAdmin(first_name, last_name, email, password, ROLES['ADMIN'])
            return jsonify(user), 200
        except Exception as error:
            print('error in admin creation: ' + str(error))
            return jsonify({'message': 'internal server error'}), 500

    @app.route('/admin/auth', methods=['POST'])
    def authenticateAdmin():
        try:
            email = request.form['email']
            password = request.form['password']
            print(email, password)
            user = authenticateUser(email, password)
            if 'status' in user.keys() :
                if user['status'] == 401:
                    return jsonify({'message': user['message']}), 401
                if user['status'] == 500:
                    raise Exception
            print(user)
            return jsonify(user), 200
        except Exception as error:
            print(error)
            return jsonify({'message': str(error)}), 500