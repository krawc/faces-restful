from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from controllers import helloController
from flask_sqlalchemy import SQLAlchemy
from data_processing import data_processor


app = Flask(__name__)

cors = CORS(app, resources={r"*": {"origins": "*"}})

api = Api(app)

# cors = CORS(app, resources={r'/api/*': {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

app.route('/foo', methods=['POST','OPTIONS'])
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///static/db/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


db = SQLAlchemy(app)

api.add_resource(helloController.HelloController, '/api/predict')

@app.after_request

def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
  return response

if __name__ == '__main__':
    app.run(debug=True)
