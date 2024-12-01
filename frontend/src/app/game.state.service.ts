import { Injectable, signal } from '@angular/core';
import { GameState } from '../models/game.state.model';

@Injectable({
  providedIn: 'root'
})
export class GameStateService {

  constructor() { }

  gameState = signal<GameState>({
    started: false,
    flow: "",
    characters: [],
    current_player: "",
    lastActionTaken: {
      type: "",
      character: "",
      location: "",
      message: ""
    }
  })
}
