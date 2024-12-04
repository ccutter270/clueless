import { NgModule } from '@angular/core'
import { ChangeDetectorRef } from '@angular/core'
import { CommonModule } from '@angular/common'
import { Component, HostListener, inject, OnDestroy, OnInit } from '@angular/core'
import { RouterOutlet } from '@angular/router'
import { RoomComponent } from './room/room.component'
import { HallwayComponent } from './hallway/hallway.component'
import { EmptyComponent } from './empty/empty.component'
import { WebSocketService } from './websocket.service'
import { WebsocketTesterComponent } from './websocket.tester/websocket.tester.component'
import { GameStateComponent } from './game-state/game-state.component'
import { GameInputComponent } from './game-input/game-input.component'
import { TrackingCardComponent } from './tracking-card/tracking-card.component'
import { PlayerInputComponent } from './player-input/player-input.component'
import { MoveToComponent } from './move-to/move-to.component'
import { DisplayCardComponent } from './display-cards/display-cards.component'
import {
  DisproveSuggestionComponent,
  Suggestion,
} from './disprove-suggestion/disprove-suggestion.component'
import { GeneralMessagePopupComponent } from './message-popup/message-popup.component'

import { GameState } from '../models/game.state.model'
import { Subscription } from 'rxjs'
import { GameStateService } from './game.state.service'
import { UserService } from './user.service'
import { Injectable } from '@angular/core'
import { HttpClient } from '@angular/common/http'
import { Observable } from 'rxjs'
import { MatDialog } from '@angular/material/dialog'
import { StartButtonComponent } from "./start-button/start-button.component";
import { MaterialDialogComponent } from './material-dialog/material-dialog.component'

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [
    RouterOutlet,
    RoomComponent,
    HallwayComponent,
    EmptyComponent,
    CommonModule,
    WebsocketTesterComponent,
    GameStateComponent,
    GameInputComponent,
    TrackingCardComponent,
    PlayerInputComponent,
    MoveToComponent,
    DisplayCardComponent,
    DisproveSuggestionComponent,
    GeneralMessagePopupComponent,
    StartButtonComponent
],
  providers: [WebSocketService],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css',
})
export class AppComponent implements OnInit, OnDestroy {
  webSocketService = inject(WebSocketService)
  gameStateService = inject(GameStateService)
  userService = inject(UserService)
  cdr = inject(ChangeDetectorRef)

  states: GameState[] = []
  private broadcastSubscription!: Subscription
  private userAssignmentSubscription!: Subscription
  private displayCardsSubscription!: Subscription
  private moveOptionSubscription!: Subscription
  private suggestionSubscription!: Subscription
  private disproveSubscription!: Subscription
  private startButtonSubscription!: Subscription
  showSpinnerDialog: boolean = false;

  @HostListener('window:beforeunload', ['$event'])
  onBeforeUnload(event: BeforeUnloadEvent): void {
    this.webSocketService.close()
  }

  title = 'Clue'

  Areas = [
    { name: 'Study', type: 'room', photo: 'study.jpg' },
    { name: 'Study to Hall', type: 'hall', photo: 'hallway.jpg' },
    { name: 'Hall', type: 'room', photo: 'hall.jpg' },
    { name: 'Hall to Lounge', type: 'hall', photo: 'hallway.jpg' },
    { name: 'Lounge', type: 'room', photo: 'lounge.jpg' },
    { name: 'Study to Library', type: 'hall', photo: 'hallway.jpg' },
    { name: 'top left', type: 'empty' },
    { name: 'Hall to Billiard', type: 'hall', photo: 'hallway.jpg' },
    { name: 'top right', type: 'empty' },
    { name: 'Lounge to Dining', type: 'hall', photo: 'hallway.jpg' },
    { name: 'Library', type: 'room', photo: 'library.jpg' },
    { name: 'Library to Billiard', type: 'hall', photo: 'hallway.jpg' },
    { name: 'Billiard Room', type: 'room', photo: 'billiard.jpg' },
    { name: 'Billiard to Dining', type: 'hall', photo: 'hallway.jpg' },
    { name: 'Dining Room', type: 'room', photo: 'dining.jpg' },
    { name: 'Library to Conservatory', type: 'hall', photo: 'hallway.jpg' },
    { name: 'bottom left', type: 'empty' },
    { name: 'Billiard to Ballroom', type: 'hall', photo: 'hallway.jpg' },
    { name: 'bottom right', type: 'empty' },
    { name: 'Dining to Kitchen', type: 'hall', photo: 'hallway.jpg' },
    { name: 'Conservatory', type: 'room', photo: 'conservatory.jpg' },
    { name: 'Conservatory to Ballroom', type: 'hall', photo: 'hallway.jpg' },
    { name: 'Ballroom', type: 'room', photo: 'ball.jpg' },
    { name: 'Ballroom to Kitchen', type: 'hall', photo: 'hallway.jpg' },
    { name: 'Kitchen', type: 'room', photo: 'kitchen.jpg' },
  ]

  // Get filtered characters for each area
  getCharactersForArea(areaName: string): any[] {
    // If characters not set, return none
    if (this.gameStateService.getGameState().characters == undefined) {
      return []
    }

    const matchingCharacters = Object.values(
      this.gameStateService.getGameState().characters,
    ).filter(character => {
      return character.location.name === areaName
    })

    return matchingCharacters
  }

  num_players = 0

  options: string[] = ['move', 'suggest', 'accuse']

  move_options: string[] = []
  cards: string[] = []

  // Disprove Suggestion Variables
  showDisproveModal = false
  total_disproves = 0

  // Disprove Popup
  popupMessage: string = ''
  isPopupOpen: boolean = false

  // hide show start button
  showStartButton: boolean = false
  startButtonMessage: string = ''

  currentSuggestion: Suggestion = {
    character: '',
    location: '',
    weapon: '',
  }

  onDisproveCard(card: string) {
    console.log(`Player disproved with card: ${card}`)
    this.webSocketService.sendDisprove(card)
    this.showDisproveModal = false
  }

  onClose() {
    console.log(`Player is done disproving.`)
  }

  showMessage(message: string) {
    // Set the popup message and show the popup
    this.popupMessage = message
    this.isPopupOpen = true
  }

  closePopup() {
    // Close the popup
    this.isPopupOpen = false
  }

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

  trackByFn(index: number, item: any) {
    return item.name // You can use a unique property
  }

  readonly dialog = inject(MatDialog);

  openDialog(): void {
    this.dialog.open(MaterialDialogComponent, {
      width: '250px',
      disableClose: true,
      data: {
        message: "Awaiting input from other players",
        showSpinner: true
      }
    });
  }

  ngOnInit() {
    // Send initial ping to server to start broadcasts
    this.webSocketService.pingForBroadcast()
    console.log('Sent broadcast request to server')

    // Subscribe to broadcast states from the server
    this.broadcastSubscription = this.webSocketService.onBroadcast().subscribe(
      (broadcast: any) => {
        this.gameStateService.gameState.set(broadcast.data)
        this.states.push(broadcast.data) // Assuming broadcast contains a 'data' property
        console.log('Received broadcast:', broadcast)
      },
      error => console.error('Broadcast error:', error),
    )

    this.userAssignmentSubscription = this.webSocketService.onPlayerAssignment().subscribe(
      (playerAssignment: any) => {
        console.log('Received Player Assignment', playerAssignment)
        this.userService.assignedCharacter.set(playerAssignment.character)
        this.num_players += 1
        console.log(`${this.num_players} is num players`)
        this.showStartButton = this.num_players >= 3
        this.startButtonMessage = `${this.num_players} joined. Click to start the game.`
      },
      error => console.error('Player Assignment error'),
    )

    this.startButtonSubscription = this.webSocketService.onShowStartButton().subscribe((data: any) => {
      console.log(data.message)
      this.startButtonMessage = data.message
      this.showStartButton = true;
    })

    // Subscribe to broadcast of when to display cards
    this.displayCardsSubscription = this.webSocketService.onDisplayCards().subscribe(
      (playerCards: any) => {
        console.log('Received Display Card Broadcast', playerCards)

        // Get the character assigned to the user
        const assignedCharacter = this.userService.assignedCharacter()

        // Find the matching character and their cards in the received data
        const matchedData = playerCards.data.find(
          (entry: [string, string[]]) => entry[0] === assignedCharacter,
        )

        // Set this.cards to the cards of the assigned character, or an empty array if not found
        this.cards = matchedData ? matchedData[1] : []
      },
      error => console.error('Display Cards Error'),
    )

    // Subscribe to Suggestion Made
    this.suggestionSubscription = this.webSocketService.onSuggestion().subscribe(
      (suggestion: any) => {
        console.log('Received Suggestion', suggestion)
        this.currentSuggestion = suggestion.data

        // If it is not your turn, show Modal popup  // TODO: what if player whos turn it wasn't made suggestion (i.e character moved there?) (Response below)
        // I don't think players are able to make suggestions outside of their turns right?
        if (
          this.gameStateService.gameState().current_player.name !==
          this.userService.assignedCharacter()
        ) {
          this.showDisproveModal = true
        }

        // if
        // (
        //   None
        // )

        // TODO: add logic here once complete

        // TODO: Once all closed disproval, send game state
      },
      error => console.error('Suggestion error'),
    )

    // Show disproves ONLY to player who's turn it is
    // Subscribe to Suggestion Made
    this.disproveSubscription = this.webSocketService.onDisproves().subscribe(
      (disproves: any) => {
        console.log('Received Disproves', disproves)

        disproves.data = disproves.data.filter((item: string) => item.trim() !== '')

        // Show popup only to person whose turn it is
        if (
          this.gameStateService.gameState().current_player.name ===
          this.userService.assignedCharacter()
        ) {
          if (disproves.data.length > 0) {
            this.dialog.closeAll()
            const message = 'The following items were disproved: \n' + disproves.data.join('\n')
            this.showMessage(message)
          } else {
            this.dialog.closeAll()
            const message = 'None of your guesses were disproved!'
            this.showMessage(message)
          }
        }
      },
      error => console.error('Suggestion error'),
    )

    // Subscribe to get move options when player chooses to move
    this.moveOptionSubscription = this.webSocketService.onMoveOptions().subscribe(
      (moveOptions: any) => {
        console.log('Received Move Options', moveOptions)
        console.log('Options', this.options)
        this.move_options = moveOptions
      },
      error => console.error('Move Option error'),
    )
  }

  ngOnDestroy() {
    // Unsubscribe to prevent memory leaks
    this.webSocketService.close()
  }
}
