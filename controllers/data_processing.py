import numpy as np
import pandas as pd
import dill as pickle

def data_processor(data):

    svc1 = './saved_model_agency.pkl'
    svc2 = './saved_model_communion.pkl'

    #print("Loading the model...")
    model_agency = None
    with open(svc1,'rb') as f:
        model_agency = pickle.load(f)

    model_communion = None
    with open(svc1,'rb') as g:
        model_communion = pickle.load(g)

    #print("The model has been loaded...doing predictions now...")
    predictions_agency = model_agency.predict(data)
    predictions_communion = model_communion.predict(data)
    predictions = "Agency: " + str(predictions_agency) + " Communion: " + str(predictions_communion)
    return predictions