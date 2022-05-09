import requests
from flask import Flask, request
from calculation import Calculation

app = Flask(__name__)

@app.route('/')
def hello_world():
    response={"message":"Hello, EATLab"}
    return response


@app.route('/calculate', methods=['POST'])
def calculate():
    data=request.get_json()
    calculation=Calculation()
    number_of_centroid=data['K']
    number_of_coordinates=data["N"]
    measure=data["measure"]
    if(bool(number_of_centroid) is True and bool(number_of_coordinates) is True and bool(measure) is True):
        count=calculation.calculate(number_of_centroid, number_of_coordinates, measure)
        response={"Count":count}
    else:
        response={"Error": "Your input data is either incorrect or missing"}
    return response

@app.route('/minradius', methods=['POST'])
def minimum_radius():
    data=request.get_json()
    calculation=Calculation()
    number_of_centroid=data['K']
    number_of_coordinates=data["N"]
    if(bool(number_of_centroid) is True and bool(number_of_coordinates) is True):
        radius=calculation.minimum_radius(number_of_centroid, number_of_coordinates)
        response={"Minimum radius": radius}
    else:
        response={"Error": "Your input data is either incorrect or missing"}
    return response

if __name__ == "__main__":
    app.run(threaded=True, port=5000)