import { Injectable, signal, Signal } from '@angular/core';
import { GameState } from '../models/game.state.model';

@Injectable({
  providedIn: 'root'
})
export class GameStateService {

  constructor() { }

  gameState = signal<GameState>({
    character: [
      {
        name: "Professor Plum",
        location: {
          name: "Kitchen",
          locationType: "Room",
          connectedLocations: [
            {
              name: "Kitchen",
              locationType: "Room",
              connectedLocations: [],
              occupied: true,
              weapon: {
                name: "Wrench"
              }
            },
            {
              name: "Kitchen",
              locationType: "Room",
              connectedLocations: [],
              occupied: true,
              weapon: {
                name: "Wrench"
              }
            }
          ],
          occupied: true,
          weapon: {
            name: "Wrench"
          }
        },
        homeSquare: {
          name: "Kitchen",
          locationType: "Room",
          connectedLocations: [],
          occupied: true,
          weapon: {
            name: "Wrench"
          }
        }
      }
    ],
    currentTurn: "Professor Plum",
    lastActionTaken: {
      type: "Action",
      character: "Professor Plum",
      location: "Kitchen",
      message: "Professor Plum moved to Kitchen."
    }
  })
}
