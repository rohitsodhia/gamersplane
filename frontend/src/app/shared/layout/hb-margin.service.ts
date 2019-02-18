import { Injectable } from '@angular/core';

import { BehaviorSubject } from 'rxjs';

@Injectable({
	providedIn: 'root'
})
export class HbMarginService {

	private groups: { [key: string]: BehaviorSubject<number> } = {};

	constructor() { }

	set(width: number, key: string = 'hb') {
		if (key in this.groups) {
			this.groups[key].next(width);
		} else {
			this.groups[key] = new BehaviorSubject(width);
		}
	}

	watch(key: string) {
		if (!(key in this.groups)) {
			this.groups[key] = new BehaviorSubject(0);
		}
		return this.groups[key].asObservable();
	}

}
