from flask import Blueprint
from flask_cors import cross_origin
from mongodbConnection import connectToDb
loginValidator=Blueprint('loginValidator',__name__)

database=connectToDb()

@loginValidator.route('/app/login')
@cross_origin()
def loginUser():
    return 'Login Here'
