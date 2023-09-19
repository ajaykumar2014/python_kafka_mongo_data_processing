
## start kafka server
./bin/kafka-server-start.sh config/server.properties

## start kafka zooker server
./bin/zookeeper-server-start.sh -daemon ./config/zookeeper.properties

## start kafka producer & consumer

./bin/kafka-topics.sh -zookeeper localhost:2181 -topic python-file-processing-panda --create --partitions 1 --replication-factor 1

./bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 -topic python-file-processing-panda

./bin/kafka-console-producer.sh --broker-list 127.0.0.1:9092 --topic python-file-processing-panda

## kafka console producer
./bin/kafka-console-producer.sh --broker-list 127.0.0.1:9092 --topic python-file-processing-panda
