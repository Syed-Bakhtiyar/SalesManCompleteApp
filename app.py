from flask import Flask #, request, json
from flask_cors import CORS
from routes.admin import admin
from routes.company import company
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
# allow cross origin
CORS(app)

admin(app)
company(app)
manager(app)
areaManager(app)
shop(app)
display(app)
ourActivity(app)
competitorActivity(app)     
picture(app)
merchandiser(app)
product(app)

if __name__ == '__main__':
    app.run(debug=True)
