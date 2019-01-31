import { TestBed, inject } from '@angular/core/testing';

import { ScreenWidthService } from './screen-width.service';

describe('ScreenWidthService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [ScreenWidthService]
    });
  });

  it('should be created', inject([ScreenWidthService], (service: ScreenWidthService) => {
    expect(service).toBeTruthy();
  }));
});
