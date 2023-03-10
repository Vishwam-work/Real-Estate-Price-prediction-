from flask import Flask,request,jsonify
import util
app=Flask(__name__) 

@app.route("/Display")
def geget_location():
    response = jsonify({
        'location':util.get_location()
    })



if __name__=='__main__':
    print("Server in on")
    app.run() 