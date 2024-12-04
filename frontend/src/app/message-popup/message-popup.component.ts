import { Component, Input, Output, EventEmitter } from '@angular/core'
import { CommonModule } from '@angular/common'
import { FormsModule } from '@angular/forms'

@Component({
  selector: 'GeneralMessagePopup',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './message-popup.component.html',
  styleUrls: ['./message-popup.component.css'],
})
export class GeneralMessagePopupComponent {
  @Input() message: string = '' // Message to display in the popup
  @Input() isOpen: boolean = false // Whether the popup is visible
  @Output() closePopup = new EventEmitter<void>() // Event emitted when the popup is closed

  close() {
    this.isOpen = false
    this.closePopup.emit()
  }
}
