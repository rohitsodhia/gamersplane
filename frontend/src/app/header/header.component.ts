import { Component, OnInit, HostListener } from '@angular/core';
import { Router, NavigationEnd, ActivatedRoute } from '@angular/router';
import { Observable } from 'rxjs';
import { filter, map, flatMap } from 'rxjs/operators';
import { Store } from '@ngrx/store';

import { State } from '../shared/root-store/root-store.state'
// import { Logout } from '../store/current-user-store/current-user/current-user.actions';
// import { selectCurrentUser } from '../store/current-user-store/current-user/current-user.selectors';

import { ScreenWidthService } from '../shared/screen-width.service';
// import { PortalModalService } from 'src/app/portal/portal-modal.service';
// import { PMService } from 'src/app/pms/pm.service';

import { slideHeight } from '../shared/animations';
import { User } from '../shared/User.class';

@Component({
	selector: 'gp-header',
	templateUrl: './header.component.html',
	styleUrls: ['./header.component.scss'],
	animations: [
		slideHeight('.5s')
	]
})
export class HeaderComponent implements OnInit {

	headerSize: string = 'standard';
	private defaultSize: string = 'standard';
	currentUser$: Observable<User>;
	loggedIn: boolean = false;
	pmCount$: Observable<number>;
	menu: MenuItem[] = [
		{
			'label': 'Tools',
			'link': '/tools',
			'loggedIn': false,
			// 'children': [
			// 	{
			// 		'label': 'Dice',
			// 		'link': '/tools/dice',
			// 	},
			// 	{
			// 		'label': 'Cards',
			// 		'link': '/tools/cards',
			// 	},
			// 	{
			// 		'label': 'Music',
			// 		'link': '/tools/music',
			// 	}
			// ]
		},
		{
			'label': 'Systems',
			'link': '/systems',
			'loggedIn': false,
		},
		{
			'label': 'Characters',
			'link': '/characters',
			'loggedIn': false,
		},
		{
			'label': 'Games',
			'link': '/games',
			'loggedIn': false,
		},
		{
			'label': 'Forums',
			'link': '/forums',
			'loggedIn': false,
		},
		{
			'label': 'The Gamers',
			'link': '/gamers',
			'loggedIn': true,
		},
		{
			'label': 'Links',
			'link': '/links',
			'loggedIn': false,
		}
	];
	toggleHeight: { [key: string]: 'open' | 'closed' } = {
		tools: 'closed',
		user: 'closed'
	};
	private currentlyOpen: { menu: any, target: any } = { menu: null, target: null };
	screenWidth$: Observable<number>;
	mobileOpen: boolean = false;

	constructor (
		private router: Router,
		private activatedRoute: ActivatedRoute,
		private store: Store<State>,
		private screenWidthService: ScreenWidthService,
		// private portalModalService: PortalModalService,
		// private pmService: PMService
	) { }

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
			flatMap(route => route.data)
		).subscribe(data => {
			this.headerSize = data['headerSize'] ? data['headerSize'] : 'standard';
			this.defaultSize = this.headerSize;
		});

		this.screenWidth$ = this.screenWidthService.get();
		this.screenWidth$.subscribe((width) => {
			this.headerSize = (width > 767) ? this.defaultSize : 'standard';
			if (width < 1024 && this.toggleHeight.user === 'closed') {
				this.toggleHeight.user = 'open';
			}
		});
		// this.currentUser$ = this.store.select(selectCurrentUser);
		// this.pmCount$ = this.pmService.getPMCount();
	}

	@HostListener('document:click', ['$event.target']) public onClick(targetElement) {
		if (targetElement !== this.currentlyOpen) {
			this.toggleHeight[this.currentlyOpen.menu] = 'closed';
			this.currentlyOpen.menu = null;
			this.currentlyOpen.target = null;
		}
	}

	toggleMenu(event: Event, route: string, submenu: string): void {
		event.stopPropagation();
		event.preventDefault();
		// this.router.navigateByUrl(route);
		this.currentlyOpen.menu = submenu;
		this.currentlyOpen.target = event.target;
		this.toggleHeight[submenu] = this.toggleHeight[submenu] === 'closed' ? 'open' : 'closed';
	}

	// toggleMenu(event: Event) {
	// 	event.preventDefault();
	// 	if (event.target['nextElementSibling'].tagName === 'UL') {

	// 	}
	// }

	openPortalModal(state: 'register' | 'login') {
		// this.portalModalService.openPortal(state);
	}

	openMobileMenu() {
		this.mobileOpen = true;
	}

	closeMobileMenu() {
		this.mobileOpen = false;
	}

	logout() {
		// this.store.dispatch(new Logout());
	}

}

interface MenuItem {
	'label': string;
	'link': string;
	'loggedIn': boolean;
	'children'?: MenuItem[];
}
