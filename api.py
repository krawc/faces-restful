from flask import Flask
from flask_restful import Api
from flask_cors import CORS, cross_origin
from controllers import helloController
from flask_sqlalchemy import SQLAlchemy
from data_processing import data_processor


app = Flask(__name__)

api = Api(app)

app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy   dog'
app.config['CORS_HEADERS'] = 'Content-Type'

cors = CORS(app, resources={r"/api/predict": {"origins": "http://localhost:port"}})

@app.route('/api/predict', methods=['POST'])
@cross_origin(origin='/api/predict',headers=['Content- Type','Authorization'])


db = SQLAlchemy(app)

api.add_resource(helloController.HelloController, '/api/predict')

if __name__ == '__main__':
    app.run(debug=True)
