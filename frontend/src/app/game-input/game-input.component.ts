import { Component, OnInit, Input, inject, Output, EventEmitter } from '@angular/core'
import { ReactiveFormsModule } from '@angular/forms'
import { FormBuilder, FormGroup, Validators } from '@angular/forms'
import { CommonModule } from '@angular/common'
import { GameStateService } from '../game.state.service'
import { WebSocketService } from '../websocket.service'

@Component({
  selector: 'gameInput',
  standalone: true,
  imports: [ReactiveFormsModule, CommonModule],
  templateUrl: './game-input.component.html',
  styleUrl: './game-input.component.css',
})
export class GameInputComponent implements OnInit {
  @Output() showSpinnerDialog = new EventEmitter<boolean>(false)

  gameForm!: FormGroup

  gameStateService = inject(GameStateService)
  webSocketService = inject(WebSocketService)

  characters = [
    'Miss Scarlet',
    'Colonel Mustard',
    'Mrs. White',
    'Mr. Green',
    'Mrs. Peacock',
    'Professor Plum',
  ]
  weapons = ['Candlestick', 'Dagger', 'Revolver', 'Lead Pipe', 'Wrench', 'Rope']

  locations = [
    'Ballroom',
    'Billiard Room',
    'Conservatory',
    'Dining Room',
    'Hall',
    'Kitchen',
    'Library',
    'Lounge',
    'Study',
  ]

  constructor(private fb: FormBuilder) {}

  ngOnInit(): void {
    this.gameForm = this.fb.group({
      character: ['', Validators.required],
      weapon: ['', Validators.required],
      location: [''],
    })
  }

  gameState = this.gameStateService.gameState

  onSubmit(): void {
    if (this.gameForm.valid) {
      const formData = this.gameForm.value

      // If suggest, show wheel
      if (this.gameStateService.gameState().flow === 'suggest') {
        this.showSpinnerDialog.emit(true)
      }
      this.webSocketService.sendSuggestion(formData) // Send data to game
    } else {
      console.log('Form is invalid')
    }
  }

  goBack(): void {
    // Logic to go back to the previous game state
    console.log('Returning to the previous state...')
    this.webSocketService.sendGoBack()
  }
}
