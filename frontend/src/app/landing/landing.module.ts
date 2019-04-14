import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';
import { RouterModule } from '@angular/router';

import { LandingRoutingModule } from './landing-routing.module';
import { SharedModule } from '../shared/shared.module';

import { LandingComponent } from './landing/landing.component';

@NgModule({
	declarations: [LandingComponent],
	imports: [
		CommonModule,
		HttpClientModule,
		RouterModule,

		SharedModule,
		LandingRoutingModule,
	]
})
export class LandingModule { }
