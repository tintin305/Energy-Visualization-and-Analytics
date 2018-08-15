from pymongo import MongoClient

MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
DBS_NAME = 'EnergyData'
COLLECTION_NAME = 'WITS 13 Jubilee Road_kVarh'

FIELDS = {'ValueTimestamp': True, 'WITS 13 Jubilee Road_kVarh': True,  '_id': False}

connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
collection = connection[DBS_NAME][COLLECTION_NAME]
projects = collection.find(projection=FIELDS)

for project in projects:
    print (project)

# client = MongoClient()

# db = client.EnergyData
# my_collection = "WITS 13 Jubilee Road_kVarh"
# collection = db.my_collection

# print(db.collection_names)

# cursor = collection.find({"activityArray": {"$elemMatch": {"sport":0 }}},{"activityArray.sport" : 1, "activityArray.id":1, "endo" : 1}) 

# for result_object in cursor[0:1]:
#     print result_object["endo"])
#     for activity in result_object["activityArray"]:
#         print activity["sport"]