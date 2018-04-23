from __future__ import division
from flask_restful import Resource
from flask import Flask, request
from sklearn import preprocessing
from sklearn import metrics
from sklearn.model_selection import train_test_split #to split in train and test set
from sklearn.neural_network import MLPClassifier
import numpy as np
import pandas as pd
import dill as pickle
from sklearn import preprocessing
from data_processing import data_processor

class HelloController(Resource):

    def get(self):
        return {"response" : "hello get"} 
    
    def post(self):
        content = request.json
        data_arr = []

        month = content['month']
        dayOfWeek = content['dayOfWeek']
        hour = content['hour']
        airline = content['airline']
        airport_dep = content['airport_dep']
        airport_arr = content['airport_arr']

        data_arr = [month] + [dayOfWeek] + [hour] + [airline] + [airport_dep] + [airport_arr]
        return {"result":data_processor(data_arr)}

    def put(self):
        return {"response" : "hello put"}

    def delete(self):
        return {"response" : "hello delete"}
