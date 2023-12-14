import swapi_call
import requests


class Starship_Pilots(swapi_call.StarWarsAPI):

    def __init__(self):
        super().__init__()
        starship_results = self.get_starships_data()['results']
        self.list = []
        for i in starship_results:
            self.list.append({i['name']: i['pilots']})

##


