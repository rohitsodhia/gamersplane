import { Directive, Input, ElementRef } from '@angular/core';

import { HbMarginService } from './hb-margin.service';

@Directive({
	selector: '[gp-hbMargin]'
})
export class HbMarginDirective {

	@Input('gp-hbMargin') key: string = 'hb';

	constructor(
		private element: ElementRef,
		private hbMarginService: HbMarginService
	) {
		this.hbMarginService.watch(this.key).subscribe((margin: number) => {
			this.element.nativeElement.style.marginLeft = (margin * 2) + 'px';
			this.element.nativeElement.style.marginRight = (margin * 2) + 'px';
		})
	}

}
