# Security Implemented

## 1. **Hashed Passwords**

- **Implementation**: Passwords are hashed using `werkzeug` to ensure they are stored securely.

- **Purpose**: Prevents plaintext password storage and mitigates the risk of sensitive user information being exposed in case of a data breach.


## 2. **JWT Token Revocation**

- **Implementation**: A blocklist mechanism is in place to handle JWT token revocation. When a user logs out, the token’s unique ID (`jti`) is added to the blocklist.

- **Purpose**: Ensures that compromised or expired tokens cannot be reused maliciously.

### Example Code:
```python
from flask_jwt_extended import JWTManager

jwt = JWTManager(app)

@jwt.token_in_blocklist_loader
def check_if_token_in_blocklist(jwt_header, jwt_payload):
    jti = jwt_payload["jti"]
    return jti in BLOCKLIST
```

## 3. **Rate Limiting**

- **Implementation**: The `Flask-Limiter` library is used to restrict API usage. Default limits are set to:
  - 200 requests per day
  - 20 requests per hour
  
- **Purpose**: Prevents abuse of the application through denial-of-service (DoS) attacks or brute force attempts.

### Example Code:
```python
limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["200 per day", "20 per hour"]
)
```

## 4. **Environment Variables**

- **Implementation**: Sensitive credentials like `MONGO_URI` and `JWT_SECRET_KEY` are stored in a `.env` file and loaded into the application.

- **Purpose**: Prevents sensitive information from being hardcoded into the application, reducing the risk of exposure.

## 5. **Secure HTTP Headers**

- **Implementation**: The `Flask-Talisman` library is used to enforce security headers, including:
  - HTTP Strict Transport Security (HSTS)
  - Frame Options set to `DENY`
  - Referrer Policy set to `no-referrer`
  
- **Purpose**: Protects against common vulnerabilities like clickjacking, man-in-the-middle attacks, and information leakage.
### Example Code:
```python
Talisman(app, strict_transport_security=True, frame_options="DENY", referrer_policy="no-referrer")
```

## 6. **CSRF Protection**

- **Implementation**: The `Flask-WTF` library provides CSRF protection by adding a CSRF token to forms.

- **Purpose**: Prevents cross-site request forgery attacks by ensuring that form submissions are from trusted sources.
### Example Code:
```python
csrf = CSRFProtect(app)
```
## 7. **Basic Input Validation**

- **Implementation**: Fields are validated for presence and correctness using the `pydantic` library for comprehensive validation.

- **Purpose**: Protects against injection attacks by validating and sanitizing user inputs..

### Example Code:
```python
class UserModel(BaseModel):
    username: str
    email: EmailStr
```

## 8. **Error Handling**

- **Implementation**: Generic error messages are returned to users to prevent stack traces or sensitive information from being leaked.

- **Purpose**: Reduces the information available to attackers during reconnaissance.

### Example Code:
```python
@app.errorhandler(Exception)
def handle_exception(e):
    return {"message": "An error occurred."}, 500
```

## 9. **Docker Isolation**

- **Implementation**: The application’s components (e.g., Flask and MongoDB) run in isolated Docker containers.

- **Purpose**: Ensures that each component operates in a self-contained environment, limiting the blast radius of potential breaches.
### Dockerfile :   [Dockerfile](./Dockerfile)


