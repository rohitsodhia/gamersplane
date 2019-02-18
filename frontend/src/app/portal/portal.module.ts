import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ReactiveFormsModule } from '@angular/forms';

import { PortalRoutingModule } from './portal-routing.module';
import { SharedModule } from '../shared/shared.module';

import { LoginComponent } from './login/login.component';

@NgModule({
	imports: [
		CommonModule,
		ReactiveFormsModule,
		PortalRoutingModule,

		SharedModule
	],
	declarations: [
		LoginComponent
	],
})
export class PortalModule { }
