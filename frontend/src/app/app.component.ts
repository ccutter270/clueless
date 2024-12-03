import { ChangeDetectorRef } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Component, HostListener, inject, OnDestroy, OnInit } from '@angular/core';
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
import { MoveToComponent } from "./move-to/move-to.component";
import { DisplayCardComponent } from "./display-cards/display-cards.component";
import { GameState } from '../models/game.state.model';
import { Subscription } from 'rxjs';
import { GameStateService } from './game.state.service';
import { UserService } from './user.service';
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, RoomComponent, HallwayComponent, EmptyComponent, CommonModule, WebsocketTesterComponent, GameStateComponent, GameInputComponent, TrackingCardComponent, PlayerInputComponent, MoveToComponent, DisplayCardComponent],
  providers: [WebSocketService],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})

export class AppComponent implements OnInit, OnDestroy {

  webSocketService = inject(WebSocketService)
  gameStateService = inject(GameStateService)
  userService = inject(UserService)
  cdr = inject(ChangeDetectorRef)

  states: GameState[] = [];
  private broadcastSubscription!: Subscription;
  private userAssignmentSubscription!: Subscription;
  private moveOptionSubscription!: Subscription;


  @HostListener('window:beforeunload', ['$event'])
  onBeforeUnload(event: BeforeUnloadEvent): void {
    this.webSocketService.close();
  }

  
  title = 'Clue';
  
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
    {characterId: "Miss Scarlet", locationId: "Ball to Kitchen"},
    {characterId: "Mrs. White", locationId: "Study"},
    {characterId: "Mr. Green", locationId: "Ball to Kitchen"},
    {characterId: "Mrs. Peacock", locationId: "Study"}
  ];
  
  // Get filtered characters for each area
  getCharactersForArea(areaName: string): any[] {
    return this.characters.filter(character => character.locationId === areaName);
  }

  options: string[] = ['move', 'suggest', 'accuse'];

  move_options: string [] = []

  // TODO: Create a "Start Game" button, and on this signal, we can get
  // initial game state & set number of players, assign cards and then fill these
  // out for each of the players based on their character
  cards: string [] = ["Test", "Test", "Test", "Test", "Test", "Test", "Test"]


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

    // Subscribe to broadcast states from the server
    this.broadcastSubscription = this.webSocketService.onBroadcast().subscribe(
      (broadcast: any) => {
        this.gameStateService.gameState.set(broadcast.data);
        this.states.push(broadcast.data); // Assuming broadcast contains a 'data' property
        console.log('Received broadcast:', broadcast);
      },
      (error) => console.error('Broadcast error:', error)
    );

    this.userAssignmentSubscription = this.webSocketService.onPlayerAssignment().subscribe(
      (playerAssignment: any) => {
        console.log("Received Player Assignment", playerAssignment)
        this.userService.assignedCharacter.set(playerAssignment.character);
      },
      (error) => console.error("Player Assignment error")
    )


    this.moveOptionSubscription = this.webSocketService.onMoveOptions().subscribe(
      (moveOptions: any) => {
        console.log("Received Move Options", moveOptions)
        console.log("Options", this.options)
        this.move_options = moveOptions;
      },
      (error) => console.error("Move Option error")
    )
  }

  ngOnDestroy() {
    // Unsubscribe to prevent memory leaks
    this.webSocketService.close();
  }
}
