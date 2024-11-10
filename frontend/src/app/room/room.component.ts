import { Component, Input } from '@angular/core';

@Component({
  selector: 'room',
  standalone: true,
  imports: [],
  templateUrl: './room.component.html',
  styleUrl: './room.component.css'
})
export class RoomComponent {
 @Input() roomName: string = "";
 @Input() image: string = "";
//  @Input() players: string[] = [];

}
