import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SkewComponent } from './skew.component';

describe('SkewComponent', () => {
  let component: SkewComponent;
  let fixture: ComponentFixture<SkewComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SkewComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SkewComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
