import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { PageLoadOverlayComponent } from './page-load-overlay.component';

describe('PageLoadOverlayComponent', () => {
  let component: PageLoadOverlayComponent;
  let fixture: ComponentFixture<PageLoadOverlayComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ PageLoadOverlayComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(PageLoadOverlayComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
