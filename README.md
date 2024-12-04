# clueless
JHU EN.605.601 Software Engineering Project Fall 2024 


## How to Run

### Frontend

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

- Start button - press to launch game. This will allow more than 3 players to join before starting
- Update game state more often / when actions are taken 
    - just change "self.last_action_taken" in game class to desired string, then call self.send_game_state
- Update "self.flow" so that frontend only shows things when needed. Here are some examples of what "flow" values can be:

    | Self.flow                | Description                                | UI Features enabled     |            
    |-----------------------|-----------------------------------------------|----------------
    | **not_started** | Waiting for game to start  |   game board
    | **get_action** | Waiting for player to choose an action | game board, player-input
    | **move**  | Player chose move, in move sequence   | game board, move-to box
    | **suggest** | Player chose suggest or placed in suggest sequence |  game board, game-input
    | **accuse** | Player chose to accuse | game board, game-input


- Display message when waiting for people to disprove (just for clarity of game flow)
- Accusation logic
    - if correct, use message-popup to display they won
    - if wrong, remove them as "player" so they can't have a turn, but allow them to disprove?



### Known Bugs
- On startup, seems to "start" the game 3x (aka things are assigned 3 different times, look at output on python terminal when starting)

