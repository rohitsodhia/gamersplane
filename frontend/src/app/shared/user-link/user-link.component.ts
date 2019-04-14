import { Component, OnInit, Input } from '@angular/core';

@Component({
	selector: 'gp-user-link',
	templateUrl: './user-link.component.html',
	styleUrls: ['./user-link.component.scss']
})
export class UserLinkComponent implements OnInit {

	@Input() user: { userId: number, username: string };

	constructor() { }

	ngOnInit() {
	}

}
