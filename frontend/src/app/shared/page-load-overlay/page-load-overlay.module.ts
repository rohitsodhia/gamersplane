import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { SharedModule } from '../shared.module';

import { PageLoadOverlayComponent } from './page-load-overlay.component';

import { PageLoadOverlayService } from './page-load-overlay.service';

@NgModule({
	imports: [
		CommonModule,
		SharedModule
	],
	declarations: [
		PageLoadOverlayComponent,
	],
	exports: [
		PageLoadOverlayComponent,
	],
	providers: [
		PageLoadOverlayService,
	]
})
export class PageLoadOverlayModule { }
