import { TestBed } from '@angular/core/testing';

import { PageLoadOverlayService } from './page-load-overlay.service';

describe('PageLoadOverlayService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: PageLoadOverlayService = TestBed.get(PageLoadOverlayService);
    expect(service).toBeTruthy();
  });
});
