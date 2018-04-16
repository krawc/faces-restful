from flask_restful import Resource
from flask import Flask, request

class HelloController(Resource):

    def get(self):
        return {"response" : "hello get"} 
    
    def post(self):
        content = request.json
        airport = content['airport']
        if (airport == 'JFK'):
            return {"delayed":"1"}
        else:
            return {"delayed":"0"}

    def put(self):
        return {"response" : "hello put"}

    def delete(self):
        return {"response" : "hello delete"}
