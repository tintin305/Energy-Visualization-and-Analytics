from pymongo import MongoClient
import pymongo
import sys
import pandas as pd
import json
import os

def importData(path):
    mongoClient = pymongo.MongoClient('localhost', 27017)
    mongoDatabase = mongoClient['testdatabase']
    collectionName = 'projects'
    databaseCollectionName = mongoDatabase[collectionName]
    cdir = os.path.dirname(__file__)
    fileRes = os.path.join(cdir, filepath)

    data = pd.read_csv(fileRes)
    dataJSON = json.loads(data.to_json(orient='records'))
    databaseCollectionName.remove()
    databaseCollectionName.insert(dataJSON)

if __name__ == "__main__":
    rootPath = 'C:\Project\Data\Stitched'
    os.chdir(rootPath)

    folderNames = []
    folderNames = os.listdir()

    for file_ in folderNames:
        filepath = 'C:/Project/Data/Stitched/' + file_
        importData(filepath)

# MONGODB_HOST = 'localhost'
# MONGODB_PORT = 27017
# DBS_NAME = 'testdatabase'
# COLLECTION_NAME = 'projects'

# fields = {'First Field':True, 'Second Field': True}

# connection =   MongoClient(MONGODB_HOST, MONGODB_PORT)
# collection = connection[DBS_NAME][COLLECTION_NAME]
# projects = collection.find(projection=fields)

# for project in projects:
#     print(project)