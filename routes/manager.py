from flask import request, jsonify
from services.manager import createManager, updateManager, getAllManagers
from services.user import createUser
from roles import ROLES

def manager(app):
    @app.route('/admin/<admin_id>/manager', methods=['POST'])
    def saveManager(admin_id):
        try:
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            email = request.form['email']
            password = request.form['password']
            user = createManager(admin_id, first_name, last_name, email, password, ROLES['MANAGER'])
            return jsonify(user), 200
        except Exception as error:
           print('error in admin creation: ' + str(error))
           return jsonify({'message': 'internal server error'}), 500

    @app.route('/admin/<admin_id>/manager')
    def getManagers(admin_id):
        try:
            print(admin_id)
            managers = getAllManagers(admin_id);
            if 'status' in managers.keys() :
                if managers['status'] == 404:
                    return jsonify({'message': managers['message']}), 404
                if managers['status'] == 500:
                    raise Exception
            return jsonify(managers), 200
        except Exception as error:
            print(error)
            return jsonify({'message': 'internal server error'}), 500

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