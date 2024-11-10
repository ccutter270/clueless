import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { RoomComponent } from "./room/room.component";
import { HallwayComponent } from "./hallway/hallway.component";
import { EmptyComponent } from './empty/empty.component';
import { WebSocketService } from './websocket.service';
import { WebsocketTesterComponent } from './websocket.tester/websocket.tester.component';
import { GameStateComponent } from './game-state/game-state.component';
import { GameInputComponent } from './game-input/game-input.component';
import { TrackingCardComponent } from './tracking-card/tracking-card.component';
import { PlayerInputComponent } from "./player-input/player-input.component";

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, RoomComponent, HallwayComponent, EmptyComponent, CommonModule, WebsocketTesterComponent, GameStateComponent, GameInputComponent, TrackingCardComponent, PlayerInputComponent],
  providers: [WebSocketService],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})

export class AppComponent {
  title = 'Clue';
  Areas = [
    {name: "Study", type: "room", photo: "study.jpg"},
    {name: "Study to Hall", type: "hall", photo: "hallway.jpg"},
    {name: "Hall", type: "room", photo: "hall.jpg"},
    {name: "Hall to Lounge", type: "hall", photo: "hallway.jpg"},
    {name: "Lounge", type: "room", photo: "lounge.jpg"},
    {name: "Study to Library", type: "hall", photo: "hallway.jpg"},
    {name: "top left", type: "empty"},
    {name: "Hall to Billiard", type: "hall", photo: "hallway.jpg"},
    {name: "top right", type: "empty"},
    {name: "Lounge to Dining", type: "hall", photo: "hallway.jpg"},
    {name: "Library", type: "room", photo: "library.jpg"},
    {name: "Library to Billiard", type: "hall", photo: "hallway.jpg"},
    {name: "Billiard Room", type: "room", photo: "billiard.jpg"},
    {name: "Billiard to Dining", type: "hall", photo: "hallway.jpg"},
    {name: "Dining Room", type: "room", photo: "dining.jpg"},
    {name: "Library to Conservatory", type: "hall", photo: "hallway.jpg"},
    {name: "bottom left", type: "empty"}, 
    {name: "Billiard to Ball", type: "hall", photo: "hallway.jpg"}, 
    {name: "bottom right", type: "empty"}, 
    {name: "Dining to Kitchen", type: "hall", photo: "hallway.jpg"}, 
    {name: "Conservatory", type: "room", photo: "conservatory.jpg"},
    {name: "Conservatory to Ball", type: "hall", photo: "hallway.jpg"},
    {name: "Ball-Room", type: "room", photo: "ball.jpg"},
    {name: "Ball to Kitchen", type: "hall", photo: "hallway.jpg"},
    {name: "Kitchen", type: "room", photo: "kitchen.jpg"},
  ]

  // coming from server
  characters: any[] = [
    {characterId: "Colonel Mustard", locationId: "Study"},
    {characterId: "Professor Plum", locationId: "Conservatory to Ball"},
  ];

  getPlayerIcon(characterId: "Professor Plum" | "Miss Scarlet" | "Colonel Mustard" | "Mrs. Peacock" | "Mr. Green" | "Mrs. White"): string {

    const playerIcons = {
      "Colonel Mustard": "colonel-mustard.jpg",
      "Professor Plum": "professor-plum.jpg",
      "Miss Scarlet": "miss-scarlett.jpg",
      "Mrs. White": "mrs-white.jpg",
      "Mr. Green": "mr-green.jpg",
      "Mrs. Peacock": "miss-peacock.jpg"
    };

    return playerIcons[characterId] || "pink.jpg";

  }
}
