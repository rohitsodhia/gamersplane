import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

import { ApiService } from './api.service';

import { ReferralLink } from './referral-link.interface';
import { ReferralLinksGetApiResponse } from './referral-links-get-api-request.interface';

@Injectable({
	providedIn: 'root'
})
export class ReferralLinksService {

	constructor(
		private api: ApiService
	) { }

	get(): Observable<ReferralLink[]> {
		return this.api.get<ReferralLinksGetApiResponse>('/referralLinks')
			.pipe(
				map(response => {
					if (response.data) {
						return response.data.referralLinks;
					} else {
						return [];
					}
				})
			);
	}

}
