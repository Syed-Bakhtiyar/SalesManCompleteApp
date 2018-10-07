from flask import request, json
from services.picture import createPictures

def picture(app):
    @app.route('/picture',methods = ['POST','GET'])
    def createPicture():
        if request.method == 'POST':
            shop_id = request.form['shop_id']
            comments = request.form['comments']
            image = request.form['image']
            date_today = request.form['date_today']
            createPictures(shop_id,comments,image,date_today)
            return shop_id
        else:
            return "hello"