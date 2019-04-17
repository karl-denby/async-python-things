# async-python-things

## Setup
1. Ensure you have pipenv installed, through your package manager or via `pip install pipenv`
1. Create virtual environment and install dependencies with `pipenv install`
1. Also run `pipenv run pip install chatterbot` * 

* pipenv when it installs chatterbot-corpus doesn't pull in chatterbot as it would have a conflicting version of pyyaml, this is hacky but it works until chatterbot-corpus upgrades to a newer pyyaml

## Usage
1. Get a shell in the virtual environment with `pipenv shell`
1. Run the server with `pipenv run python app.py`
1. Run the client with `pipenv run python client.py`

## TODO list in no particular order
- Create a frontend in Vue.js
- Train Diego to understand more things
- Add more endpoints to the API
- Create a working docker image
