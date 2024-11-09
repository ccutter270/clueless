import { Injectable } from '@angular/core';
import { io, Socket } from 'socket.io-client';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class WebSocketService {
  private socket: Socket;

  constructor() {
    // Replace with your server's URL
    this.socket = io('http://localhost:5000');
  }

  // Observable for incoming messages
  onMessage(): Observable<any> {
    console.log('Subscribed to message!')
    return new Observable((observer) => {
      this.socket.on('message', (data) => observer.next(data));
      this.socket.on('connect_error', (error) => observer.error(error));
    });
  }

  // Method to send messages to the server
  sendMessage(message: string) {
    this.socket.emit('message', message);
  }

  // Method to close the socket connection
  close() {
    if (this.socket) {
      this.socket.disconnect();
    }
  }
}
