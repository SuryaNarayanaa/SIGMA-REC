import logging
from werkzeug.security import check_password_hash, generate_password_hash
from flask import current_app, jsonify
from bson import ObjectId
import coloredlogs

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
coloredlogs.install(level='INFO', logger=logger, fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def validate_user(data):
    user_data = ['username', 'email', 'password']
    fields_not_present = [field for field in user_data if field not in data]
    if fields_not_present:
        logger.warning(f"Fields not present: {fields_not_present}")
        return jsonify({"message": f"{fields_not_present} not present"}), 400
    return True

def validate_password(password_hash, password):
    try:
        return check_password_hash(password_hash, password)
    except Exception as e:
        logger.error(f"Error validating password: {e}")
        return False

def get_all_users():
    try:
        collection = current_app.db['users']
        users = collection.find({}, {'password': 0})
        logger.info("Fetched all users")
        return users
    except Exception as e:
        logger.error(f"Error fetching all users: {e}")
        return None

def find_by_username(username):
    try:
        collection = current_app.db['users']
        user = collection.find_one({'username': username})
        logger.info(f"User found by username: {username}")
        return user
    except Exception as e:
        logger.error(f"Error finding user by username: {e}")
        return None

def get_user_by_email(email):
    try:
        collection = current_app.db['users']
        user = collection.find_one({'email': email})
        logger.info(f"User found by email: {email}")
        return user
    except Exception as e:
        logger.error(f"Error finding user by email: {e}")
        return None

def find_by_id(_id):
    try:
        collection = current_app.db['users']
        user = collection.find_one({'_id': ObjectId(_id)})
        logger.info(f"User found by ID: {_id}")
        return user
    except Exception as e:
        logger.error(f"Error finding user by ID: {e}")
        return None

def get_user_id(username):
    try:
        user = find_by_username(username)
        user_id = user['_id'] if user else None
        logger.info(f"User ID for username {username}: {user_id}")
        return user_id
    except Exception as e:
        logger.error(f"Error getting user ID: {e}")
        return None

def update_username(email, new_username):
    try:
        collection = current_app.db['users']
        result = collection.update_one({'email': email}, {'$set': {'username': new_username}})
        logger.info(f"Updated username for email {email}: {result.modified_count} document(s) updated")
    except Exception as e:
        logger.error(f"Error updating username: {e}")

def update_email(email, new_email):
    try:
        collection = current_app.db['users']
        result = collection.update_one({'email': email}, {'$set': {'email': new_email}})
        logger.info(f"Updated email for {email}: {result.modified_count} document(s) updated")
    except Exception as e:
        logger.error(f"Error updating email: {e}")

def update_password(email, new_password):
    try:
        collection = current_app.db['users']
        result = collection.update_one({'email': email}, {'$set': {'password': generate_password_hash(new_password)}})
        logger.info(f"Updated password for email {email}: {result.modified_count} document(s) updated")
    except Exception as e:
        logger.error(f"Error updating password: {e}")

def update_record(id, email, username, password, isadmin):
    try:
        collection = current_app.db['users']
        result = collection.update_one(
            {'_id': ObjectId(id)}, 
            {'$set': {
                'email': email, 
                'username': username, 
                'password': generate_password_hash(password), 
                'isadmin': isadmin
            }}
        )
        logger.info(f"Updated record for ID {id}: {result.modified_count} document(s) updated")
    except Exception as e:
        logger.error(f"Error updating record: {e}")

def delete_user_by_id(id):
    try:
        object_id = ObjectId(id)
        collection = current_app.db['users']
        result = collection.delete_one({'_id': object_id})
        logger.info(f"Deleted user by ID {id}: {result.deleted_count} document(s) deleted")
        return result.deleted_count
    except Exception as e:
        logger.error(f"Error deleting user by ID: {e}")
        return None
        # Configure colored logging
        