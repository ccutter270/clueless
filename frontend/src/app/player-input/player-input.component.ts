import { Component } from '@angular/core';
import { WebSocketService } from '../websocket.service';
// import { Subscription } from 'rxjs';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms'; 


@Component({
  selector: 'playerInput',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './player-input.component.html',
  styleUrl: './player-input.component.css'
})
export class PlayerInputComponent {

    message: string = '';
    sending: boolean = false;

    constructor(private webSocketService: WebSocketService) {}

    sendMessage() {
      if (this.message.trim()) {
        this.sending = true; // Indicate message is being sent
        // Send message to the server
        this.webSocketService.sendMessage(this.message);
        this.message = ''; // Clear the input field after sending
        this.sending = false; // Reset the sending status
      }
    }

}
