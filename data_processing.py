import numpy as np
import pandas as pd
import dill as pickle

def data_processor(data):

    clf = './model_v3_sc.pk'

    airlines = ['airline_AA','airline_AS','airline_B6','airline_DL','airline_UA','airline_WN']
    departure_airports = ['airport_dep_ABE','airport_dep_ABQ','airport_dep_ACK','airport_dep_AGS','airport_dep_ALB','airport_dep_AMA','airport_dep_ANC','airport_dep_ATL','airport_dep_ATW','airport_dep_AUS','airport_dep_AVL','airport_dep_AVP','airport_dep_BDL','airport_dep_BGR','airport_dep_BHM','airport_dep_BIL','airport_dep_BIS','airport_dep_BLI','airport_dep_BNA','airport_dep_BOI','airport_dep_BOS','airport_dep_BQN','airport_dep_BSM','airport_dep_BTR','airport_dep_BTV','airport_dep_BUF','airport_dep_BUR','airport_dep_BWI','airport_dep_BZN','airport_dep_CAE','airport_dep_CAK','airport_dep_CHA','airport_dep_CHO','airport_dep_CHS','airport_dep_CLE','airport_dep_CLT','airport_dep_CMH','airport_dep_COS','airport_dep_CRP','airport_dep_CRW','airport_dep_CVG','airport_dep_DAB','airport_dep_DAL','airport_dep_DAY','airport_dep_DCA','airport_dep_DEN','airport_dep_DFW','airport_dep_DLH','airport_dep_DSM','airport_dep_DTW','airport_dep_ECP','airport_dep_EGE','airport_dep_ELP','airport_dep_EVV','airport_dep_EWR','airport_dep_EYW','airport_dep_FAI','airport_dep_FAR','airport_dep_FAT','airport_dep_FAY','airport_dep_FCA','airport_dep_FLL','airport_dep_FNT','airport_dep_FSD','airport_dep_GEG','airport_dep_GNV','airport_dep_GPT','airport_dep_GRB','airport_dep_GRR','airport_dep_GSO','airport_dep_GSP','airport_dep_GUC','airport_dep_GUM','airport_dep_HDN','airport_dep_HNL','airport_dep_HOU','airport_dep_HPN','airport_dep_HRL','airport_dep_HSV','airport_dep_HYA','airport_dep_IAD','airport_dep_IAH','airport_dep_ICT','airport_dep_ILM','airport_dep_IND','airport_dep_ISP','airport_dep_ITO','airport_dep_JAC','airport_dep_JAN','airport_dep_JAX','airport_dep_JFK','airport_dep_JNU','airport_dep_KOA','airport_dep_KTN','airport_dep_LAS','airport_dep_LAX','airport_dep_LBB','airport_dep_LEX','airport_dep_LFT','airport_dep_LGA','airport_dep_LGB','airport_dep_LIH','airport_dep_LIT','airport_dep_MAF','airport_dep_MCI','airport_dep_MCO','airport_dep_MDT','airport_dep_MDW','airport_dep_MEM','airport_dep_MFE','airport_dep_MHT','airport_dep_MIA','airport_dep_MKE','airport_dep_MLB','airport_dep_MOB','airport_dep_MSN','airport_dep_MSO','airport_dep_MSP','airport_dep_MSY','airport_dep_MTJ','airport_dep_MVY','airport_dep_MYR','airport_dep_OAK','airport_dep_OGG','airport_dep_OKC','airport_dep_OMA','airport_dep_ONT','airport_dep_ORD','airport_dep_ORF','airport_dep_ORH','airport_dep_PBI','airport_dep_PDX','airport_dep_PHL','airport_dep_PHX','airport_dep_PIT','airport_dep_PNS','airport_dep_PSC','airport_dep_PSE','airport_dep_PSP','airport_dep_PVD','airport_dep_PWM','airport_dep_RAP','airport_dep_RDU','airport_dep_RIC','airport_dep_RNO','airport_dep_ROA','airport_dep_ROC','airport_dep_RSW','airport_dep_SAN','airport_dep_SAT','airport_dep_SAV','airport_dep_SDF','airport_dep_SEA','airport_dep_SFO','airport_dep_SGF','airport_dep_SHV','airport_dep_SIT','airport_dep_SJC','airport_dep_SJU','airport_dep_SLC','airport_dep_SMF','airport_dep_SNA','airport_dep_SRQ','airport_dep_STL','airport_dep_STT','airport_dep_STX','airport_dep_SWF','airport_dep_SYR','airport_dep_TLH','airport_dep_TPA','airport_dep_TRI','airport_dep_TUL','airport_dep_TUS','airport_dep_TVC','airport_dep_TYS','airport_dep_VPS','airport_dep_XNA']
    arrival_airports = ['airport_arr_ABQ','airport_arr_ATL','airport_arr_AUS','airport_arr_BDL','airport_arr_BNA','airport_arr_BOS','airport_arr_BUF','airport_arr_BUR','airport_arr_BWI','airport_arr_CLE','airport_arr_CLT','airport_arr_CMH','airport_arr_CVG','airport_arr_DAL','airport_arr_DCA','airport_arr_DEN','airport_arr_DFW','airport_arr_DTW','airport_arr_EWR','airport_arr_FLL','airport_arr_HNL','airport_arr_HOU','airport_arr_IAD','airport_arr_IAH','airport_arr_IND','airport_arr_JAX','airport_arr_JFK','airport_arr_LAS','airport_arr_LAX','airport_arr_LGA','airport_arr_MCI','airport_arr_MCO','airport_arr_MDW','airport_arr_MIA','airport_arr_MKE','airport_arr_MSP','airport_arr_MSY','airport_arr_OAK','airport_arr_OGG','airport_arr_OMA','airport_arr_ONT','airport_arr_ORD','airport_arr_PBI','airport_arr_PDX','airport_arr_PHL','airport_arr_PHX','airport_arr_PIT','airport_arr_RDU','airport_arr_RSW','airport_arr_SAN','airport_arr_SAT','airport_arr_SEA','airport_arr_SFO','airport_arr_SJC','airport_arr_SJU','airport_arr_SLC','airport_arr_SMF','airport_arr_SNA','airport_arr_STL','airport_arr_TPA']

    API_month = [10]
    API_dayOfWeek = [4]
    API_hour = [1055]
    API_airline = [0] * len(airlines)
    API_airport_dep = [0] * len(departure_airports)
    API_airport_arr = [0] * len(arrival_airports)

    for x in range(0, len(airlines)):
        if data[3] == airlines[x]:
            API_airline[x] = 1
        else:
            API_airline[x] = 0

    for x in range(0, len(departure_airports)):
        if data[4] == departure_airports[x]:
            API_airport_dep[x] = 1
        else:
            API_airport_dep[x] = 0

    for x in range(0, len(arrival_airports)):
        if data[5] == arrival_airports[x]:
            API_airport_arr[x] = 1
        else:
            API_airport_arr[x] = 0

    data_array = API_month + API_dayOfWeek + API_hour + API_airline + API_airport_dep + API_airport_arr

    test = np.array(data_array)

    testScaled = (test - np.mean(test, axis=0)) / (np.std(test, axis=0))

    testScaled = testScaled.reshape(1, -1)

    #print("Loading the model...")
    loaded_model = None
    with open(clf,'rb') as f:
        loaded_model = pickle.load(f)

    #print(loaded_model)

    #print("The model has been loaded...doing predictions now...")
    predictions = loaded_model.predict(testScaled)
    prediction_series = list(pd.Series(predictions))
    #print(prediction_series[0])
    if (prediction_series[0] == 1):
        return 'HOLDUP'
    else:
        return 'ONTIME'
