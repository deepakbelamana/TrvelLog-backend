from flask import Blueprint
from flask_cors import cross_origin
from flask_cors import cross_origin

from mongodbConnection import connectToDb

registerUserValidator=Blueprint('registerUserValidator',__name__)

database=connectToDb()

@registerUserValidator.route('/app/register')
@cross_origin()
def registerUser():
    collection=database.users
    result=collection.find({})
    for re in result:
        print(re)
    return "register Here"