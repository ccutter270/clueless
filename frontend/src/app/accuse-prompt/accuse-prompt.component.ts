import { ChangeDetectorRef, EventEmitter, Output } from '@angular/core'
import { Component, Input, inject } from '@angular/core'
import { WebSocketService } from '../websocket.service'
import { CommonModule } from '@angular/common'
import { FormsModule } from '@angular/forms'
import { GameStateService } from '../game.state.service'
import { UserService } from '../user.service'

@Component({
  selector: 'AccusePrompt',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './accuse-prompt.component.html',
  styleUrl: './accuse-prompt.component.css'
})
export class AccusePromptComponent {
  gameStateService = inject(GameStateService)
  webSocketService = inject(WebSocketService)
  userService = inject(UserService)
  cdr = inject(ChangeDetectorRef)

  sending: boolean = false
  @Input() options: string[] = []

  gameState = this.gameStateService.gameState

  sendMessage(message: string) {
    if (message.trim()) {
      this.sending = true // Indicate message is being sent

      // Send message to the server
      this.webSocketService.sendPlayerAction({
        type: 'Action',
        character: this.userService.assignedCharacter(),
        location: '',
        message: message,
      })

      message = '' // Clear the input field after sending
      this.sending = false // Reset the sending status
    }
  }
}
