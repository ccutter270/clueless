import { Component, OnInit, OnDestroy } from '@angular/core'
import { WebSocketService } from '../websocket.service'
import { Subscription } from 'rxjs'
import { CommonModule, NgFor } from '@angular/common'

@Component({
  selector: 'app-websocket-tester',
  standalone: true,
  imports: [CommonModule, NgFor],
  templateUrl: './websocket.tester.component.html',
  styleUrls: ['./websocket.tester.component.css'],
})
export class WebsocketTesterComponent implements OnInit, OnDestroy {
  messages: string[] = []
  private broadcastSubscription!: Subscription

  constructor(private webSocketService: WebSocketService) {}

  ngOnInit() {
    // Send initial ping to server to start broadcasts
    this.webSocketService.pingForBroadcast()
    console.log('Sent broadcast request to server')

    // Subscribe to broadcast messages from the server
    this.broadcastSubscription = this.webSocketService.onBroadcast().subscribe(
      (broadcast: any) => {
        this.messages.push(broadcast.data) // Assuming broadcast contains a 'data' property
        console.log('Received broadcast:', broadcast)
      },
      error => console.error('Broadcast error:', error),
    )
  }

  ngOnDestroy() {
    // Unsubscribe to prevent memory leaks
    this.broadcastSubscription.unsubscribe()
    this.webSocketService.close()
  }
}
