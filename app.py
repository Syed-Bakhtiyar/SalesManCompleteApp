from flask import Flask #, request, json
from flask_cors import CORS
from routes.admin import admin
from routes.company import company
from routes.manager import manager
from routes.areaManager import areaManager
from routes.shop import shop
from routes.activityCompetitorDisplay import activity
from routes.picture import picture
from routes.merchandiser import merchandiser
from routes.product import product


app = Flask(__name__)
# allow cross origin
CORS(app)

admin(app)
company(app)
manager(app)
areaManager(app)
shop(app)
activity(app)
picture(app)
merchandiser(app)
product(app)

if __name__ == '__main__':
    app.run(debug=True)
