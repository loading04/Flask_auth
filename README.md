

# Flask User Authentication

This is a Flask application that demonstrates user authentication using Flask, Flask-Login, and SQLAlchemy.
Simple flask authentication using werkzeug
## Installation

1. Clone the repository:

```bash
git clone https://github.com/loading04/Flask_auth.git
```

2.Navigate to the project directory:

```
cd Flask_auth
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:

```
python app.py
```

## Usage
Once the application is running, you can access it by navigating to http://localhost:5000 in your web browser. <br>

## Routes
/ - Home page <br>
/register - User registration page <br>
/login - User login page <br>
/secrets - Protected route that displays user information <br>
/logout - Logout route <br>
/download - Route to download a file (cheat_sheet.pdf) <br>

## Configuration
The application can be configured by modifying the following variables in the code: <br>

SECRET_KEY - Secret key used for session encryption <br>
SQLALCHEMY_DATABASE_URI - URI for the SQLite database file <br>
SQLALCHEMY_TRACK_MODIFICATIONS - Tracks modifications to database models. Set to False to improve performance <br>
## Database
The application uses a SQLite database to store user information. The database schema is defined by the User class in the code. The table will be created automatically the first time the application is run. You can uncomment the db.create_all() line to create the table manually. <br>

## Dependencies
The application relies on the following dependencies: <br>

Flask <br>
Flask-Login <br>
SQLAlchemy <br>
Werkzeug <br>
