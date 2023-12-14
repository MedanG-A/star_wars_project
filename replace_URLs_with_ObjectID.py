import requests
import pymongo
import starship_pilots as sp


client = pymongo.MongoClient()

db = client['starwars']

class ReplacePilotUrls(sp.Starship_Pilots):

    def __init__(self):
        super().__init__()

    def pilot_ids(self):
        pilot_names = []
        for starships in self.list:
            pilots = list(starships.values())[0]
            if len(pilots) >= 1:
                get_starship_name = list(starships.keys())
                starship = get_starship_name[0]
                driver_dict = {starship: []}
                for pilot in pilots:
                    pilot_details = requests.get(pilot)
                    json_pilot_details = pilot_details.json()
                    driver_dict[starship].append(json_pilot_details['name'])
                pilot_names.append(driver_dict)

        pilot_objectids = []
        for starships in pilot_names:
            get_starship_name = list(starships.keys())
            starship = get_starship_name[0]
            pilot_ids_dict = {starship: []}
            name_list = list(starships.values())[0]
            for name in name_list:
                character = db.characters.find_one({"name": name}, {"_id": 1})
                if character:
                    pilot_ids_dict[starship].append(character["_id"])
            pilot_objectids.append(pilot_ids_dict)

        return pilot_objectids

    def replace_urls_with_objectids(self):
        self.starship
        pilot_object_ids = self.pilot_ids()
        
        for starships in pilot_object_ids:
            get_starship_name = list(starships.keys())
            starship = get_starship_name[0]
            if starship ==


pilot_replace = ReplacePilotUrls()

pilot_replace.replace_urls_with_objectids()