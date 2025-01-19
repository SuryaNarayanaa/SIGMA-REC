
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


6. **Run with Docker:**

    **Build the Docker image:**
    ```sh
    docker build -t sigma-rec .
    ```

    **Run the Docker container:**
    ```sh
    docker run -d -p 5000:5000 --name sigma-rec-container sigma-rec
    ```

7. **Run both Flask and MongoBD with Docker Compose:**
    ```sh
    docker-compose up -d
    ```


<!-- ## Testing

1. **Run unit tests:**
    ```sh
    pytest
    ``` -->
8. **Testing the modules**:

    Added `Unit Testing` to each modules and helper functions with the help of  `pytest` package 

    **To Test all the files under \test**
    ```sh
    pytest
    ```

    **To Test individual file under \test**
    ```sh
    pytest test\{testing_file_name.py}
    ```

    **To Test Files with verbose \test**
    ```sh
    pytest -v
    ```

9. **Continuous Integration:**

    A `ci.yml` file has been added for Continuous Integration (CI) using GitHub Actions. This file is located in the `.github/workflows` directory and is configured to run tests and checks on every push and pull request to the repository.




**Test API endpoints:**


 You can test the API endpoints using Postman by accessing  the following link:

 [Postman API Documentation](https://bit.ly/SIGMA-API)


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
