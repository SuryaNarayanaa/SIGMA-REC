from flask import current_app
import pymongo
from werkzeug.security import generate_password_hash, check_password_hash


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
        except pymongo.errors.DuplicateKeyError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error: {e}")

        
