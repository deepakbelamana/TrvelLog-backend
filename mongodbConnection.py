from pymongo import MongoClient

def connectToDb():
    try:   
        cluster=MongoClient('mongodb://travellog:travellog@ac-9jri8uh-shard-00-00.t6ldjf8.mongodb.net:27017,ac-9jri8uh-shard-00-01.t6ldjf8.mongodb.net:27017,ac-9jri8uh-shard-00-02.t6ldjf8.mongodb.net:27017/?ssl=true&replicaSet=atlas-5h4dl2-shard-0&authSource=admin&retryWrites=true&w=majority')
        db=cluster.travellog
        return db
    except Exception as e :
        print(e)
        return 'error occured connecting database'