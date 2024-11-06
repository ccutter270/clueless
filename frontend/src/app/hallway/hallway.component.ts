import { Component, Input } from '@angular/core';

@Component({
  selector: 'hallway',
  standalone: true,
  imports: [],
  templateUrl: './hallway.component.html',
  styleUrl: './hallway.component.css'
})
export class HallwayComponent {
  @Input() hallName: string = "";
  @Input() imageURL: string ="";
}
