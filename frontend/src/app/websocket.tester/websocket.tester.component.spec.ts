import { ComponentFixture, TestBed } from '@angular/core/testing'

import { WebsocketTesterComponent } from './websocket.tester.component'

describe('WebsocketTesterComponent', () => {
  let component: WebsocketTesterComponent
  let fixture: ComponentFixture<WebsocketTesterComponent>

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [WebsocketTesterComponent],
    }).compileComponents()

    fixture = TestBed.createComponent(WebsocketTesterComponent)
    component = fixture.componentInstance
    fixture.detectChanges()
  })

  it('should create', () => {
    expect(component).toBeTruthy()
  })
})
