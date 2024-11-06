import { ComponentFixture, TestBed } from '@angular/core/testing';

import { HallwayComponent } from './hallway.component';

describe('HallwayComponent', () => {
  let component: HallwayComponent;
  let fixture: ComponentFixture<HallwayComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [HallwayComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(HallwayComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
