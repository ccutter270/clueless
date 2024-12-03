import { ChangeDetectorRef } from '@angular/core';
import { Component, Input, inject } from '@angular/core';
import { WebSocketService } from '../websocket.service';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { GameStateService } from '../game.state.service';
import { UserService } from '../user.service';


@Component({
  selector: 'DisplayCard',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './display-cards.component.html',
  styleUrl: './display-cards.component.css'
})
export class DisplayCardComponent {

  gameStateService = inject(GameStateService);
  webSocketService = inject(WebSocketService);
  userService = inject(UserService);

  sending: boolean = false;
  @Input() cards: string[] = [];

  gameState = this.gameStateService.gameState;
  
}