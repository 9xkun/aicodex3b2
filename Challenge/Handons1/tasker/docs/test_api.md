# API Test Cases for Creating Users

| Test Case ID | Description | Input | Expected Output | Actual Output | Status |
|--------------|-------------|-------|-----------------|---------------|--------|
| TC001 | Validate email format | Invalid email (e.g., "user@domain") | Error message: "Invalid email format" | | |
| TC002 | Validate password length | Password less than 8 characters | Error message: "Password must be at least 8 characters long" | | |
| TC003 | Validate name length | Name less than 3 characters | Error message: "Name must be at least 3 characters long" | | |
| TC004 | Check unique email | Email already exists in the database | Error message: "Email already exists" | | |
| TC005 | Check unique password | Password already exists in the database | Error message: "Password already exists" | | |
