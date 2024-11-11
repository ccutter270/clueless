import { Component, OnInit, OnDestroy, Input } from '@angular/core';
import { CommonModule, NgFor } from '@angular/common';
import { GameState } from '../../models/game.state.model';

@Component({
  selector: 'gameState',
  standalone: true,
  imports: [CommonModule, NgFor],
  templateUrl: './game-state.component.html',
  styleUrl: './game-state.component.css'
})
export class GameStateComponent {
  @Input() states: GameState[] = [];
}
