from flask import Flask
from flask_restful import Api
from flask_cors import CORS, cross_origin
from controllers import helloController
from flask_sqlalchemy import SQLAlchemy
from data_processing import data_processor


app = Flask(__name__)


cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

app.route('/api/predict', methods=['POST','OPTIONS'])
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///static/db/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

api = Api(app)


db = SQLAlchemy(app)

@app.route("/")
api.add_resource(helloController.HelloController, '/api/predict')

if __name__ == '__main__':
    app.run(debug=True)
