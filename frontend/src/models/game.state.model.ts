import { Action } from "./action.model";
import { Character } from "./character.model";

export interface GameState {
    characters: Character[],
    currentTurn: string,
    lastActionTaken: Action
}