import { Component, OnInit } from '@angular/core';

@Component({
	selector: 'gp-loading-spinner',
	templateUrl: './loading-spinner.component.html',
	styleUrls: ['./loading-spinner.component.scss']
})
export class LoadingSpinnerComponent implements OnInit {

	showFore: boolean = false;

	constructor() { }

	ngOnInit() {
		let toggleFore = () => {
			this.showFore = !this.showFore;
			setTimeout(toggleFore, 2000);
		};
		toggleFore();
	}

}
