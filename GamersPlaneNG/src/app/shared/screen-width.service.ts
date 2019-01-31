import { Injectable } from '@angular/core';
import { Observable, fromEvent } from 'rxjs';
import { map, publishBehavior, refCount } from 'rxjs/operators';

@Injectable({
	providedIn: 'root'
})
export class ScreenWidthService {

	private screenWidth$: Observable<number>;

	constructor() {
		this.screenWidth$ = fromEvent<Event>(window, 'resize').pipe(
			map(event => event.target['innerWidth']),
			publishBehavior(window.innerWidth),
			refCount()
		)
	}

	get() {
		return this.screenWidth$;
	}

}
