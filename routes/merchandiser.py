from flask import request, jsonify
from services.merchandiser import createMerchandiser, getAllMerchandisers
from roles import ROLES

def merchandiser(app):
    @app.route('/admin/<admin_id>/merchandiser', methods=['POST'])
    def addMerchandiser(admin_id):
        try:
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            email = request.form['email']
            password = request.form['password']
            user = createMerchandiser(admin_id, first_name, last_name, email, password, ROLES['MERCHANDISER'])
            return jsonify(user), 200
        except Exception as error:
           print('error in admin creation: ' + str(error))
           return jsonify({'message': 'internal server error'}), 500

    @app.route('/admin/<admin_id>/merchandisers')
    def getMerchandisers(admin_id):
        try:
            print(admin_id)
            merchandisers = getAllMerchandisers(admin_id);
            if 'status' in merchandisers.keys() :
                if merchandisers['status'] == 404:
                    return jsonify({'message': merchandisers['message']}), 404
                if merchandisers['status'] == 500:
                    raise Exception
            return jsonify(merchandisers), 200
        except Exception as error:
            print(error)
            return jsonify({'message': 'internal server error'}), 500

# def merchandiser(app):
#     @app.route('/merchandiser', methods=['POST', 'GET'])
#     def addMerchandiser():
#         if request.method == 'POST':
#             area_manager_id = request.form['area_manager_id']
#             shop_id = request.form['shop_id']
#             name = request.form['name']
#             email = request.form['email']
#             passord = request.form['password']
#             company_name = request.form['company_name']
#             time_stamp = request.form['date_today']
#             createMerchandiser(area_manager_id, shop_id, name, email, passord, company_name, True, time_stamp)
#             return name
#         else:
#             return "hello"