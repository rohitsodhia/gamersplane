import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable } from 'rxjs';

@Injectable({
	providedIn: 'root'
})
export class PageLoadOverlayService {

	visibleSubject: BehaviorSubject<boolean> = new BehaviorSubject(false);

	constructor() { }

	showOverlay() {
		this.visibleSubject.next(true);
	}

	hideOverlay() {
		this.visibleSubject.next(false);
	}

	getOverlayVisiblity(): Observable<boolean> {
		return this.visibleSubject.asObservable();
	}

}
