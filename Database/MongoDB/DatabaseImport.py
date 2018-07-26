import pandas as pd
from pymongo import MongoClient
import json
import os

def mongoimport(folderPath,csv_path, db_name, coll_name, db_url, db_port):
    """ Imports a csv file at path csv_name to a mongo colection
    returns: count of the documents in the new collection
    """
    os.chdir(folderPath)
    client = MongoClient(db_url, db_port)
    db = client[db_name]
    coll = db[coll_name]
    data = pd.read_csv(csv_path)
    payload = json.loads(data.to_json(orient='records'))
    # coll.delete_many()
    coll.insert_many(payload)
    return coll.estimated_document_count()


rootPath = 'C:\Project\Data\Stitched'
os.chdir(rootPath)

folderNames = []
folderNames = os.listdir()

db_url = 'localhost'
db_name = 'EnergyData'
db_port = 27017


for file_ in folderNames:
    filePath = 'C:\Project\Data\Stitched' + '\\'+ file_ + '\\' + file_+ '.csv'
    folderPath = 'C:\Project\Data\Stitched' + '\\'+ file_
    coll_name = file_
    os.chdir(folderPath)
    mongoimport(folderPath,filePath,db_name,coll_name,db_url,db_port)