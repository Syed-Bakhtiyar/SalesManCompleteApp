from flask import request, jsonify
from services.areaManager import addAreaManager, getAllAreaManagers
from roles import ROLES

def areaManager(app):
    @app.route('/admin/<admin_id>/area-manager', methods=['POST'])
    def createAreaManager(admin_id):
        try:
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            email = request.form['email']
            password = request.form['password']
            user = addAreaManager(admin_id, first_name, last_name, email, password, ROLES['AREAMANAGER'])
            return jsonify(user), 200
        except Exception as error:
           print('error in admin creation: ' + str(error))
           return jsonify({'message': 'internal server error'}), 500
    
    @app.route('/admin/<admin_id>/area-manager')
    def getAreaManagers(admin_id):
        try:
            print(admin_id)
            areaManagers = getAllAreaManagers(admin_id);
            if 'status' in areaManagers.keys() :
                if areaManagers['status'] == 404:
                    return jsonify({'message': areaManagers['message']}), 404
                if areaManagers['status'] == 500:
                    raise Exception
            return jsonify(areaManagers), 200
        except Exception as error:
            print(error)
            return jsonify({'message': 'internal server error'}), 500

# def areaManager(app):
#     @app.route('/areaManager', methods=['POST', 'GET'])
#     def createAreaManager():
#         if request.method == 'POST':
#             manager_id = request.form['manager_id']
#             name = request.form['name']
#             password = request.form['password']
#             time_stamp = request.form['date_today']
#             latitude = request.form['latitude']
#             longitude = request.form['longitude']
#             addAreaManager(manager_id, name, password, time_stamp, latitude, longitude)
#             return name
#         else:
#             return "hello"
