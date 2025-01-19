
## Setup Instructions

1. **Clone the repository:**
    ```sh
    git clone https://github.com/SuryaNarayanaa/SIGMA-REC.git
    cd SIGMA-REC    
    ```

2. **Create and activate a virtual environment:**
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**
    Create a `.env` file in the root directory and add your environment variables:
    ```
    PORT                       = port_number
    SECRET_KEY                 = flask_secret_key
    MONGO_INITDB_DATABASE      = database_name 
    MONGO_INITDB_ROOT_USERNAME = mongo_user_name
    MONGO_INITDB_ROOT_PASSWORD = mongo_user_password
    JWT_SECRET_KEY             = jwt_secret_key

5. **Run the application:**
    ```sh
    flask run
    ```

<!-- ## Testing

1. **Run unit tests:**
    ```sh
    pytest
    ``` -->

**Test API endpoints:**


 You can test the API endpoints using Postman by accessing  the following link:

 [Postman API Documentation](bit.ly/SIGMA-API)


## API Endpoints

Below is a quick reference table of the main endpoints. Some routes require a valid JWT token and/or admin privileges (`isadmin = true`). Adjust as necessary if your routes differ slightly.

| Endpoint                      | Access Level        | Description                                                        |
|-------------------------------|---------------------|--------------------------------------------------------------------|
| `POST /user/register`         | public              | Register a new user (name, email, password, isadmin).              |
| `POST /user/login`            | public              | Login with email + password, returns a JWT access token.           |
| `GET /user/users/<user_id>`   | Logged-in user (JWT)| Retrieve user data by ID (own or any, depending on logic).         |
| `POST /user/logout`           | Logged-in user (JWT)| Logout (revokes token server-side).                                |
| `GET /user/users`             | Admin user (JWT)    | Retrieve a list of all users in the system.                        |
| `PUT /user/users/<user_id>`   | Admin user (JWT)    | Update user’s data (username, email, password, isadmin).           |
| `DELETE /user/users/<user_id>`| Admin user (JWT)    | Delete a user by ID.                                               |

## JWT Authorization

Include a header:

```
Authorization: Bearer <ACCESS_TOKEN>
```
