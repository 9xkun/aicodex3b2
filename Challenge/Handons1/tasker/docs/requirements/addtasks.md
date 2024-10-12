Create Task
Desc: As an user, I can create Task
Flow:
    User navigates to the "Add Task" form.
    User enters task details (title, description, priority, due date).
    User submits the form.
    System validates the input and saves the task to the database.
    System displays a confirmation message and updates the task list.

```mermaid
graph TD
    A[User navigates to the "Add Task" form] --> B[User enters task details (title, description, priority, due date)]
    B --> C[User submits the form]
    C --> D[System validates the input]
    D --> E{Is input valid?}
    E -- Yes --> F[System saves the task to the database]
    F --> G[System displays a confirmation message]
    G --> H[System updates the task list]
    E -- No --> I[System displays an error message]

Feature: Add Task
  Scenario: Successfully add a new task
    Given the user is on the "Add Task" form
    When the user enters valid task details (title, description, priority, due date)
    And the user submits the form
    Then the system should validate the input
    And the system should save the task to the database
    And the system should display a confirmation message
    And the system should update the task list with the new task

  Scenario: Fail to add a new task due to invalid input
    Given the user is on the "Add Task" form
    When the user enters invalid task details (e.g., empty title)
    And the user submits the form
    Then the system should validate the input
    And the system should display an error message
    And the task should not be saved to the database
    And the task list should not be updated

  Scenario: Fail to add a new task due to network error
    Given the user is on the "Add Task" form
    When the user enters valid task details (title, description, priority, due date)
    And the user submits the form
    And there is a network error
    Then the system should display a network error message
    And the task should not be saved to the database
    And the task list should not be updated    