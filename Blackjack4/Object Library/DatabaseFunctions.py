import pymongo
import dns
import pprint


if __name__ == '__main__':
    test = {"test":1}
    client = pymongo.MongoClient(
        "mongodb+srv://root:chicago1%21@blackjackanalytics-idjco.mongodb.net/Results?retryWrites=true&w=majority&authSource=admin")

    db = client.Results
    coll = db.TestColResults

    #insert 1 docc
    coll.insert_one()
    
    #clears collection
    #coll.delete_many({})


