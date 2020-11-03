from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3


class Item(Resource):
    TABLE_NAME = "items"
    parser = reqparse.RequestParser()
    parser.add_argument('price',type=float,required=True,help="This field can not be left blank!")

    @classmethod
    def find_by_name(cls,name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM {table} WHERE name=?".format(table=cls.TABLE_NAME)
        result = cursor.execute(query,(name,))
        row = result.fetchone()
        connection.close()
        if row:
            return{'item':{'name':row[0],'price':row[1]}}
    @classmethod
    def insert(cls,item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "INSERT into {table} VALUES(?,?)".format(table=cls.TABLE_NAME)
        cursor.execute(query,(item['name'],item['price']))
        connection.commit()
        connection.close()
        

    @jwt_required()
    def get(self,name):
        item = self.find_by_name(name)
        if item:
            return item
        return {"message":"Item not found"}, 404  
    @jwt_required()
    def post(self,name):
        if self.find_by_name(name):
            return {"message":"An item with name '{}' already exist".format(name)}
        data = Item.parser.parse_args()
        item = {"name":name,"price":data['price']}
        try:
            Item.insert(item)
        except Exception as e:
        #print(str(e))
            return {"message":"An error occurred inserting the item"}
        return item        
