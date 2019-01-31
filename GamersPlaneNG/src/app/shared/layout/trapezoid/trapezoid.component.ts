import { Component, OnInit, Input, ElementRef } from '@angular/core';

@Component({
	selector: 'gp-trapezoid',
	templateUrl: './trapezoid.component.html',
	styleUrls: ['./trapezoid.component.scss']
})
export class TrapezoidComponent implements OnInit {

	@Input() skew: number = -30;
	@Input() direction: string = 'down';
	@Input() red: boolean;
	borderWidth: number;
	borderHeight: number;
	directionBorder: {} = {};

	constructor(private element: ElementRef) { }

	ngOnInit() {
		this.red = this.red !== undefined;
		if (this.direction !== 'up' && this.direction !== 'down') {
			this.direction = 'down';
		}
		
		this.borderHeight = this.element.nativeElement.lastElementChild.offsetHeight;
		this.borderWidth = Math.ceil(Math.tan(Math.abs(this.skew) * Math.PI / 180) * this.borderHeight);
		if (this.direction === 'down') {
			this.directionBorder['border-bottom-width'] = this.borderHeight + 'px';
		} else {
			this.directionBorder['border-top-width'] = this.borderHeight + 'px';
		}
	}

}
