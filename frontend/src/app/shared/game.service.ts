import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

import { ApiService } from './api.service';

@Injectable({
	providedIn: 'root'
})
export class GameService {

	constructor(
		private api: ApiService
	) { }

	get(options: OptionsGetGames): Observable<{}> {
		return this.api.get('/games', options);
	}

}

interface OptionsGetGames {
	system?: string;
	orderBy?: string;
	orderByDir?: string;
	limit?: number;
	fields?: string;
}