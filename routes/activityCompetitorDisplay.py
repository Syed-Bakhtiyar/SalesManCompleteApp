from flask import request, json
from services.activityCompetitorDisplay import createActivity

def activity(app):
    @app.route('/activity', methods=['POST', 'GET'])
    def addOurActivity():
        if request.method == 'POST':
            shop_id = request.form['shop_id']
            product_type_id = request.form['product_type_id']
            product_sub_type_id = request.form['product_sub_type_id']
            comments = request.form['comments']
            image = request.form['image']
            activity_type = request.form['activity_type']
            date_today = request.form['date_today']
            creatrActivity(shop_id, product_type_id, product_sub_type_id, comments, image, activity_type, date_today)
            return shop_id
        else:
            return "hello"
