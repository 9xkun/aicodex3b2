# UserService

Service class for managing user-related operations.

## Methods

### `create_user(name, password, email, phone)`

Creates a new user with the provided details.

**Args:**
- `name` (str): The name of the user.
- `password` (str): The password for the user.
- `email` (str): The email address of the user.
- `phone` (str): The phone number of the user.

**Returns:**
- `User`: The newly created user object.

**Example usage:**
```python
user_service = UserService()
new_user = user_service.create_user("John Doe", "password123", "john.doe@example.com", "123-456-7890")
new_user = user_service.create_user("Jane", None, "hoang@mail.com", None)
print(new_user)