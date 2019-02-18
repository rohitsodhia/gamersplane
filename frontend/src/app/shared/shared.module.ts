import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { LogoComponent } from './logo/logo.component';
import { SkewComponent } from './layout/skew/skew.component';
import { TrapezoidComponent } from './layout/trapezoid/trapezoid.component';
import { LoadingSpinnerComponent } from './loading-spinner/loading-spinner.component';

import { HbMarginDirective } from './layout/hb-margin.directive';

@NgModule({
	declarations: [
		LogoComponent,
		SkewComponent,
		TrapezoidComponent,
		LoadingSpinnerComponent,

		HbMarginDirective,
	],
	imports: [
		CommonModule
	],
	exports: [
		LogoComponent,
		SkewComponent,
		TrapezoidComponent,
		LoadingSpinnerComponent,

		HbMarginDirective,
	],

})
export class SharedModule { }
