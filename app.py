from flask import Flask #, request, json
# from database_connection import Connection
# import base64
from routes.manager import manager
from routes.areaManager import areaManager
from routes.shop import shop
from routes.display import display
from routes.activity import ourActivity
from routes.competitorActivity import competitorActivity
from routes.picture import picture
from routes.merchandiser import merchandiser
from routes.product import product


app = Flask(__name__)

manager(app)
areaManager(app)
shop(app)
display(app)
ourActivity(app)
competitorActivity(app)     
picture(app)
merchandiser(app)
product(app)

# @app.route('/')
# def helloWorld():
#     return "Hello world"


# @app.route('/createmanager', methods=['POST', 'GET'])
# def createManager():
#     if request.method == 'POST':
#         name = request.form['name']
#         email = request.form['email']
#         password = request.form['password']
#         company_name = request.form['company_name']
#         connection.createManager(name, email, password, company_name, True)
#         return name
#     else:
        # return "hello"


# @app.route('/createareamanager', methods=['POST', 'GET'])
# def createAreaManager():
#     if request.method == 'POST':
#         manager_id = request.form['manager_id']
#         name = request.form['name']
#         password = request.form['password']
#         time_stamp = request.form['date_today']
#         latitude = request.form['latitude']
#         longitude = request.form['longitude']
#         connection.createAreaManager(manager_id, name, password, time_stamp, latitude, longitude)
#         return name
#     else:
#         return "hello"


# @app.route('/createmerchandiser', methods=['POST', 'GET'])
# def createMerchandiser():
#     if request.method == 'POST':
#         area_manager_id = request.form['area_manager_id']
#         shop_id = request.form['shop_id']
#         name = request.form['name']
#         email = request.form['email']
#         passord = request.form['password']
#         company_name = request.form['company_name']
#         time_stamp = request.form['date_today']
#         connection.createMerchandiser(area_manager_id, shop_id, name, email, passord, company_name, True, time_stamp)
#         return name
#     else:
#         return "hello"


# @app.route('/createshop', methods=['POST', 'GET'])
# def createShop():
#     if request.method == 'POST':
#         manager_id = request.form['manager_id']
#         area_manager_id = request.form['area_manager_id']
#         merch_id = request.form['merch_id']
#         shop_name = request.form['shop_name']
#         connection.createShop(manager_id, area_manager_id, merch_id, shop_name)
#         return shop_name
#     else:
#         return "hello"


# @app.route('/createdisplay', methods=['POST', 'GET'])
# def createDisplay():
#     if request.method == 'POST':
#         shop_id = request.form['shop_id']
#         product_type_id = request.form['product_type_id']
#         product_sub_type_id = request.form['product_sub_type_id']
#         comments = request.form['comments']
#         image = request.form['image']
#         date_today = request.form['date_today']
#         connection.createDisplay(shop_id, product_type_id, product_sub_type_id, comments, image, date_today)
#         return shop_id
#     else:
#         return "hello"


# @app.route('/createouractivity', methods=['POST', 'GET'])
# def createOurActivity():
#     if request.method == 'POST':
#         shop_id = request.form['shop_id']
#         product_type_id = request.form['product_type_id']
#         product_sub_type_id = request.form['product_sub_type_id']
#         comments = request.form['comments']
#         image = request.form['image']
#         date_today = request.form['date_today']
#         connection.creatrOurActivity(shop_id, product_type_id, product_sub_type_id, comments, image, date_today)
#         return shop_id
#     else:
#         return "hello"


# @app.route('/createcompactivity', methods=['POST', 'GET'])
# def createCompActivity():
#     if request.method == 'POST':
#         shop_id = request.form['shop_id']
#         product_type_id = request.form['product_type_id']
#         product_sub_type_id = request.form['product_sub_type_id']
#         comments = request.form['comments']
#         image = request.form['image']
#         date_today = request.form['date_today']
#         connection.creatrCompActivity(shop_id, product_type_id, product_sub_type_id, comments, image, date_today)
#         return shop_id
#     else:
#         return "hello"


# @app.route('/createpicture',methods = ['POST','GET'])
# def createPicture():
#     if request.method == 'POST':
#         shop_id = request.form['shop_id']
#         comments = request.form['comments']
#         image = request.form['image']
#         date_today = request.form['date_today']
#         connection.createPictures(shop_id,comments,image,date_today)
#         return shop_id
#     else:
#         return "hello"


# @app.route('/createproduct', methods=['POST', 'GET'])
# def createProduct():
#     if request.method == 'POST':
#         manager_id = request.form['manager_id']
#         product_type_title = request.form['product_type_title']
#         product_sub_type_title = request.form['product_sub_type_title']
#         product_title = request.form['product_title']
#         image = request.form['image']
#         connection.createProductType(manager_id, product_type_title, product_sub_type_title, product_title, image)
#         return manager_id
#     else:
#         return "hello"


# @app.route('/createisavailable', methods=['POST', 'GET'])
# def isAvailable():
#     if request.method == 'POST':
#         product_id = request.form['product_id']
#         shop_id = request.form['shop_id']
#         is_active = request.form['is_active']
#         connection.createIsAvailable(product_id, shop_id, is_active)
#         return product_id
#     else:
#         return "hello"


if __name__ == '__main__':
    app.run(debug=True)
