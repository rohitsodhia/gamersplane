import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { LogoComponent } from './logo/logo.component';
import { SkewComponent } from './layout/skew/skew.component';
import { TrapezoidComponent } from './layout/trapezoid/trapezoid.component';

@NgModule({
	declarations: [
		LogoComponent,
		SkewComponent,
		TrapezoidComponent,
	],
	imports: [
		CommonModule
	],
	exports: [
		LogoComponent,
		SkewComponent,
		TrapezoidComponent,
	],

})
export class SharedModule { }
