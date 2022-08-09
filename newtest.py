import pymongo

client = pymongo.MongoClient("mongodb://lohith369:Mongo369@ac-qn6cw65-shard-00-00.onq988i.mongodb.net:27017,ac-qn6cw65-shard-00-01.onq988i.mongodb.net:27017,ac-qn6cw65-shard-00-02.onq988i.mongodb.net:27017/?ssl=true&replicaSet=atlas-vkjq5c-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test
print(db)

data = [
        {
            "item": "canvas",
            "qty": 100,
            "size": {"h": 28, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "journal",
            "qty": 25,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mat",
            "qty": 85,
            "size": {"h": 27.9, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mousepad",
            "qty": 25,
            "size": {"h": 19, "w": 22.85, "uom": "cm"},
            "status": "P",
        },
        {
            "item": "notebook",
            "qty": 50,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "P",
        },
        {
            "item": "paper",
            "qty": 100,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "D",
        },
        {
            "item": "planner",
            "qty": 75,
            "size": {"h": 22.85, "w": 30, "uom": "cm"},
            "status": "D",
        },
        {
            "item": "postcard",
            "qty": 45,
            "size": {"h": 10, "w": 15.25, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketchbook",
            "qty": 80,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketch pad",
            "qty": 95,
            "size": {"h": 22.85, "w": 30.5, "uom": "cm"},
            "status": "A",
        },
    ]

database = client["myinfo"]
collections = database["New Table"]
collections.insert_many(data)
#f = collections.find({'status': 'A'})                      # prints value where status is A
#f = collections.find({'status':{"$in":["A","P"]}})         # Prints data where status is either A or P
#f = collections.find({'status':{"$gt" : "C"}})             # Prints data greater than C
#f = collections.find({"qty" : {"$gte" : 50}})              # Prints data greater than equal to 40
#f = collections.find({'qty': 80})                          # Prints qty is 80
#f = collections.find({'item': 'sketchbook','qty' : {'$gte' : 80}})   #Prints 2 condition AND
#f = collections.find({'$or' : [{'item': 'mat'},{'qty': {'$gte' : 80}}]})    # OR condition
#collections.update_one({'item': 'canvas'}, {'$set':{'item': 'LOHITH'}})     # UPDATE commond
collections.delete_one({'item': 'LOHITH'})               #DELETE commond
f = collections.find({'item': 'LOHITH'})
for i in f:
    print(i)

