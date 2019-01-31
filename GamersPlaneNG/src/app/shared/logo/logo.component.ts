import { Component, OnChanges, Input, SimpleChange } from '@angular/core';

@Component({
	selector: 'gp-logo',
	templateUrl: './logo.component.html',
	styleUrls: ['./logo.component.scss']
})
export class LogoComponent implements OnChanges {

	@Input() width: number = 170;
	@Input() height: number = 90;
	whRatio: number = 170 / 90;

	constructor() { }

	ngOnChanges(changes: { [key: string]: SimpleChange }) {
		if ('width' in changes && !('height' in changes)) {
			this.height = changes['width'].currentValue / this.whRatio;
		} else if ('height' in changes && !('width' in changes)) {
			this.width = changes['height'].currentValue * this.whRatio;
		}
	}

}
