import { Component, OnInit, OnDestroy } from '@angular/core';
import { WebSocketService } from '../websocket.service';
import { Subscription } from 'rxjs';
import { CommonModule, NgFor } from '@angular/common';

@Component({
  selector: 'app-websocket-tester',
  standalone: true,
  imports: [CommonModule, NgFor],
  templateUrl: './websocket.tester.component.html',
  styleUrls: ['./websocket.tester.component.css'],
})
export class WebsocketTesterComponent implements OnInit, OnDestroy {
  messages: string[] = [];
  private socketSubscription!: Subscription;
  private customEventSubscription!: Subscription;

  constructor(private webSocketService: WebSocketService) { }

  ngOnInit() {
    // Subscribe to 'game_state' events
    this.socketSubscription = this.webSocketService.onMessage().subscribe(
      (message: any) => {
        this.messages.push(message);
        console.log('Received message:', message);
      },
      (error) => console.error('WebSocket error:', error)
    );
  }

  // Method to send a message to the server
  sendMessage() {
    this.webSocketService.sendPlayerAction({
      type: "Action",
      message: "Someone moved somewhere."
    });
  }

  ngOnDestroy() {
    // Unsubscribe to prevent memory leaks
    this.socketSubscription.unsubscribe();
    this.customEventSubscription.unsubscribe();
    this.webSocketService.close();
  }
}
