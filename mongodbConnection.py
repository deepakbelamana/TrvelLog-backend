from pymongo import MongoClient

def connectToDb():
    try:   
        cluster=MongoClient('mongodb+srv://travellog:travellog@travellog.t6ldjf8.mongodb.net/?retryWrites=true&w=majority')
        db=cluster.travellog
        return db
    except Exception as e :
        return 'error occured'