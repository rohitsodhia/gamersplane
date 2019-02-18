import { Injectable } from '@angular/core';
import { Observable, of as ObservableOf } from 'rxjs';
import { map } from 'rxjs/operators';

import { ApiService } from './api.service';

import { System } from './System.class';

@Injectable({
	providedIn: 'root'
})
export class SystemService {

	private systems: System[] = []

	constructor(
		private api: ApiService
	) { }

	get(systems?: string[], options?: OptionsGetSystems): Observable<System[]> {
		if (
			this.systems.length === 0 ||
			systems !== undefined && (
				systems.some((system) => !this.systems.find((eSystem) => system === eSystem._id)) ||
				systems.some((system) => this.systems.find((eSystem) => system === eSystem._id).publisher === undefined)
			)
		) {
			if (options === undefined) {
				options = {};
			}
			if (systems === undefined || systems.length === 0) {
				options['all'] = true;
			} else {
				options['systems'] = systems.join(',');
			}
			return this.api.get('/systems', options).pipe(
				map(response => {
					if (response['success']) {
						for (let system in response['systems']) {
							this.systems[system] = response['systems'][system];
						}
						return response['systems'];
					} else {
						return {};
					}
				})
			)
		} else {
			return ObservableOf(this.systems);
		}
	}

	initLoad() {
		return this.get([], {
			basic: true
		})
			.toPromise()
			.then(() => true)
			.catch(error => console.log(error));
	}

}

interface OptionsGetSystems {
	all?: boolean;
	systems?: string;
	basic?: boolean;
}