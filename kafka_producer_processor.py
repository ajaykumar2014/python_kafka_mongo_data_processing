from kafka import KafkaProducer, KafkaConsumer
from time import sleep
from json import dumps
import pandas as pd

kafkaProducer = KafkaProducer(bootstrap_servers=['127.0.0.1:9092'], #change ip here
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))
#,value_serializer = lambda x :dumps(x).encodes('utf-8'))


df = pd.read_csv("kafka_panda_data_processing/indexProcessed.csv")
while True:
    stock_records = df.sample(1).to_dict(orient="records")[0]
    kafkaProducer.send(topic='python-file-processing-panda',value=stock_records)
    sleep(.5)
kafkaProducer.flush()



