from cmd import IDENTCHARS
import sys
import flask
from flask import request, jsonify, Flask
import sqlite3
from flask_restful import Resource, Api, abort
from datetime import date, datetime
import re, json

import DatabaseController as db

app = flask.Flask(__name__)
#app.config["DEBUG"] = True

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


@app.route('/', methods=['GET'])
def home():
    return '''<h1>CAR FUELAGE DATABASE</h1>
<p>Contact Admin for API access</p>'''


@app.route('/api/post/user/new', methods=['POST'])
def postNewUser():
    content = request.get_json()
    print(content)
    query = '''INSERT INTO car.Users (Name) VALUES ("{}")'''.format(
                    content['Name']) 
    db.sqlInsert(query)
    return "Post successful"

@app.route('/api/post/car/new', methods=['POST'])
def postNewCar():
    content = request.get_json()
    print(content)
    query = '''INSERT INTO Car ('Car_Name', 'idUser') 
                VALUES ("{}","{}")'''.format(
                    content['Car_Name'], content['idUser']) 
    try:
        x = db.sqlInsert(query)
        print(x)
    except:
        return "Post failed"

@app.route('/api/post/data/new', methods=['POST'])
def postDataCar():
    content = request.get_json()
    print(content)
    query = '''INSERT INTO Refuel (Total_km, Trip_km, Litres, Litres_euro, Price_Total, idUser) 
    VALUES ("{}","{}","{}","{}","{}","{}")'''.format(
        content['Total_km'],
        content['Trip_km'],
        content['Litres'],
        content['Litres_euro'],
        content['Price_Total'],
        content['idUser'])
    db.sqlInsert(query)
    return "Post successful"



@app.route('/api/get/cars/all', methods=['GET']) 
def getAllCars():
    print (request.is_json)
    content = request.get_json()
    print(content)
    query = '''SELECT  Users.Name, Car_Name
                FROM Users
                Join Car 
                ON Car.idCar=Users.idCar'''
    
    response = db.sqlQuery(query)

    json_list = []
    for row in response:
        t = {"Name": row[0], 
             "Car Name":row[1]}
        json_list.append(t)
        
    json_list = json.dumps(json_list, indent=4)
    return json_list

@app.route('/api/post/user/update', methods=['POST']) 
def updateUser():
    print (request.is_json)
    content = request.get_json()
    print(content)
    query = '''UPDATE Users SET Name = "testi2" WHERE idUsers = {}'''
    
    response = db.sqlQuery(query)
    return jsonify(response)

@app.route('/api/get/cars/<user>', methods=['GET']) 
def getCarsByUser(user):
    print (request.is_json)
    content = request.get_json()
    print(content)
    query = '''SELECT   date_format(Timestamp, '%Y-%m-%d'),
                        Total_km,
                        Trip_km,
                        Litres,
                        Litres_euro,
                        Price_Total,
                        Name,
                        Car_Name
                        FROM SelectCarAll WHERE Name = "{}" ORDER BY Timestamp DESC LIMIT 10'''.format(user)
    response = db.sqlQuery(query)
     
    json_list = []
    for row in response:
        t = {"Time": row[0], 
             "Trip Total":row[1], 
             "Trip curr":row[2], 
             "Litres refuelled":row[3], 
             "Price per Litre":row[4], 
             "Total Price":row[5], 
             "Name":row[6], 
             "Car Name":row[7]}
        json_list.append(t)
        
    json_list = json.dumps(json_list, indent=4)
    return json_list
  
@app.route('/api/get/data/all', methods=['GET'])
def getDataAll():
    print (request.is_json)
    content = request.get_json()
    print(content)
    query = '''SELECT   date_format(Timestamp, '%Y-%m-%d'),
                        Total_km,
                        Trip_km,
                        Litres,
                        Litres_euro,
                        Price_Total,
                        Name,
                        Car_Name
                        FROM SelectCarAll ORDER BY Timestamp DESC'''
    response = db.sqlQuery(query)
    

    json_list = []
    for row in response:
        t = {"Time": row[0], 
             "Trip Total":row[1], 
             "Trip curr":row[2], 
             "Litres refuelled":row[3], 
             "Price per Litre":row[4], 
             "Total Price":row[5], 
             "Name":row[6], 
             "Car Name":row[7]}
        json_list.append(t)
        
    json_list = json.dumps(json_list, indent=4)
    return json_list

@app.route('/api/get/user/all', methods=['GET']) 
def getAllUsers():
    content = request.get_json()
    query = '''SELECT Name From Users'''
    response = db.sqlQuery(query)

    json_list = []
    for row in response:
        t = {"Name": row[0]}
        json_list.append(t)
        
    json_list = json.dumps(json_list, indent=4)
    return json_list


#Dog API
@app.route('/api/get/trainers/all', methods=['GET']) 
def getAllTrainers():
    content = request.get_json()
    print(content)
    query = '''SELECT name, idTrainer FROM Car.Trainer'''
    
    response = db.sqlQuery(query)

    json_list = []
    for row in response:
        t = {"name": row[0],
             "idTrainer": row[1]}
        json_list.append(t)
        
    json_list = json.dumps(json_list, indent=4)
    return json_list

@app.route('/api/get/dogs/all', methods=['GET']) 
def getAllDogs():
    content = request.get_json()
    print(content)
    query = '''SELECT name, idDog FROM Car.Dog'''
    
    response = db.sqlQuery(query)

    json_list = []
    for row in response:
        t = {"name": row[0],
             "idDog": row[1]}
        json_list.append(t)
        
    json_list = json.dumps(json_list, indent=4)
    return json_list

@app.route('/api/get/dogs/info', methods=['GET']) 
def getDogInfo():
    content = request.get_json()
    print(content)
    query = '''SELECT name, Weight, date_format(timestamp, '%Y-%m-%d') FROM Car.Dog Join Car.DogInfo ON Dog.idDog = DogInfo.idDog'''
    
    response = db.sqlQuery(query)

    json_list = []
    for row in response:
        t = {"name": row[0],
             "Weight": row[1],
             "timestamp": row[2]}
        json_list.append(t)
        
    json_list = json.dumps(json_list, indent=4)
    return json_list

@app.route('/api/get/trainingtype/all', methods=['GET']) 
def getAllTypes():
    content = request.get_json()
    print(content)
    query = '''SELECT duration, succesfullPasses, otherInfo FROM Car.TrainingType'''
    
    response = db.sqlQuery(query)

    json_list = []
    for row in response:
        t = {"duration": row[0],
             "succesfullPasses": row[1],
             "otherInfo": row[2]}
        json_list.append(t)
        
    json_list = json.dumps(json_list, indent=4)
    return json_list

@app.route('/api/get/training/all', methods=['GET']) 
def getAllTrainings():
    content = request.get_json()
    print(content)
    query = '''SELECT   date_format(timestamp, '%Y-%m-%d'), 
                        duration, 
                        succesfullPasses, 
                        otherInfo, 
                        Dog.name as dog,
                        Dog.idDog,
                        Trainer.name as trainer,
                        Trainer.idTrainer
                        FROM Car.Training 
                        JOIN Car.TrainingType 
                        ON Training.idType = TrainingType.idTrainingType 
                        JOIN Car.Dog 
                        On Training.idDog = Dog.idDog 
                        JOIN Car.Trainer 
                        ON Training.idTrainer = Trainer.idTrainer'''
    
    response = db.sqlQuery(query)

    json_list = []
    for row in response:
        t = {"timestamp":row[0],
            "duration": row[1],
             "succesfullPasses": row[2],
             "otherInfo": row[3],
             "dog": row[4],
             "idDog": row[5],
             "trainer": row[6],
             "idTrainer": row[7]}
        json_list.append(t)
        
    json_list = json.dumps(json_list, indent=4)
    return json_list

@app.route('/api/post/training/new', methods=['POST'])
def postTraining():
    content = request.get_json()
    query = '''INSERT INTO TrainingType (duration, succesfullPasses, otherInfo) 
    VALUES ("{}","{}","{}")'''.format(
        content['duration'],
        content['succesfullPasses'],
        content['otherInfo'])
    try:
        db.sqlInsert(query)
    except:
        return "Post failed"

    try:
        idTrainingType = db.sqlQuery("SELECT idTrainingType from TrainingType ORDER BY idTrainingType DESC Limit 1")
        idType = idTrainingType[0][0]
        #update training id
        newQuery = '''INSERT INTO Training (idDog,idTrainer,idType) VALUES ("{}","{}","{}")'''.format(
            content["idDog"],
            content["idTrainer"],
            idType)
        print(newQuery)
        db.sqlInsert(newQuery)
        return "200 Post Success" 
    except: 
        return "Update failed"
       
@app.route('/api/post/dog/info', methods=['POST'])
def postDogInfo():
    content = request.get_json()
    query = '''INSERT INTO DogInfo (Weight, idDog) 
    VALUES ("{}","{}")'''.format(
        content['Weight'],
        content['idDog'])
    try:
        db.sqlInsert(query)
        return "200 Post Success" 
    except: 
        return "Update failed"

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

if __name__ == "__main__":
	app.run()