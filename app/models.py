from flask import current_app
import pymongo
from werkzeug.security import generate_password_hash
import logging 
import coloredlogs
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
coloredlogs.install(level='INFO', logger=logger, fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class User:

    def __init__(self, username, email, password, isadmin=False):
        if not username or not email or not password:
            raise ValueError("Username, email, and password are required fields")
        
        self.collection = current_app.db['users']
        self.collection.create_index('username', unique=True)
        self.collection.create_index('email', unique=True)
        self.username = username
        self.password = password
        self.email = email
        self.isadmin = isadmin

    def save(self):
        try:
            collection = current_app.db['users']
            collection.insert_one({
                'username': self.username,
                'email': self.email,
                'password': generate_password_hash(self.password),
                'isadmin': self.isadmin
            })
            logger.info(f"User {self.username} saved successfully.")
        except pymongo.errors.DuplicateKeyError as e:
            logger.error(f"Duplicate key error: {e}")
        except Exception as e:
            logger.error(f"An error occurred: {e}")

        
