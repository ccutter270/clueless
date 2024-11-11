import { Action } from "./action.model";
import { Character } from "./character.model";

export interface GameState {
    character: Character[],
    currentTurn: string,
    lastActionTaken: Action
}