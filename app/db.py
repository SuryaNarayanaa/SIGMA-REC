from pymongo import MongoClient
import os
from dotenv import load_dotenv
load_dotenv()


def init_db():

    username = os.getenv('MONGO_INITDB_ROOT_USERNAME', 'sampleUser')
    password = os.getenv('MONGO_INITDB_ROOT_PASSWORD', 'samplePass123')
    client = MongoClient(f'mongodb://{username}:{password}@localhost:27017/')
    db = client[os.environ.get('MONGO_INITDB_DATABASE', 'USerDB')]
    
    return db