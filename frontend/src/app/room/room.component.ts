import { CommonModule, NgFor } from '@angular/common'
import { Component, Input } from '@angular/core'

@Component({
  selector: 'room',
  standalone: true,
  imports: [NgFor, CommonModule],
  templateUrl: './room.component.html',
  styleUrl: './room.component.css',
})
export class RoomComponent {
  @Input() roomName: string = ''
  @Input() image: string = ''
  @Input() characters: any[] = []

  getPlayerIcon(
    characterId:
      | 'Professor Plum'
      | 'Miss Scarlet'
      | 'Colonel Mustard'
      | 'Mrs. Peacock'
      | 'Mr. Green'
      | 'Mrs. White',
  ): string {
    const playerIcons = {
      'Colonel Mustard': 'colonel-mustard.jpg',
      'Professor Plum': 'professor-plum.jpg',
      'Miss Scarlet': 'miss-scarlett.jpg',
      'Mrs. White': 'mrs-white.jpg',
      'Mr. Green': 'mr-green.jpg',
      'Mrs. Peacock': 'miss-peacock.jpg',
    }

    const iconURL = playerIcons[characterId] || 'pink.jpg'
    return iconURL
  }
}
