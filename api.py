from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from controllers import helloController
from flask_sqlalchemy import SQLAlchemy
from data_processing import data_processor


app = Flask(__name__)

api = Api(app)

cors = CORS(app, resources={r'/api/*': {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

app.route('/foo', methods=['POST','OPTIONS'])
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///static/db/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


db = SQLAlchemy(app)

api.add_resource(helloController.HelloController, '/api/predict')

if __name__ == '__main__':
    app.run(debug=True)
