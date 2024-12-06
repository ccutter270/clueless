import { Injectable } from '@angular/core'
import { io, Socket } from 'socket.io-client'
import { Observable } from 'rxjs'
import { Action } from '../models/action.model'

@Injectable({
  providedIn: 'root',
})
export class WebSocketService {
  private socket: Socket

  constructor() {
    // Replace with your server's URL
    this.socket = io('http://localhost:5000') // Update to match your Flask server URL and port
  }

  // Method to emit a ping event to the server
  pingForBroadcast() {
    this.socket.emit('player_connected')
  }

  // Observable for listening to broadcasts from the server
  onBroadcast(): Observable<any> {
    return new Observable(observer => {
      this.socket.on('game_state', data => observer.next(data))
    })
  }

  onPlayerAssignment(): Observable<any> {
    return new Observable(observer => {
      this.socket.on('character_assignment', data => observer.next(data))
    })
  }

  onError(): Observable<any> {
    return new Observable(observer => {
      this.socket.on('game_error', data => observer.next(data))
    })
  }

  onShowStartButton(): Observable<any> {
    return new Observable(observer => {
      this.socket.on('show_start_button', data => observer.next(data))
    })
  }
  // Observable looking for signal to display cards
  onDisplayCards(): Observable<any> {
    return new Observable(observer => {
      this.socket.on('display_cards', data => observer.next(data))
    })
  }

  // Observable looking for signal of suggestion
  onSuggestion(): Observable<any> {
    return new Observable(observer => {
      this.socket.on('suggestion_made', data => observer.next(data))
    })
  }

  // Observable looking for signal of disproves to display
  onDisproves(): Observable<any> {
    return new Observable(observer => {
      this.socket.on('show_disproves', data => observer.next(data))
    })
  }

  // Observable looking for signal of game over
  onGameOver(): Observable<any> {
    return new Observable(observer => {
      this.socket.on('game_over', data => observer.next(data))
    })
  }

  // Observable looking for signal of player lost
  onPlayerLost(): Observable<any> {
    return new Observable(observer => {
      this.socket.on('player_lost', data => observer.next(data))
    })
  }

  // Observable looking for move options for user
  onMoveOptions(): Observable<any> {
    return new Observable(observer => {
      this.socket.on('move_options', data => observer.next(data))
    })
  }

  sendStartGame() {
    console.log('starting game')
    this.socket.emit('start_game')
  }

  sendPlayerAction(action: Action) {
    console.log('sending player action')
    this.socket.emit('player_action', action)
  }

  sendMoveLocation(location: string) {
    console.log('sending move location')
    this.socket.emit('player_move_location', location)
  }

  // Send suggestion from UI once form is submitted
  sendSuggestion(suggestion: object) {
    console.log('sending player suggestion')
    this.socket.emit('player_suggestion', suggestion)
  }

  sendDisprove(disprove: string) {
    console.log('sending disprove')
    this.socket.emit('disprove', disprove)
  }

  // Send game over
  sendGameOver() {
    console.log('Sending Game Over')
    this.socket.emit('game_over')
  }

  // Method to close the socket connection
  close() {
    if (this.socket) {
      this.socket.disconnect()
    }
  }
}
