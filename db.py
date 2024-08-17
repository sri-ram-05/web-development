from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Get the MongoDB URI from environment variables
mongo_uri = os.getenv("MONGO_URI")

def databaseInit(mongo_uri):
    """
    Initialize the MongoDB database connection.
    
    Args:
        mongo_uri (str): The MongoDB URI for connecting to the database.
        
    Returns:
        db: The database connection object.
    """
    # Create a MongoClient to connect to the MongoDB instance
    client = MongoClient(mongo_uri)
    print(client)  # Print the client object to verify the connection (can be removed in production)
    
    # You can access the database using either attribute or dictionary style.
    # Attribute style:
    # db = client.project_dbase  # Uncomment this line if your database name is 'project_dbase'
    
    # Dictionary style:
    # db = client["project-dbase"]  # Uncomment this line if your database name is 'project-dbase'
    
    # Here we use attribute style to access the 'project' database
    db = client.project
    
    # Return the database connection object
    return db

# Notes:
# - Ensure that the .env file contains the MONGO_URI variable with the correct MongoDB connection string.
# - The database name used here is 'project'. If your database name is different, adjust the code accordingly.
# - The print statement is useful for debugging purposes to ensure the connection is successful.
# - MongoClient can be configured with additional parameters for more control over the connection (e.g., authentication, timeouts).
