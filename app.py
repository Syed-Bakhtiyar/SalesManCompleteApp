from flask import Flask,request,json
from database_connection import Connection
app = Flask(__name__)

connection = Connection();

@app.route('/')
def helloWorld():
    return "Hello world"

@app.route('/createmanager',methods = ['POST','GET'])
def createManager():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        company_name = request.form['company_name']
        connection.createManager( name, email, password, company_name, True)
        return name
    else:
        return "hello"

@app.route('/createareamanager',methods = ['POST','GET'])
def createAreaManager():
    if request.method == 'POST':
        manager_id = request.form['manager_id']
        name = request.form['name']
        password = request.form['password']
        time_stamp = request.form['date_today']
        latitude = request.form['latitude']
        longitude = request.form['longitude']
        connection.createAreaManager( manager_id, name, password, time_stamp, latitude, longitude)
        return name
    else:
        return "hello"


if __name__ == '__main__':
    connection.createManager("bakhtiiyar", "bakhtiyar@sanu.com", "abcdefg", "Got It?", True)
    # app.run(debug=True)