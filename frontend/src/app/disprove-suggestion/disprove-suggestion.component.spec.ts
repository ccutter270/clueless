import { ComponentFixture, TestBed } from '@angular/core/testing'

import { DisproveSuggestionComponent } from './disprove-suggestion.component'

describe('DisproveSuggestionComponent', () => {
  let component: DisproveSuggestionComponent
  let fixture: ComponentFixture<DisproveSuggestionComponent>

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [DisproveSuggestionComponent],
    }).compileComponents()

    fixture = TestBed.createComponent(DisproveSuggestionComponent)
    component = fixture.componentInstance
    fixture.detectChanges()
  })

  it('should create', () => {
    expect(component).toBeTruthy()
  })
})
