## Record Keeper

A friendly little CLI and webapp that reads in person records and displays them in sorted order. Done as homework for a prospective new employer.

### Running

#### CLI

`python3 record_parser.py --sort-choice=2 --files=../mock_data/MOCK_DATA_1.csv,../mock_data/MOCK_DATA_1.csv`

`sort-choice` options:
1) _(default)_ Females before males, then last name ascending, e.g. (Lisa Ashcroft, Lisa Zulu, Dan Asher, Dan Weber).
2) DoB ascending (oldest person first), e.g. (1960, 1970, 2010). 
3) Last name descending, (Hank Zimmerman, Hank Martinez, Hank Bolt, Hank Asher)


#### App Server

1) `python3 -m pip install requirements.txt`
2) `python3 app/server.py`

Reachable at `localhost:5000`

### Tests

#### Unit Tests

1) `python3 -m pip install requirements.txt`
2) `python3 -m pytest tests/`


#### API Testing

Executed through Postman GUI. Postman does have the option to run tests through CLI, so these could be integrated into a CICD-like pipelike in the future.

1) Download postman from http://getpostman.com and open it.
2) In upper left, import collection `RecordKeeper.postman_collection.json`
3) In upper right (gear), import environment `RecordKeeper LOCALHOST.postman_environment.json`
4) Run collection
