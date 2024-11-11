import { Component, OnInit, OnDestroy } from '@angular/core';
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

  // @ViewChild('messageBox') messageBox!: ElementRef;

  messages: string[] = [];

  private socketSubscription!: Subscription;

  constructor(private webSocketService: WebSocketService) {}

  ngOnInit() {
  }

  ngOnDestroy() {
    // Unsubscribe to prevent memory leaks
    this.socketSubscription.unsubscribe();
    this.webSocketService.close();
  }

  // ngAfterViewChecked() {
  //   // Scroll to the bottom every time the view is updated
  //   this.scrollToBottom();
  // }

  // scrollToBottom() {
  //   const container = this.messageBox.nativeElement;
  //   container.scrollTop = container.scrollHeight;
  // }
}
