import { Component, OnInit } from '@angular/core';
import { ReactiveFormsModule } from '@angular/forms';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'gameInput',
  standalone: true,
  imports: [ReactiveFormsModule, CommonModule],
  templateUrl: './game-input.component.html',
  styleUrl: './game-input.component.css'
})


export class GameInputComponent implements OnInit{

  gameForm!: FormGroup;

  characters = ['Miss Scarlet', 'Col. Mustard', 'Mrs. White', 'Mr. Green', 'Mrs. Peacock', 'Prof. Plum'];
  rooms = ['Study', 'Hall', 'Lounge', 'Library', 'Billiard Room', 'Dining Room', 'Conservatory', 'Ball-Room', 'Kitchen'];
  weapons = ['Candlestick', 'Dagger', 'Revolver', 'Lead Pipe', 'Wrench', 'Rope'];

  constructor(private fb: FormBuilder) {}

  ngOnInit(): void {
    this.gameForm = this.fb.group({
      character: ['', Validators.required],
      room: ['', Validators.required],
      weapon: ['', Validators.required]
    });
  }

  onSubmit(): void {
    if (this.gameForm.valid) {
      const formData = this.gameForm.value;
      console.log('Form Data:', formData);

      // process form data and send to server
    } else {
      console.log('Form is invalid');
    }
  }
}
