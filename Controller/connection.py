import os
from os.path import join, dirname
from dotenv import load_dotenv

from pymongo import MongoClient

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

def connection():
	MONGODB_URI = os.environ.get("MONGODB_URI")
	DB_NAME =  "dbproject_akhir"
	client = MongoClient(MONGODB_URI)
	db = client[DB_NAME]
	return db
