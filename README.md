# Star Wars Project
This project involved creating an ETL pipeline for Star Wars information obtained from the Star Wars API (https://swapi.dev/). The API provides information about various entities in the Star Wars universe, including starships and characters.

## Data Source
The data used in this project was sourced from the [Star Wars API](https://swapi.dev/). The API provides a RESTful interface to access a wealth of information about Star Wars, including details about starships and characters.

## Task Overview
The primary task of this project was to pull data on all available starships from the API. The "pilots" key in the starships data contains URLs pointing to the characters who pilot the starship. 

The goal was to replace 'pilots' with a list of ObjectIDs from our characters collection. After this transformation, the starships data was inserted into its own collection using MongoDB for the backend. This allows effective filtering when querying the Star Wars data.

## Implementation
To achieve this task, Python scripts have been developed. The following steps outline the process:


## Data Extraction:
- Utilized the requests library to fetch data on all available starships from the Star Wars API.

## Data Transformation:
- Implemented functions to transform the starships data, specifically retrieving the information from the pilot URL's and replacing the URLs with character ObjectIDs cross-referenced from our characters collection.

## Data Loading:
- Implemented functions to connect to a MongoDB database and insert the transformed starships data into its own collection.

## Requiremnts:
- Latest Python version (3.11)
- MongoDB 5.0 or later
  - MongoDB Compass
  - MongoDB Shell
  - MongoDB Database Tools
- pip install pymongo

## Amazing Contributers:
- Jesse Rolfe (<https://github.com/jvrolfe>)
- T Oladimeji (<https://github.com/T-meji>)
- Medan Grant-Anderson (<https://github.com/MedanG-A>)
- Aymen Shallal (<https://github.com/Shalala06>)
- Seb Manley (<https://github.com/SebManley>)
- Richard Van Parys (<https://github.com/ReggieVP>)
