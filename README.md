# clueless

JHU EN.605.601 Software Engineering Project Fall 2024

## How to Run

### Run formatter

```sh
# For Frontend
$ npm install --save-dev prettier
$ npx prettier --write .

# For backend
$ pip install autopep8
$ autopep8 --in-place --recursive backend/
```

### Frontend

```sh
$ cd clueless/frontend
$ npm install
```

```sh
$ sudo ng serve
```

This should run on http://localhost:4200/

### Backend

Create venv:

```sh
$ cd <directory>/clueless
$ python3 -m venv venv
$ source venv/bin/activate
```

Install requirements:

```sh
$ pip install -r backend/requirements.txt
```

Run:

```sh
$ python3 <directory>/clueless/backend/app.py
```

This should run on http://127.0.0.1:5000

## TODO List

Ongoing list of thing that still need to be done as we find them

- Update the game state when necessary
  - just change "self.last_action_taken" in game class to desired string, then call self.send_game_state

### Known Bugs

- Figure out how to do the validation on the location part of the form for accuse logic


- Deployment of front end isn't working
npx http-server ./dist/clue
