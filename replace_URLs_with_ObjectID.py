import requests
import pymongo
import starship_pilots as sp
import swapi_call as sw


client = pymongo.MongoClient()

db = client['starwars']


class ReplacePilotUrls(sp.Starship_Pilots, sw.StarWarsAPI):

    def __init__(self):
        super().__init__()

    def pilot_ids(self):
        # pilot_names will be populated with the names of the pilots from the starships database
        pilot_names = []
        for starships in self.list:             # self.list is a list of dictionaries. Each dict is a starship.
            pilots = list(starships.values())[0]        # Extracting the list of pilot names from the starship dict.
            if len(pilots) >= 1:
                get_starship_name = list(starships.keys())
                starship = get_starship_name[0]                 # Extracting the name of the starship.
                driver_dict = {starship: []}
                for pilot in pilots:
                    pilot_details = requests.get(pilot)         # Requesting the pilot data from the pilot URL
                    json_pilot_details = pilot_details.json()       # Converting the response to json
                    driver_dict[starship].append(json_pilot_details['name'])
                pilot_names.append(driver_dict)

        # A list of dictionaries with starship as the key and a list of pilot ids.
        pilot_objectids = []
        for starships in pilot_names:
            get_starship_name = list(starships.keys())
            starship = get_starship_name[0]             # Extracting the starship name
            pilot_ids_dict = {starship: []}
            name_list = list(starships.values())[0]     # Extracting the list of pilot names
            for name in name_list:
                # Finding the pilot_id from the characters collection
                character = db.characters.find_one({"name": name}, {"_id": 1})
                if character:
                    pilot_ids_dict[starship].append(character["_id"])
            pilot_objectids.append(pilot_ids_dict)

        return pilot_objectids

    def replace_urls_with_objectids(self):
        pilot_object_ids = self.pilot_ids()
        starships_data = self.get_starships_data()['results']
        for i in range(len(starships_data)):
            if len(starships_data[i]['pilots']) >= 1:
                for pilot in starships_data[i]['pilots']:
                    for ship_dict in pilot_object_ids:
                        for each_ship in ship_dict:
                            if starships_data[i]['name'] == each_ship:
                                starships_data[i]['pilots'] = ship_dict[each_ship]

        return starships_data



