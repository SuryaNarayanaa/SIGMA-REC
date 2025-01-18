from werkzeug.security import check_password_hash, generate_password_hash
from flask import current_app ,jsonify
from bson import ObjectId

def validate_user(data):
    user_data = [ 'username', 'email', 'password' , ]
    fields_not_present = [field for field in user_data if field not in data]
    if fields_not_present:
        return jsonify({"message": f"{fields_not_present} not present"}), 400
    return True

def validate_password(password_hash, password):
    try:
        return check_password_hash(password_hash, password)
    except Exception as e:
        print(f"Error: {e}")
        return False
    
def get_all_users():
    try:
        collection = current_app.db['users']
        return collection.find({}, {'password': 0})
    except Exception as e:
        print(f"Error: {e}")
        return None

def find_by_username(username):
    try:
        collection = current_app.db['users']
        return collection.find_one({'username': username})
    except Exception as e:
        print(f"Error: {e}")
        return None

def get_user_by_email(email):
    try:
        collection = current_app.db['users']
        return collection.find_one({'email': email})
    except Exception as e:
        print(f"Error: {e}")
        return None

def find_by_id(_id):
    try:
        collection = current_app.db['users']
        return collection.find_one({'_id': ObjectId(_id)})
    except Exception as e:
        print(f"Error: {e}")
        return None

def get_user_id(username):
    try:
        user = find_by_username(username)
        return user['_id'] if user else None
    except Exception as e:
        print(f"Error: {e}")
        return None

def update_username(email, new_username):
    try:
        collection = current_app.db['users']
        collection.update_one({'email': email}, {'$set': {'username': new_username}})
    except Exception as e:
        print(f"Error: {e}")

def update_email(email, new_email):
    try:
        collection = current_app.db['users']
        collection.update_one({'email': email}, {'$set': {'email': new_email}})
    except Exception as e:
        print(f"Error: {e}")

def update_password(email, new_password):
    try:
        collection = current_app.db['users']
        collection.update_one({'email': email}, {'$set': {'password': generate_password_hash(new_password)}})
    except Exception as e:
        print(f"Error: {e}")

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
        print(f"Update result: {result.modified_count} document(s) updated")
    except Exception as e:
        print(f"Error: {e}")

def delete_user_by_id(id):
    try:
        object_id = ObjectId(id)
        collection = current_app.db['users']
        result = collection.delete_one({'_id': object_id})
        return result.deleted_count
    except Exception as e:
        print(f"Error: {e}")
