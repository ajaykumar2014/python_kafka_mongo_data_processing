import certifi
from kafka import KafkaConsumer
from time import sleep
from json import loads
import pandas as pd
from pymongo import MongoClient


consumer = KafkaConsumer(
    'python-file-processing-panda',
    bootstrap_servers=[':9092'], #add your IP here
    value_deserializer=lambda x: loads(x.decode('utf-8')))

MONGO_DB_CONNECTION = "mongodb+srv://ajay:ajay12345@cluster0.vx6ddia.mongodb.net/"

client = MongoClient(MONGO_DB_CONNECTION,tlsCAFile=certifi.where())
"""
fixed - pymongo.errors.ServerSelectionTimeoutError: ac-nwtldka-shard-00-01.vx6ddia.mongodb.net:27017: [SSL: CERTIFICATE_VERIFY_FAILED] then
1.)  $ python3 -m pip install certifi  
2.) check your IP address and whitelist the ip address
"""
employee = {
    "id": "102",
    "name": "Peter",
    "profession": "Software Engineer"
}
db = client["stock_matrix_db"]
stockCollection = db.stock_matrix
# for val in collection_name.find():
#     print(val)

# collection_name.insert_one(employee)
# for val in collection_name.find():
#     print(val)

for msg in consumer:
    print( msg.topic,msg.key, "=>", msg.value)
    stockCollection.insert_one(msg.value)
    sleep(.5)
