from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter (object):
    """ CRUD operations for Animal collection in MongoDB """
    
    def __init__(self, user, passwrd):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31028
        DB = 'AAC'
        COL = 'animals'
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (user, passwrd, HOST, PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
    
    # Creates new animal
    def create(self, data):
#         If data is not empty then an animal can be added to database
        if data:
            insert = self.database.animals.insert(data)  # data should be dictionary
            if insert != 0:
                return True
            else:
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    # Searches for animal based on criteria
    def read(self, criteria=None):
        # If criteria is not none then search by query
        if criteria is not None:
            data = self.database.animals.find(criteria) # data should be dictionary
            return data
        # Else get all animals
        else:
            data = self.database.animals.find({})
    
    # Updates animaldata
    def update(self, criteria, new_data):
        # if criteria is not empty look for animal
        if criteria is not None:
            # If animal is found then update animal data
            if(self.database.animals.count_documents(criteria, limit = 1) > 0):
                update = self.database.animals.update_many(criteria, {"$set": new_data})  # data should be dictionary
                result = update.raw_result 
            # Else then animal is not in database
            else:
                result = "No Animals Found"
            return result
        else:
            raise Exception("Nothing to Update, because data parameter is empty")

    # Deletes animal
    def delete(self, criteria):
        # If criteria is not empty
        if criteria is not None:
            # If animal is found then delete animal
            if(self.database.animals.count_documents(criteria, limit = 1) > 0):
                delete = self.database.animals.delete_many(criteria) # data should be dictionary
                result = delete.raw_result
            # Else then animal is not in database
            else:
                result = "No Animals Found" 
            return result
        else:
            raise Exception("Nothing to read, because data parameter is empty")
