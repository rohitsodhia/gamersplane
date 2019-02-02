import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { LogoComponent } from './logo/logo.component';
import { SkewComponent } from './layout/skew/skew.component';
import { TrapezoidComponent } from './layout/trapezoid/trapezoid.component';
import { LoadingSpinnerComponent } from './loading-spinner/loading-spinner.component';

@NgModule({
	declarations: [
		LogoComponent,
		SkewComponent,
		TrapezoidComponent,
		LoadingSpinnerComponent,
	],
	imports: [
		CommonModule
	],
	exports: [
		LogoComponent,
		SkewComponent,
		TrapezoidComponent,
		LoadingSpinnerComponent,
	],

})
export class SharedModule { }
