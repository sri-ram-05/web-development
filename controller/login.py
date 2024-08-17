import sys
import os

# Add the path to the 'flask' directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the entire db.py as database
import db as database
from dotenv import load_dotenv

def login_controller(formData):
    # Load environment variables from the .env file
    load_dotenv()
    
    # Get the MongoDB URI from the environment variables
    mongo_uri = os.getenv('MONGO_URI')
    
    # Initialize the database connection
    db = database.databaseInit(mongo_uri)
    users = db.users
    
    # Extract username and password from the form data
    username = formData['username']
    password = formData['password']
    
    try:
        # Check if a user with the given username exists
        data = users.find_one({"uname": username})
        
        if data is not None:
            # Check if the provided password matches the stored password
            if data["password"] != password:
                return "password"  # Return 'password' if the password is incorrect
            return "Loggedin"  # Return 'Loggedin' if the credentials are correct
        
        # Return 'User' if the user does not exist
        return "User"
    
    except Exception as e:
        # Print any exceptions that occur and return 'False'
        print("ERROR Read doc:", e)
        return False
