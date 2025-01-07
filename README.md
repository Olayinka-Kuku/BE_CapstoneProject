# Task Management API

A Django-based API for managing tasks, projects, and comments. This project is part of the Backend Capstone Project.

## Setup Instructions

1. Clone the repository:
   bash
   git clone https://github.com/yourusername/TaskManagementAPI.git


## Prerequisites
Before running this project, ensure you have the following installed:

Python 3.10 or higher
pip (Python package manager)
Git
Virtual environment tool (e.g., venv)

## Setup Instructions
Follow these steps to set up and run the project:

1. Clone the Repository
bash
git clone https://github.com/Olayinka-Kuku/BE_CapstoneProject.git
cd BE_CapstoneProject

2. Set Up the Virtual Environment
bash
python -m venv myenv
source myenv/Scripts/activate   # For Windows (Git Bash or VSCode Terminal)

3. Install Dependencies
bash
pip install -r requirements.txt





4. Create a .env File
Add your environment variables (e.g., secret key, database configuration) to a .env file. Example:

plaintext
Copy code
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
5. Run Migrations
bash
Copy code
python manage.py makemigrations
python manage.py migrate
6. Run the Development Server
bash
Copy code
python manage.py runserver
Visit http://127.0.0.1:8000 in your browser.

Usage
Use an API testing tool like Postman or cURL to test API endpoints.
Authentication is required for most operations (login, register, etc.).
API Endpoints
Endpoint	Method	Description
/api/register/	POST	Register a new user
/api/login/	POST	Login and obtain a token
/api/projects/	GET	List all projects
/api/projects/	POST	Create a new project
/api/projects/{id}/tasks/	GET	List all tasks for a project
/api/tasks/{id}/comments/	GET	List all comments for a task
Built With
Django: Web framework
Django REST Framework (DRF): API development
SQLite: Default database for development
Python: Programming language
 Features

- User authentication and authorization.
- Create and manage projects.
- Add tasks to projects with due dates and statuses (e.g., Pending, Completed).
- Add comments to tasks.
- RESTful API built with Django and Django REST Framework.

---

## Project Structure

BE_CapstoneProject/
│
├── task_management_api/   # Main Django project directory
│   ├── settings.py        # Project settings
│   ├── urls.py            # Main URL configurations
│   ├── wsgi.py            # WSGI configuration for deployment
│
├── myenv/                 # Virtual environment 
├── requirements.txt       # Python dependencies
├── manage.py              # Django management script
├── README.md              # Project documentation
├── .gitignore             # Git ignore rules
└── ...
