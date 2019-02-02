import { Component, OnInit } from '@angular/core';

import { PageLoadOverlayService } from './page-load-overlay.service';

@Component({
	selector: 'gp-page-load-overlay',
	templateUrl: './page-load-overlay.component.html',
	styleUrls: ['./page-load-overlay.component.scss']
})
export class PageLoadOverlayComponent implements OnInit {

	showOverlay: boolean = true;

	constructor(private pageLoadOverlayService: PageLoadOverlayService) { }

	ngOnInit() {
		this.pageLoadOverlayService.getOverlayVisiblity().subscribe((visible: boolean) => {
			this.showOverlay = visible;
		});
	}

}
