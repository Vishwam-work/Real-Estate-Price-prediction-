from flask import Flask,request,jsonify
import util
app=Flask(__name__) 

@app.route("/get_location",methods=['GET'])
def get_location():
    response = jsonify({
        'location':util.get_location()
    })
    response.headers.add('Access-control-Allow-Origin','*')
    return response

@app.route("/predict_home_price",methods=['POST'])
def predict_home_price():
    total_sqft=float(request.form['total_sqft'])
    location=(request.form['location'])
    BHK=int(request.form['BHK'])
    bath=int(request.form['bath'])
    response=jsonify({
        'estimated_price':util.asii_price(location,total_sqft,BHK,bath)
    })
    response.headers.add('Access-control-Allow-Origin','*')
    return response

if __name__=='__main__':
    print("Server in on")
    util.load_saved_aritfacts()
    app.run() 