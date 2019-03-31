import numpy as np
import pandas as pd
from ast import literal_eval
from flask import jsonify
from sklearn.externals import joblib

def data_processor(data):

    data_arr = np.array(literal_eval(data)).reshape(1, -1)

    svc1 = './saved_model_agency.pkl'
    svc2 = './saved_model_communion.pkl'

    #print("Loading the model...")
    model_agency = joblib.load(svc1) 
    model_communion = joblib.load(svc2) 

    #print("The model has been loaded...doing predictions now...")
    predictions_agency = model_agency.predict(data_arr)
    predictions_communion = model_communion.predict(data_arr)
    predictions = {"agency": str(predictions_agency), "communion": str(predictions_communion)}
    return predictions