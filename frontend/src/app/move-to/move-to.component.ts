import { ChangeDetectorRef } from '@angular/core'
import { Component, Input, inject } from '@angular/core'
import { WebSocketService } from '../websocket.service'
import { CommonModule } from '@angular/common'
import { FormsModule } from '@angular/forms'
import { GameStateService } from '../game.state.service'
import { UserService } from '../user.service'

@Component({
  selector: 'moveTo',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './move-to.component.html',
  styleUrl: './move-to.component.css',
})
export class MoveToComponent {
  gameStateService = inject(GameStateService)
  webSocketService = inject(WebSocketService)
  userService = inject(UserService)

  sending: boolean = false
  @Input() move_options: string[] = []

  gameState = this.gameStateService.gameState

  SendLocation(message: string) {
    if (message.trim()) {
      this.sending = true // Indicate message is being sent

      // Send message to the server
      this.webSocketService.sendMoveLocation(message)
      message = '' // Clear the input field after sending
      this.sending = false // Reset the sending status
    }
  }
}
