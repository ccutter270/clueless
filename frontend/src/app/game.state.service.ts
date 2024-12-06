import { Injectable, signal } from '@angular/core'
import { GameState } from '../models/game.state.model'
import { Character } from '../models/character.model'
import { NONE_TYPE } from '@angular/compiler'
import { EmptyComponent } from './empty/empty.component'

@Injectable({
  providedIn: 'root',
})
export class GameStateService {
  constructor() {}

  gameState = signal<GameState>({
    started: false,
    flow: '',
    characters: [],
    current_player: {
      name: '',
      location: {
        name: '',
        locationType: '',
        connectedLocations: [],
        occupied: true,
        weapon: { name: '' },
      },
      homeSquare: {
        name: '',
        locationType: '',
        connectedLocations: [],
        occupied: true,
        weapon: { name: '' },
      },
      moved_to: false,
    },
    lastActionTaken: {
      type: '',
      character: '',
      location: '',
      message: '',
    },
  })

  getGameState(): GameState {
    return this.gameState()
  }
}
