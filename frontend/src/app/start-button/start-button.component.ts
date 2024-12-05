import { Component, EventEmitter, inject, Input, Output } from '@angular/core'
import { CommonModule } from '@angular/common'
import { WebSocketService } from '../websocket.service'

@Component({
  selector: 'StartButton',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './start-button.component.html',
  styleUrl: './start-button.component.css',
})
export class StartButtonComponent {
  webSocketService = inject(WebSocketService)
  @Input() showStartButton: boolean = false
  @Input() startButtonMessage: string = ''
  @Input() isGameStarting: boolean = false
  @Output() startGameClicked: EventEmitter<void> = new EventEmitter()

  onStartGame() {
    this.isGameStarting = true
    this.showStartButton = false
    this.webSocketService.sendStartGame()
  }
}
