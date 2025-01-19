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

## Security

This project follows a number of secure coding practices:

- **Hashed Passwords:** Uses bcrypt/werkzeug for password hashing.

- **JWT Token Revocation:** Logout adds the token’s unique ID to a blocklist.

- **Environment Variables:** Sensitive credentials (like `MONGO_URI`, `JWT_SECRET_KEY`) can be placed in a `.env` file.

- **Basic Input Validation:** Checks for required fields; can be extended with libraries like marshmallow.

- **Error Handling:** Generic errors are returned to avoid leaking stack traces.

- **Docker Isolation:** Flask and MongoDB run in separate containers.