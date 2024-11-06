import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { RoomComponent } from "./room/room.component";
import { HallwayComponent } from "./hallway/hallway.component";
import { EmptyComponent } from './empty/empty.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, RoomComponent, HallwayComponent, EmptyComponent, CommonModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'Clue';
  Areas = [
    {name: "Study", type: "room", photo: "C:\\Users\\ldgri\\Documents\\Courses\\JHU\\Software Engineering Foundations\\Group Project\\Clue\\public\\study.jpg"},
    {name: "Study to Hall", type: "hall", photo: "C:\Users\ldgri\Documents\Courses\JHU\Software Engineering Foundations\Group Project\Clue\public\hallway.jpg"},
    {name: "Hall", type: "room", photo: "C:\Users\ldgri\Documents\Courses\JHU\Software Engineering Foundations\Group Project\Clue\public\hall.jpg"},
    {name: "Hall to Lounge", type: "hall", photo: "C:\Users\ldgri\Documents\Courses\JHU\Software Engineering Foundations\Group Project\Clue\public\hallway.jpg"},
    {name: "Lounge", type: "room", photo: "C:\Users\ldgri\Documents\Courses\JHU\Software Engineering Foundations\Group Project\Clue\public\lounge.jpg"},
    {name: "Study to Library", type: "hall", photo: "C:\Users\ldgri\Documents\Courses\JHU\Software Engineering Foundations\Group Project\Clue\public\hallway.jpg"},
    {name: "top left", type: "empty"},
    {name: "Hall to Billiard", type: "hall", photo: "C:\Users\ldgri\Documents\Courses\JHU\Software Engineering Foundations\Group Project\Clue\public\hallway.jpg"},
    {name: "top right", type: "empty"},
    {name: "Lounge to Dining", type: "hall", photo: "C:\Users\ldgri\Documents\Courses\JHU\Software Engineering Foundations\Group Project\Clue\public\hallway.jpg"},
    {name: "Library", type: "room", photo: "C:\Users\ldgri\Documents\Courses\JHU\Software Engineering Foundations\Group Project\Clue\public\library.jpg"},
    {name: "Library to Billiard", type: "hall", photo: "C:\Users\ldgri\Documents\Courses\JHU\Software Engineering Foundations\Group Project\Clue\public\hallway.jpg"},
    {name: "Billiard Room", type: "room", photo: "C:\Users\ldgri\Documents\Courses\JHU\Software Engineering Foundations\Group Project\Clue\public\billiard.jpg"},
    {name: "Billiard to Dining", type: "hall", photo: "C:\Users\ldgri\Documents\Courses\JHU\Software Engineering Foundations\Group Project\Clue\public\hallway.jpg"},
    {name: "Dining Room", type: "room", photo: "C:\Users\ldgri\Documents\Courses\JHU\Software Engineering Foundations\Group Project\Clue\public\dining.jpg"},
    {name: "Library to Conservatory", type: "hall", photo: "C:\Users\ldgri\Documents\Courses\JHU\Software Engineering Foundations\Group Project\Clue\public\hallway.jpg"},
    {name: "bottom left", type: "empty"}, 
    {name: "Billiard to Ball", type: "hall", photo: "C:\Users\ldgri\Documents\Courses\JHU\Software Engineering Foundations\Group Project\Clue\public\hallway.jpg"}, 
    {name: "bottom right", type: "empty"}, 
    {name: "Dining to Kitchen", type: "hall", photo: "C:\Users\ldgri\Documents\Courses\JHU\Software Engineering Foundations\Group Project\Clue\public\hallway.jpg"}, 
    {name: "Conservatory", type: "room", photo: "C:\Users\ldgri\Documents\Courses\JHU\Software Engineering Foundations\Group Project\Clue\public\conservatory.jpg"},
    {name: "Conservatory to Ball", type: "hall", photo: "C:\Users\ldgri\Documents\Courses\JHU\Software Engineering Foundations\Group Project\Clue\public\hallway.jpg"},
    {name: "Ball-Room", type: "room", photo: "C:\Users\ldgri\Documents\Courses\JHU\Software Engineering Foundations\Group Project\Clue\public\ball.jpg"},
    {name: "Ball to Kitchen", type: "hall", photo: "C:\Users\ldgri\Documents\Courses\JHU\Software Engineering Foundations\Group Project\Clue\public\hallway.jpg"},
    {name: "Kitchen", type: "room", photo: "C:\Users\ldgri\Documents\Courses\JHU\Software Engineering Foundations\Group Project\Clue\public\kitchen.jpg"},
  ]
}
