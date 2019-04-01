from flask import Flask
from flask import request
from flask_restful import Api
# from flask_cors import CORS
from controllers import helloController
from flask_sqlalchemy import SQLAlchemy
from data_processing import data_processor


app = Flask(__name__)

api = Api(app)

# cors = CORS(app, resources={'/api/*': {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

app.route('/foo', methods=['POST','OPTIONS'])
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///static/db/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


db = SQLAlchemy(app)

api.add_resource(helloController.HelloController, '/api/predict')

@app.after_request
def after_request(response):
    white_origin= ['https://faces-frontend.herokuapp.com','http://localhost']
    if request.headers['Origin'] in white_origin:
        response.headers['Access-Control-Allow-Origin'] = request.headers['Origin'] 
        response.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    return response

if __name__ == '__main__':
    app.run(debug=True)
