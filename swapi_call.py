import requests as r
import json

# starwars_url = r.get('https://swapi.dev/api/starships')
# starwars_json = starwars_url.json()


# print(type(starwars_json))

class StarWarsAPI():
    def __init__(self, swapi_base_url='https://swapi.dev/api/'):
        self.swapi_base_url = swapi_base_url

    def get_starships_data(self):
        starwars_url = f'{self.swapi_base_url}starships/'
        response = r.get(starwars_url)
        return response.json()
