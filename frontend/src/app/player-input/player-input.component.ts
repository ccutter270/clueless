import { ChangeDetectorRef, EventEmitter, Output } from '@angular/core'
import { Component, Input, inject } from '@angular/core'
import { WebSocketService } from '../websocket.service'
import { CommonModule } from '@angular/common'
import { FormsModule } from '@angular/forms'
import { GameStateService } from '../game.state.service'
import { UserService } from '../user.service'

@Component({
  selector: 'playerInput',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './player-input.component.html',
  styleUrl: './player-input.component.css',
})
export class PlayerInputComponent {
  gameStateService = inject(GameStateService)
  webSocketService = inject(WebSocketService)
  userService = inject(UserService)
  cdr = inject(ChangeDetectorRef)

  sending: boolean = false
  @Input() options: string[] = []
  @Output() showSpinnerDialog = new EventEmitter<boolean>()

  gameState = this.gameStateService.gameState

  //TODO: Fix Suggestion logic here
  sendMessage(message: string) {
    if (message.trim()) {
      this.sending = true // Indicate message is being sent

      console.log('DEBUGGING< ACTION CHOSEN IS ')

      // Send message to the server
      this.webSocketService.sendPlayerAction({
        type: 'Action',
        character: this.userService.assignedCharacter(),
        location: 'Library',
        message: message,
      })

      if (message === 'suggest') {
        this.showSpinnerDialog.emit(true)
      }

      message = '' // Clear the input field after sending
      this.sending = false // Reset the sending status
      this.cdr.detectChanges()
    }
  }
}
