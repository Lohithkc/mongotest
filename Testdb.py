import pymongo

client = pymongo.MongoClient("mongodb://lohith369:Mongo369@ac-qn6cw65-shard-00-00.onq988i.mongodb.net:27017,ac-qn6cw65-shard-00-01.onq988i.mongodb.net:27017,ac-qn6cw65-shard-00-02.onq988i.mongodb.net:27017/?ssl=true&replicaSet=atlas-vkjq5c-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "Name" : "Lohith",
    "Age" : 30,
    "Email" : "lohith@gmail.com",
    "Address" : "bangalore"
}

d = {
    "Name" : "Lohith",
    "Age" : 30,
    "Email" : "lohith@gmail.com",
    "Address" : "bangalore"
}

d = {
    "Name" : "Lohith",
    "Age" : 30,
    "Email" : "lohith@gmail.com",
    "Address" : "bangalore"
}
db1 = client['mongggtest']
collection = db1['test']
collection.insert_one(d)