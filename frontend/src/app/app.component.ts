import { Component } from '@angular/core';
import { Router, ActivatedRoute, NavigationEnd } from '@angular/router';
import { filter, map, flatMap } from 'rxjs/operators';

// import { RootClassesService } from './shared/root-classes.service';
// import { PortalModalService } from './portal/portal-modal.service';

@Component({
	selector: 'gp-root',
	templateUrl: './app.component.html',
	styleUrls: ['./app.component.scss']
})
export class AppComponent {

	contentClasses: string[];
	portalState: string;
	registeredUser: {
		userID: number,
		username: string,
		email: string
	};

	constructor(
		private router: Router,
		private activatedRoute: ActivatedRoute,
		// private rootClassesService: RootClassesService,
		// private portalModalService: PortalModalService,
	) {
		// this.portalModalService.getState().subscribe(state => this.portalState = state);
	}

	ngOnInit() {
		this.router.events.pipe(
			filter(event => event instanceof NavigationEnd),
			map(() => this.activatedRoute),
			map((route) => {
				while (route.firstChild) {
					route = route.firstChild;
				}
				return route;
			}),
			flatMap(route => route.data),
		).subscribe(data => {
			this.contentClasses = data['contentClasses'] ? data['contentClasses'] : [];
			if (data['headerSize'] === 'large') {
				this.contentClasses.push('largeHeader');
			}
		})
	}

	userRegistered(user) {
		this.portalState = 'registerSuccess';
		this.registeredUser = user;
	}

	userLoggedIn(success: boolean) {
		if (success) {
			// this.portalModalService.closePortal();
		}
	}

}
