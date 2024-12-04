import { CommonModule } from '@angular/common'
import { Component } from '@angular/core'
import { FormsModule } from '@angular/forms'

@Component({
  selector: 'trackingCard',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './tracking-card.component.html',
  styleUrl: './tracking-card.component.css',
})
export class TrackingCardComponent {
  characters = [
    { name: 'Miss Scarlet', isChecked: false },
    { name: 'Professor Plum', isChecked: false },
    { name: 'Mrs. Peacock', isChecked: false },
    { name: 'Mr. Green', isChecked: false },
    { name: 'Colonel Mustard', isChecked: false },
    { name: 'Mrs. White', isChecked: false },
  ]

  weapons = [
    { name: 'Knife', isChecked: false },
    { name: 'Candlestick', isChecked: false },
    { name: 'Revolver', isChecked: false },
    { name: 'Rope', isChecked: false },
    { name: 'Lead Pipe', isChecked: false },
    { name: 'Wrench', isChecked: false },
  ]

  rooms = [
    { name: 'Kitchen', isChecked: false },
    { name: 'Ballroom', isChecked: false },
    { name: 'Conservatory', isChecked: false },
    { name: 'Dining Room', isChecked: false },
    { name: 'Library', isChecked: false },
    { name: 'Billiard Room', isChecked: false },
    { name: 'Lounge', isChecked: false },
    { name: 'Hall', isChecked: false },
    { name: 'Study', isChecked: false },
  ]
}
