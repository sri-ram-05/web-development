import pymongo

# Establish a connection to the MongoDB server running on localhost at the default port 27017
myclient = pymongo.MongoClient('mongodb://localhost:27017/')

# Create a new database named 'mydatabase' (if it doesn't already exist)
mydb = myclient['mydatabase']

# Create a new collection named 'customers' within 'mydatabase' (if it doesn't already exist)
mycol = mydb["customers"]

# Create a dictionary to represent the document you want to insert
mydict = { "name": "John", "address": "Highway 37" }

# Insert the document into the 'customers' collection
x = mycol.insert_one(mydict)

# Print the result of the insert operation to verify that the document was inserted successfully
print(x)

# Notes:
# - The 'insert_one' method returns an InsertOneResult object, which contains information about the insertion.
# - 'x' will have a property 'inserted_id' which gives the unique ID of the inserted document.
# - Ensure that the MongoDB server is running and accessible at 'localhost:27017'.
# - This example assumes that no authentication is required to connect to the MongoDB server. If authentication is needed, include the credentials in the connection string.
