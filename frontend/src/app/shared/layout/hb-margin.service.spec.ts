import { TestBed } from '@angular/core/testing';

import { HbMarginService } from './hb-margin.service';

describe('HbMarginService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: HbMarginService = TestBed.get(HbMarginService);
    expect(service).toBeTruthy();
  });
});
