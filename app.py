from mongodbConnection import connectToDb
from flask import Flask,jsonify
from flask_cors import CORS, cross_origin
from registerUserValidator import registerUserValidator


app=Flask(__name__)
CORS(app)


app.register_blueprint(registerUserValidator,url_prefix='')


cors = CORS(app, resources={
    r"/*":
    {
        "origins": "*"
    }
})

app.config['CORS_HEADERS'] = 'Content-Type'


if __name__ == "__main__":
    app.run(debug=True)