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
    this.socket = io('http://localhost:5000'); // Update to match your Flask server URL and port
  }

  // Method to emit a ping event to the server
  pingForBroadcast() {
    this.socket.emit('player_connected');
  }

  // Observable for listening to broadcasts from the server
  onBroadcast(): Observable<any> {
    return new Observable((observer) => {
      this.socket.on('game_state', (data) => observer.next(data));
    });
  }

  sendPlayerAction(action: Action) {
    console.log("sending player action")
    this.socket.emit("player_action", action)
  }

  // Method to close the socket connection
  close() {
    if (this.socket) {
      this.socket.disconnect();
    }
  }
}
