import { NgIf } from '@angular/common';
import { Component, inject, Input } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';
import { MatDialogActions, MatDialogClose, MatDialogTitle, MatDialogContent, MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner';

@Component({
  selector: 'app-material-dialog',
  standalone: true,
  imports: [MatButtonModule, MatDialogTitle, MatDialogContent, MatProgressSpinnerModule, NgIf],
  templateUrl: './material-dialog.component.html',
  styleUrl: './material-dialog.component.css'
})
export class MaterialDialogComponent {
  readonly dialogRef = inject(MatDialogRef<MaterialDialogComponent>);

  data = inject(MAT_DIALOG_DATA);
}
