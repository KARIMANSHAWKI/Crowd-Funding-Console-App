from pymongo import MongoClient

uri = "mongodb://localhost:27017/"
client = MongoClient(uri)

crowdFundingDatabase = client.CrowdFundingDatabase
userCollection = crowdFundingDatabase.user


# Create user
def create_user(firstName, lastName, email, password, phoneNumber):
    newUserDocument = {
        'firstName': firstName,
        'lastName': lastName,
        'email': email,
        'password': password,
        'phoneNumber': phoneNumber
    }
    checkDocument = {
        'email': email,
    }
    if not userCollection.find_one(checkDocument):
        return userCollection.insert_one(newUserDocument).inserted_id
    else:
        return False


# Find One User - Login
def findOneUser( email, password):
    findOneUserDocument = {
        'email': email,
        'password': password
    }
    userData = userCollection.find(findOneUserDocument)
    userDocumentation = {}
    for property in userData:
        userDocumentation = property

    return userDocumentation
