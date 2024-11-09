import { Component, OnInit, OnDestroy  } from '@angular/core';
import { WebSocketService } from '../websocket.service';
import { Subscription } from 'rxjs';
import { CommonModule, NgFor } from '@angular/common';

@Component({
  selector: 'gameState',
  standalone: true,
  // providers: [WebSocketService],
  imports: [CommonModule, NgFor],
  templateUrl: './game-state.component.html',
  styleUrl: './game-state.component.css'
})
export class GameStateComponent implements OnInit, OnDestroy {

  messages: string[] = [];
  private socketSubscription!: Subscription;

  constructor(private webSocketService: WebSocketService) {}

  ngOnInit() {
    // Subscribe to incoming messages
    this.socketSubscription = this.webSocketService.onMessage().subscribe(
      (message: any) => {
        this.messages.push(message);
        console.log('Received message:', message);
      },
      (error) => console.error('WebSocket error:', error)
    );
  }

  ngOnDestroy() {
    // Unsubscribe to prevent memory leaks
    this.socketSubscription.unsubscribe();
    this.webSocketService.close();
  }
}
