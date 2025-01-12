# Task Management API

This project is a RESTful API built with Django REST Framework (DRF) for managing tasks. It provides endpoints for creating, retrieving, updating, deleting, and completing tasks, as well as filtering and sorting options. This API is designed to be used by front-end applications or other services that need to interact with task data.

## Table of Contents

- [Project Description](#project-description)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
  - [Authentication](#authentication)
  - [Endpoints](#endpoints)
    - [Users](#users)
    - [Tasks](#tasks)
  - [Filtering and Sorting](#filtering-and-sorting)
- [Testing](#testing)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Project Description

This API aims to provide a robust and flexible solution for managing tasks. It allows users to create tasks with titles, descriptions, due dates, priorities, and statuses. The API also supports user authentication, ensuring that users can only access and manage their own tasks.

## Features

-   User authentication (using Token Authentication)
-   CRUD (Create, Read, Update, Delete) operations for tasks
-   Marking tasks as complete/incomplete
-   Filtering tasks by status
-   Sorting tasks by due date
-   Detailed error handling
-   Clear API documentation (using this README)

## Technologies Used

-   Python
-   Django
-   Django REST Framework (DRF)
-   SQLite (development) / PostgreSQL (production)
-   Git (version control)

## Installation & Setup Instructions

**Prerequisites:**

-   Python 3.8+
-   pip

**Steps:**

1.  Clone the repository:

    ```bash
    git clone [invalid URL removed]
    ```

2.  Navigate to the project directory:

    ```bash
    cd YOUR_REPO_NAME
    ```

3.  Create a virtual environment (recommended):

    ```bash
    python -m venv venv  # On Windows
    python3 -m venv venv # On Linux/macOS
    source venv/bin/activate # On Linux/macOS
    venv\Scripts\activate # On Windows
    ```

4.  Install the project dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5.  Apply database migrations:

    ```bash
    python manage.py migrate
    ```

6.  Create a superuser (for admin access):

    ```bash
    python manage.py createsuperuser
    ```

## Usage

### Authentication

This API uses Token Authentication. To access protected endpoints, you need to obtain a token by registering a user and then logging in.

1.  **Register a User (POST /api/users/):**

    ```json
    {
        "username": "testuser",
        "password": "TestPassword123!",
        "email": "test@example.com",
        "first_name": "Test",
        "last_name": "User"
    }
    ```

2.  **Retrieve a Token (POST /api/token/):**

    ```json
    {
        "username": "testuser",
        "password": "TestPassword123!"
    }
    ```

    The response will contain a token:

    ```json
    {
        "token": "YOUR_GENERATED_TOKEN"
    }
    ```

Include this token in the `Authorization` header of subsequent requests: `Authorization: Token YOUR_GENERATED_TOKEN`

### Endpoints

Base URL: `http://127.0.0.1:8000/api/` (for local development)

#### Users

-   **POST /api/users/**: Create a new user (registration).

#### Tasks

-   **GET /api/tasks/**: List all tasks for the authenticated user.
-   **POST /api/tasks/**: Create a new task.
-   **GET /api/tasks/{id}/**: Retrieve a specific task by ID.
-   **PATCH /api/tasks/{id}/**: Update a specific task.
-   **DELETE /api/tasks/{id}/**: Delete a specific task.
-   **PATCH /api/tasks/{id}/complete/**: Mark a task as complete/incomplete.

### Filtering and Sorting

-   **Filtering by Status:** `GET /api/tasks/?status=pending` (or `completed`, `in_progress`, etc.)
-   **Sorting by Due Date:** `GET /api/tasks/?ordering=due_date` (ascending) or `GET /api/tasks/?ordering=-due_date` (descending)

## Testing

To run the tests:

```bash
python manage.py test
