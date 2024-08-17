import sys
import os

# Add the path to the 'flask' directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the entire db.py as database
import db as database
from dotenv import load_dotenv

def signin_controller(formData):
    # Load environment variables from the .env file
    load_dotenv()
    
    # Get the MongoDB URI from the environment variables
    mongo_uri = os.getenv('MONGO_URI')
    
    # Initialize the database connection
    db = database.databaseInit(mongo_uri)
    users = db.users
    
    # Extract email and username from the form data
    email = formData['email']
    uname = formData['uname']
    
    try:
        # Check if a user with the given email already exists
        checkExistingUser = users.find_one({'email': email})
        
        if checkExistingUser is None:
            # Check if a user with the given username already exists
            checkUsername = users.find_one({'uname': uname})
            
            if checkUsername is None:
                # Insert the new user into the database
                users.insert_one(formData)
                return 'inserted'
            
            # Return 'username' if the username already exists
            return 'username'
        
        # Return 'email' if the email already exists
        return 'email'
    
    except Exception as e:
        # Print any exceptions that occur and return 'error'
        print("An Exception Occurred, Read Docs:", e)
        return 'error'
