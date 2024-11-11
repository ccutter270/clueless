import { CommonModule } from '@angular/common';
import { Component, OnDestroy, OnInit } from '@angular/core';
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
import { GameState } from '../models/GameState';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, RoomComponent, HallwayComponent, EmptyComponent, CommonModule, WebsocketTesterComponent, GameStateComponent, GameInputComponent, TrackingCardComponent, PlayerInputComponent],
  providers: [WebSocketService],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})

export class AppComponent implements OnInit, OnDestroy {
  messages: GameState[] = [];
  private broadcastSubscription!: Subscription;

  constructor(private webSocketService: WebSocketService) { }
  title = 'Clue';
  game_state: GameState = {
    character: [
      {
        name: "Professor Plum",
        location: {
          name: "Kitchen",
          locationType: "Room",
          connectedLocations: [],
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
      message: "Professor Plum moved to Kitchen."
    }
  }
  Areas = [
    { name: "Study", type: "room", photo: "study.jpg" },
    { name: "Study to Hall", type: "hall", photo: "hallway.jpg" },
    { name: "Hall", type: "room", photo: "hall.jpg" },
    { name: "Hall to Lounge", type: "hall", photo: "hallway.jpg" },
    { name: "Lounge", type: "room", photo: "lounge.jpg" },
    { name: "Study to Library", type: "hall", photo: "hallway.jpg" },
    { name: "top left", type: "empty" },
    { name: "Hall to Billiard", type: "hall", photo: "hallway.jpg" },
    { name: "top right", type: "empty" },
    { name: "Lounge to Dining", type: "hall", photo: "hallway.jpg" },
    { name: "Library", type: "room", photo: "library.jpg" },
    { name: "Library to Billiard", type: "hall", photo: "hallway.jpg" },
    { name: "Billiard Room", type: "room", photo: "billiard.jpg" },
    { name: "Billiard to Dining", type: "hall", photo: "hallway.jpg" },
    { name: "Dining Room", type: "room", photo: "dining.jpg" },
    { name: "Library to Conservatory", type: "hall", photo: "hallway.jpg" },
    { name: "bottom left", type: "empty" },
    { name: "Billiard to Ball", type: "hall", photo: "hallway.jpg" },
    { name: "bottom right", type: "empty" },
    { name: "Dining to Kitchen", type: "hall", photo: "hallway.jpg" },
    { name: "Conservatory", type: "room", photo: "conservatory.jpg" },
    { name: "Conservatory to Ball", type: "hall", photo: "hallway.jpg" },
    { name: "Ball-Room", type: "room", photo: "ball.jpg" },
    { name: "Ball to Kitchen", type: "hall", photo: "hallway.jpg" },
    { name: "Kitchen", type: "room", photo: "kitchen.jpg" },
  ]

  // coming from server
  characters: any[] = [
    {characterId: "Colonel Mustard", locationId: "Study"},
    {characterId: "Professor Plum", locationId: "Study"},
    {characterId: "Miss Scarlet", locationId: "Study"},
    {characterId: "Mrs. White", locationId: "Study"},
    {characterId: "Mr. Green", locationId: "Study"},
    {characterId: "Mrs. Peacock", locationId: "Study"}
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

    const iconURL = playerIcons[characterId] || "pink.jpg";
    return iconURL    
  }

  trackByFn(index: number, item: any) {
    return item.name; // You can use a unique property
  }


  ngOnInit() {
    // Send initial ping to server to start broadcasts
    this.webSocketService.pingForBroadcast();
    console.log('Sent broadcast request to server');

    // Subscribe to broadcast messages from the server
    this.broadcastSubscription = this.webSocketService.onBroadcast().subscribe(
      (broadcast: any) => {
        this.messages.push(broadcast.data); // Assuming broadcast contains a 'data' property
        console.log('Received broadcast:', broadcast);
      },
      (error) => console.error('Broadcast error:', error)
    );
  }

  ngOnDestroy() {
    // Unsubscribe to prevent memory leaks
    this.webSocketService.close();
  }
}
