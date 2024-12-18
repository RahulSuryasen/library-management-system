# Library Management System

This is a simple Flask-based library management system that allows users to perform CRUD operations for books and members, including search functionality and pagination. The system also includes token-based authentication for secure access.

## Project Structure

/digital-library /static /css styles.css /templates index.html books.html app.py models.py auth.py library.db requirements.txt README.md /tests test_auth.py test_books.py test_members.py


### How to Run the Project

#### Prerequisites:
- Python 3.x
- Flask
- SQLite (for database)

#### Steps to run the project:
1. **Clone the Repository**:
   Clone the repository to your local machine by clicking the "Code" button in GitHub, then copying the URL. In your terminal, use the command:
   ```bash
   git clone https://github.com/yourusername/library-management-system.git
Install Dependencies: Make sure you have all the necessary Python packages installed. In the project directory, run:


pip install -r requirements.txt
Setup Database: The application uses an SQLite database. The library.db file is already included in the project, but you can recreate it by running the following commands in Python:


from models import db
db.create_all()
Run the Application: To start the Flask application, run the following command:


python app.py
The app will be running at http://127.0.0.1:5000.

Access the Application: Open your browser and navigate to http://127.0.0.1:5000.

Design Choices
Flask Framework: Chosen for its simplicity and flexibility in handling routing, templates, and databases.
SQLite: Used as a lightweight database for storing book and member information.
Jinja2 Templating: Used for rendering dynamic HTML templates on the client side.
Token-based Authentication: Implemented using simple JWT (JSON Web Tokens) to ensure secure access for CRUD operations.
Responsive UI: HTML and CSS are used to create a simple, user-friendly interface. The design is mobile-friendly.
Assumptions and Limitations


Assumptions:

Users are familiar with basic CRUD operations.
The system assumes that the user is logged in to perform operations like adding or modifying books or members.


Limitations:

The application is not intended for large-scale production use, as it uses SQLite, which is suitable for small to medium-sized databases.
There is no advanced authentication system. It uses a simple token-based approach which is not suitable for large-scale, enterprise-level applications.
The front-end UI is very basic and lacks advanced features like filtering, sorting, or advanced search options.
Future Improvements
Integrate more robust authentication methods (OAuth, Google Sign-In).
Add features like sorting and advanced search for books and members.
Use a more scalable database like PostgreSQL or MySQL for production environments.



