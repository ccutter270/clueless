import { Action } from "./action.model";
import { Character } from "./character.model";

export interface GameState {
    started: Boolean,
    characters: Character[],
    current_player: string,
    lastActionTaken: Action
}