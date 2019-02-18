import { TestBed } from '@angular/core/testing';

import { ReferralLinksService } from './referral-links.service';

describe('ReferralLinksService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: ReferralLinksService = TestBed.get(ReferralLinksService);
    expect(service).toBeTruthy();
  });
});
