// location.model.ts
import { Weapon } from './weapon.model';

export interface Location {
    name: string;
    locationType: string;
    connectedLocations: Location[]; // Array of Location objects
    occupied: boolean;
    weapon: Weapon;
}