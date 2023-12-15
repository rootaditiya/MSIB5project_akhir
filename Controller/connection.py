from pymongo import MongoClient

MONGODB_CONNECTION_STRING = 'mongodb://ditiya:sparta@ac-rcamlhi-shard-00-00.rc6xlci.mongodb.net:27017,ac-rcamlhi-shard-00-01.rc6xlci.mongodb.net:27017,ac-rcamlhi-shard-00-02.rc6xlci.mongodb.net:27017/?ssl=true&replicaSet=atlas-7keaa1-shard-0&authSource=admin&retryWrites=true&w=majority'

def connection():
	client = MongoClient(MONGODB_CONNECTION_STRING)
	db = client.dbproject_akhir
	return db
