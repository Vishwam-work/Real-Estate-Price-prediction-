import json
import pickle
__location=None
__data_columns=None
__model=None
def get_location():
    return __location

def load_saved_aritfacts():
    print("LOADING THE ARTIFACTS......")
    global __data_columns
    global __location
    global __model

    with open("./artifacts/columns.json",'r') as f:
        __data_columns=json.load(f)['data_columns']
        __location = __data_columns[3:]
    with open("./artifacts/Home_prices_model.pickle",'rb') as f:
        __model = pickle.load(f)
    print("Loading is Done")

if __name__=='__main__':
    load_saved_aritfacts()
    print(get_location())
    