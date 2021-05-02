from bson import ObjectId

# initial fields
from pymongo import MongoClient

uri = "mongodb://localhost:27017/"
client = MongoClient(uri)
crowdFundingDatabase = client.CrowdFundingDatabase
projectCollection = crowdFundingDatabase.project


def createProject(userId, title, details, totalTarget, startDate, endDate):
    newProjectDocument = {
        'userId': ObjectId(userId),
        'title': title,
        'details': details,
        'total': totalTarget,
        'startDate': startDate,
        'endDate': endDate
    }
    return projectCollection.insert_one(newProjectDocument).inserted_id


# View All Project

def findAllproject(userId):
    allProjectsDictionry = {}
    for project in projectCollection.find({'userId': userId}):
        projectDictionry = {
            'title': project['title'],
            'details': project['details'],
            'total': project['total'],
            'startDate': project['startDate'],
            'endDate': project['endDate']
        }
        allProjectsDictionry[projectDictionry['title']] = projectDictionry
    return allProjectsDictionry


def findOneProject(userId, title):
    return projectCollection.find_one({
        'userId': userId,
        'title': title
    })


def deleteOneProject(userID, projectTitle):
    return projectCollection.delete_one({
        'userId': ObjectId(userID),
        'title': projectTitle
    })

    # Delete All Project for One User


def deleteAllProject(userID):
    return projectCollection.delete({
        'userId': ObjectId(userID),
    })
