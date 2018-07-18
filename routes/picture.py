from flask import request, json
from database_connection import connection

def picture(app):
    @app.route('/createpicture',methods = ['POST','GET'])
    def createPicture():
        if request.method == 'POST':
            shop_id = request.form['shop_id']
            comments = request.form['comments']
            image = request.form['image']
            date_today = request.form['date_today']
            connection.createPictures(shop_id,comments,image,date_today)
            return shop_id
        else:
            return "hello"