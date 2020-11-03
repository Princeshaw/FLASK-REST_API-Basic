from flask import Flask,request
from flask_restful import Api,Resource,reqparse
from security import identity,authenticate
from flask_jwt import JWT, jwt_required, current_identity
import sqlite3 
from items import Item

connection = sqlite3.connect('data.db')
cursor = connection.cursor()


app = Flask(__name__)
app.secret_key="princeisagoodboy1298"
api = Api(app)

jwt = JWT(app,authenticate,identity)

api.add_resource(Item,'/item/<string:name>')

app.run(debug=True)
