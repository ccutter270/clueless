import { CommonModule, NgFor } from '@angular/common';
import { Component, Input } from '@angular/core';

@Component({
  selector: 'hallway',
  standalone: true,
  imports: [NgFor, CommonModule],
  templateUrl: './hallway.component.html',
  styleUrl: './hallway.component.css'
})
export class HallwayComponent {
  @Input() hallName: string = "";
  @Input() imageURL: string ="";
  @Input() characters: any[] = [];

  getPlayerIcon(characterId: "Professor Plum" | "Miss Scarlet" | "Colonel Mustard" | "Mrs. Peacock" | "Mr. Green" | "Mrs. White"): string {

    const playerIcons = {
      "Colonel Mustard": "colonel-mustard.jpg",
      "Professor Plum": "professor-plum.jpg",
      "Miss Scarlet": "miss-scarlett.jpg",
      "Mrs. White": "mrs-white.jpg",
      "Mr. Green": "mr-green.jpg",
      "Mrs. Peacock": "miss-peacock.jpg"
    };

    const iconURL = playerIcons[characterId] || "pink.jpg";
    return iconURL
  }
}
