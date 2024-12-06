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
$ autopep8 --in-place --recursive hoodid/
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
$ pip install -r hoodid/requirements.txt
```

Run:

```sh
$ python3 <directory>/clueless/hoodid/app.py
```

This should run on http://127.0.0.1:5000

## TODO List

Ongoing list of thing that still need to be done as we find them

- Make a "go back" button for move options? especially accuse so if player accidentally presses accuse they can go back and chose a different option
- If a player drops out during the game - remove them & distribute their cards to others(stretch goal)
- If there are no move options (all hallways are blocked), allow for accusation but not movement (can't make a suggestion)
- Update game state more often / when actions are taken
  - just change "self.last_action_taken" in game class to desired string, then call self.send_game_state
- Add error popup message when too many people in game (aka for emit('game_error', {'message': "Maximum players already reached."}))
- Update "self.flow" so that frontend only shows things when needed. Here are some examples of what "flow" values can be:

  | Self.flow         | Description                                                 | UI Features enabled      |
  | ----------------- | ----------------------------------------------------------- | ------------------------ |
  | **not_started**   | Waiting for game to start                                   | game board               |
  | **get_action**    | Waiting for player to choose an action                      | game board, player-input |
  | **move**          | Player chose move, in move sequence                         | game board, move-to box  |
  | **suggest**       | Player chose suggest or placed in suggest sequence          | game board, game-input   |
  | **wait_disprove** | Wait for players to disprove                                | game board               |
  | **ask_accuse**    | Ask player if accuse or next turn game board, accuse-prompt |
  | **accuse**        | Player chose to accuse                                      | game board, game-input   |

- Display message when waiting for people to disprove (just for clarity of game flow)
- Accusation logic

  - if correct, use message-popup to display they won
  - if wrong, remove them as "player" so they can't have a turn, but allow them to disprove?

- Once the game has started (i.e after start game button is pressed) don't allow new players to join

  - started implementing in @socketio.on('player_connected')... need to add popup to persons screen

- Accusation disproof function should only show close button if nothing to disprove (check rules if you have to disprove something)

### Known Bugs

- Figure out how to do the validation on the location part of the form for accuse logic
