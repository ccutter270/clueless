import {
  Component,
  OnInit,
  OnDestroy,
  Input,
  ViewChild,
  ElementRef,
  AfterViewChecked,
} from '@angular/core'
import { CommonModule, NgFor } from '@angular/common'
import { GameState } from '../../models/game.state.model'

@Component({
  selector: 'gameState',
  standalone: true,
  imports: [CommonModule, NgFor],
  templateUrl: './game-state.component.html',
  styleUrls: ['./game-state.component.css'], // Note: Use "styleUrls" instead of "styleUrl"
})
export class GameStateComponent implements AfterViewChecked {
  @Input() states: GameState[] = []
  @ViewChild('messageBox') private messageBox!: ElementRef

  ngAfterViewChecked(): void {
    this.scrollToBottom() // Call scrollToBottom after view is checked
  }

  // Method to scroll the container to the bottom
  private scrollToBottom(): void {
    const box = this.messageBox.nativeElement
    box.scrollTop = box.scrollHeight
  }
}
