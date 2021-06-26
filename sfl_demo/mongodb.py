from pymongo import MongoClient

cluster = MongoClient('mongodb+srv://yipeng:78641@demo.fby7a.mongodb.net/SFL_demo?retryWrites=true&w=majority')
db = cluster['SFL_demo']
collection = db['img_predict']

def insert(doc):
    collection.insert_one(doc)

def query(args):
    return collection.find(args)
    
