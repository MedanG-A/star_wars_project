import swapi_call as swapi
import starship_pilots as sp
import replace_URLs_with_ObjectID as rurl
import starships_to_collection as stc

import_starships = swapi.StarWarsAPI()
starships_api_data = import_starships.get_starships_data()

pilot_urls = sp.Starship_Pilots()

replace_pilot_urls = rurl.ReplacePilotUrls()
pilot_ids = replace_pilot_urls.replace_urls_with_objectids()

send_to_collection = stc.StarshipsToCollection()
collection_creation = send_to_collection.starshipstocoll()