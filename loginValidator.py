import json
from flask import Blueprint, jsonify,request
from flask_cors import cross_origin
from mongodbConnection import connectToDb
loginValidator=Blueprint('loginValidator',__name__)

database=connectToDb()

@loginValidator.route('/app/login',methods=['post'])
@cross_origin()
def loginUser():
    form_data=request.data
    collection=database.users
    form_data=form_data.decode()
    form_data=json.loads(form_data)
    userExists=True if collection.count_documents({'userEmail':form_data['userEmail']})!=0 else False
    if userExists:
        user_data=collection.find_one({'userEmail':form_data['userEmail']})
        if(user_data['userPassword']== form_data['userPassword']):
            return jsonify(result=True,register=True,password=True)
        else:
            return jsonify(result=True,register=True,password=False)
    else:
        return jsonify(register=False,result=False,password=False)
