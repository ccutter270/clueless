import { ComponentFixture, TestBed } from '@angular/core/testing'

import { AccusePromptComponent } from './accuse-prompt.component'

describe('AccusePromptComponent', () => {
  let component: AccusePromptComponent
  let fixture: ComponentFixture<AccusePromptComponent>

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [AccusePromptComponent],
    }).compileComponents()

    fixture = TestBed.createComponent(AccusePromptComponent)
    component = fixture.componentInstance
    fixture.detectChanges()
  })

  it('should create', () => {
    expect(component).toBeTruthy()
  })
})
