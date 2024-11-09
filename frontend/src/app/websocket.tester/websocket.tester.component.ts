import { Component, OnInit, OnDestroy } from '@angular/core';
import { WebSocketService } from '../websocket.service';
import { Subscription } from 'rxjs';
import { CommonModule, NgFor } from '@angular/common';

@Component({
  selector: 'app-websocket-tester',
  standalone: true,
  imports: [CommonModule, NgFor],
  providers: [WebSocketService],
  templateUrl: './websocket.tester.component.html',
  styleUrls: ['./websocket.tester.component.css'],
})
export class WebsocketTesterComponent implements OnInit, OnDestroy {
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

  // Method to send a message to the server
  sendMessage() {
    this.webSocketService.sendMessage('Hello, Server!');
  }

  ngOnDestroy() {
    // Unsubscribe to prevent memory leaks
    this.socketSubscription.unsubscribe();
    this.webSocketService.close();
  }
}
