import { Injectable } from '@angular/core';
import { io, Socket } from 'socket.io-client';
import { Observable } from 'rxjs';
import { Action } from '../models/action.model';

@Injectable({
  providedIn: 'root',
})
export class WebSocketService {
  private socket: Socket;

  constructor() {
    // Replace with your server's URL
    this.socket = io('http://localhost:5000');  // Ensure this matches your Flask server URL and port
  }

  // Observable for incoming 'game_state' events
  onMessage(): Observable<any> {
    return new Observable((observer) => {
      this.socket.on('game_state', (data) => observer.next(data));
    });
  }

  // Method to send messages to the server
  sendPlayerAction(action: Action) {
    this.socket.emit('player_action', action);
  }

  // Method to close the socket connection
  close() {
    if (this.socket) {
      this.socket.disconnect();
    }
  }
}
