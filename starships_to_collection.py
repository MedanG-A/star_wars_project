import pymongo
import json
import replace_URLs_with_ObjectID as Rp
from bson import json_util

client = pymongo.MongoClient()
db = client['starwars']


class StarshipsToCollection(Rp.ReplacePilotUrls):
    def __init__(self):
        super().__init__()

    @staticmethod
    def starshipstocoll():
        # retrieving finalised data from "replace urls with object ID" function
        if 'starships' not in db.list_collection_names():
            # retrieving finalised data from "replace urls with object ID" function
            x = Rp.ReplacePilotUrls().replace_urls_with_objectids()
            # dumping into json file and then loading it up, then creating a starships collection
            # and bulk inserting the data into it
            json_path = json.loads(json_util.dumps(x))
            collection = db['starships']
            collection.insert_many(json_path)
            print("Execution complete, check MongoDB")
        else:
            print("This collection already exists, ending the process")


# running the function to check it works, but this can just be put into main
# StarshipsToCollection().starshipstocoll()
