from starship_pilots import *
from swapi_call import *
from replace_URLs_with_ObjectID import *
import unittest
# import pymongo
from unittest.mock import patch, Mock


class TestSWAPICall(unittest.TestCase):

    def test_default_swapi_base_url(self):
        instance = StarWarsAPI()
        self.assertEqual(instance.swapi_base_url, 'https://swapi.dev/api/',
                         "Default swapi_base_url is not set correctly")

    def test_custom_swapi_base_url(self):
        custom_url = 'https://custom-swapi-url.com/api/'
        instance = StarWarsAPI(swapi_base_url=custom_url)
        self.assertEqual(instance.swapi_base_url, custom_url,
                         "Custom swapi_base_url is not set correctly")

    @patch('swapi_call.r.get')
    def test_get_starships_data(self, mock_get):
        # Mocking the response of the requests.get method
        mock_response = unittest.mock.Mock()
        mock_response.json.return_value = {'results': [{'name': 'Starship1'}, {'name': 'Starship2'}]}
        mock_get.return_value = mock_response

        # Creating an instance of StarWarsAPI
        star_wars_api = StarWarsAPI()

        # Calling the method we want to test
        result = star_wars_api.get_starships_data()

        # Assertions
        mock_get.assert_called_once_with('https://swapi.dev/api/starships/')
        self.assertEqual(result, {'results': [{'name': 'Starship1'}, {'name': 'Starship2'}]})


class TestStarshipPilotsInitialization(unittest.TestCase):

    @patch('starship_pilots.Starship_Pilots.get_starships_data')
    def test_starship_pilots_list(self, mock_get_starships_data):
        # Mocking the response of the get_starships_data method
        mock_get_starships_data.return_value = {'results': [
            {'name': 'Starship1', 'pilots': ['Pilot1', 'Pilot2']},
            {'name': 'Starship2', 'pilots': ['Pilot3', 'Pilot4']},
        ]}

        # Creating an instance of Starship_Pilots
        starship_pilots = Starship_Pilots()

        expected_list = [
            {'Starship1': ['Pilot1', 'Pilot2']},
            {'Starship2': ['Pilot3', 'Pilot4']},
        ]

        self.assertEqual(starship_pilots.list, expected_list,
                         "Starship_Pilots list is not initialized correctly")


class TestReplacePilotUrls(unittest.TestCase):

    @patch('replace_URLs_with_ObjectID.sp.Starship_Pilots.get_starships_data')
    @patch('replace_URLs_with_ObjectID.db.characters.find_one')
    @patch('replace_URLs_with_ObjectID.requests.get')
    def test_pilot_ids(self, mock_get, mock_find_one, mock_get_starships_data):
        # Mocking starship data from the sp module
        mock_get_starships_data.return_value = {'results': [
            {'name': 'Starship1', 'pilots': ['https://mockpilot1', 'https://mockpilot2']},
            {'name': 'Starship2', 'pilots': ['https://mockpilot3', 'https://mockpilot4']}
        ]}

        # Mocking responses for requests.get
        mock_get_responses = [
            Mock(json=lambda: {'name': 'Pilot1'}),
            Mock(json=lambda: {'name': 'Pilot2'}),
            Mock(json=lambda: {'name': 'Pilot3'}),
            Mock(json=lambda: {'name': 'Pilot4'})
        ]
        mock_get.side_effect = mock_get_responses

        # Mocking database responses
        mock_find_responses = [
            {'_id': 'ObjectID1'},
            {'_id': 'ObjectID2'},
            {'_id': 'ObjectID3'},
            {'_id': 'ObjectID4'}
        ]
        mock_find_one.side_effect = mock_find_responses

        # Creating an instance of ReplacePilotUrls
        replace_pilot_urls = ReplacePilotUrls()

        # Calling the method we want to test
        result = replace_pilot_urls.pilot_ids()

        # Assertions
        expected_result = [
            {'Starship1': ['ObjectID1', 'ObjectID2']},
            {'Starship2': ['ObjectID3', 'ObjectID4']}
        ]
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
