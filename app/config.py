from dotenv import load_dotenv
import os
load_dotenv()

class Config:
    PORT = int(os.getenv('PORT', 5000))
    MONGO_INITDB_ROOT_USERNAME = os.getenv('MONGO_INITDB_ROOT_USERNAME', 'sampleUser')
    MONGO_INITDB_ROOT_PASSWORD = os.getenv('MONGO_INITDB_ROOT_PASSWORD', 'samplePass123')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'secret')