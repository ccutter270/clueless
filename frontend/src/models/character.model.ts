// character.model.ts
import { Location } from './location.model'

export interface Character {
  name: string
  location: Location
  homeSquare: Location
  moved_to: boolean
}
