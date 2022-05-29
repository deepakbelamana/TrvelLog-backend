from flask import Blueprint, jsonify,request
from flask_cors import cross_origin
from flask_cors import cross_origin
import json
from mongodbConnection import connectToDb

registerUserValidator=Blueprint('registerUserValidator',__name__)

database=connectToDb()

@registerUserValidator.route('/app/register',methods=['post'])
@cross_origin()
def registerUser():
    if(type(database)!= str):
        collection=database.users
        userData=request.data
        userData=userData.decode()
        userData=json.loads(userData)
        userExists=True if collection.count_documents({'userEmail':userData['userEmail']})!=0 else False #checking user exists are not by checking with their useremail by getting docs count 
        if(userExists):
            return jsonify(['there is an account already associated with this email, Try other email or login with the same email'])
        else:
            if(userData['userPassword']==userData['userReTypedPassword']):
                userData.pop('userReTypedPassword',None) #not inserting retyped password
                insertUser=userData
                collection.insert_one(insertUser)
                return jsonify(['Registration Successfull'])
            else:
                return jsonify(['re-Entered password does not matched ,re enter the same password'])
    else:
        print(database)
        return jsonify(['Servers Unreachable Try again'])
    