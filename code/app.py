from flask import Flask,request
from flask_restful import Api,Resource,reqparse
from security import identity,authenticate
from flask_jwt import JWT, jwt_required, current_identity

app = Flask(__name__)
app.secret_key="princeisagoodboy1298"
api = Api(app)

jwt = JWT(app,authenticate,identity)


app.run(debug=True)
