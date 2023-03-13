import json
import pickle
import numpy as np
__location=None
__data_columns=None
__model=None


def asii_price(location,sqft,BHK,bath):
    try:
        loc_index=__data_columns.index(location.lower())
    except:
        loc_index=-1
    x=np.zeros(len(__data_columns))
    x[0]=sqft
    x[1]=BHK
    x[2]=bath
    if loc_index>=0:
        x[loc_index]=1
    return round(__model.predict([x])[0],2)

# load the artifact means load the pickel and json model
def load_saved_aritfacts():
    print("LOADING THE ARTIFACTS......")
    global __data_columns
    global __location
    global __model

    f = open('columns.json','r')
    __data_columns=json.load(f)['data_columns']
    __location = __data_columns[3:]
    with open("Home_prices_model.pickle",'rb') as f:
         __model = pickle.load(f)
    print("Loading is Done")
def get_location():
    return __location
def get_data_column():
    return __data_columns

if __name__=='__main__':
    load_saved_aritfacts()

    print(get_location())
    print(asii_price('1st Block Jayanagar',1000,3,3))
    print(asii_price('1st Block Jayanagar',1000,2,2))
    print(asii_price('2nd Stage Nagarbhavi',1000,3,3))
    print(asii_price('6th Phase JP Nagar',1000,3,3))
