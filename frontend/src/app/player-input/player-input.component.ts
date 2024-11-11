import { Component, Input, inject } from '@angular/core';
import { WebSocketService } from '../websocket.service';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { GameStateService } from '../game.state.service';
import { UserService } from '../user.service';


@Component({
  selector: 'playerInput',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './player-input.component.html',
  styleUrl: './player-input.component.css'
})
export class PlayerInputComponent {

  gameStateService = inject(GameStateService);
  webSocketService = inject(WebSocketService);
  userService = inject(UserService);

  sending: boolean = false;
  @Input() options: string[] = [];

  gameState = this.gameStateService.gameState();

  sendMessage(message: string) {
    if (message.trim()) {
      this.sending = true; // Indicate message is being sent
      // Send message to the server
      this.webSocketService.sendPlayerAction({
        type: "Action",
        character: "Professor Plum",
        location: "Library",
        message: "Hello"
      });
      message = ''; // Clear the input field after sending
      this.sending = false; // Reset the sending status
    }
  }
}
