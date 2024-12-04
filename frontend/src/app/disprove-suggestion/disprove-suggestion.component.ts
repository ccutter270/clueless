import { Component, inject, Inject, Input, Output, EventEmitter } from '@angular/core'
import { MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog'
import { CommonModule } from '@angular/common'
import { FormsModule } from '@angular/forms'
import { GameStateService } from '../game.state.service'
import { WebSocketService } from '../websocket.service'
import { UserService } from '../user.service'

export interface Suggestion {
  character: string
  location: string
  weapon: string
}

@Component({
  selector: 'DisproveSuggestion',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './disprove-suggestion.component.html',
  styleUrls: ['./disprove-suggestion.component.css'],
})
export class DisproveSuggestionComponent {
  @Input() suggestion: Suggestion = {
    character: '',
    location: '',
    weapon: '',
  }

  @Input() playerCards: string[] = []
  @Output() disproveCard = new EventEmitter<string>()
  @Output() closed = new EventEmitter<void>() // Notify when modal is closed
  isOpen: boolean = false
  cardsToDisprove: string[] = []
  webSocketService = inject(WebSocketService)

  ngOnChanges() {
    if (this.suggestion) {
      this.cardsToDisprove = this.playerCards.filter(card =>
        [this.suggestion?.character, this.suggestion?.location, this.suggestion?.weapon].includes(
          card,
        ),
      )
      this.isOpen = true
      // this.isOpen = this.cardsToDisprove.length > 0;
    }
  }

  onDisprove(card: string) {
    // Notify the parent that a card was used to disprove
    this.disproveCard.emit(card)
    this.isOpen = false
  }
}
