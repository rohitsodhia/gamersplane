import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';

import { LogoComponent } from './logo/logo.component';
import { SkewComponent } from './layout/skew/skew.component';
import { TrapezoidComponent } from './layout/trapezoid/trapezoid.component';
import { LoadingSpinnerComponent } from './loading-spinner/loading-spinner.component';

import { HbMarginDirective } from './layout/hb-margin.directive';
import { UserLinkComponent } from './user-link/user-link.component';
import { ComboboxComponent } from './combobox/combobox.component';

@NgModule({
	declarations: [
		LogoComponent,
		SkewComponent,
		TrapezoidComponent,
		LoadingSpinnerComponent,

		HbMarginDirective,

		UserLinkComponent,
		ComboboxComponent,
	],
	imports: [
		CommonModule,
		RouterModule,
	],
	exports: [
		LogoComponent,
		SkewComponent,
		TrapezoidComponent,
		LoadingSpinnerComponent,

		HbMarginDirective,

		UserLinkComponent,
		ComboboxComponent,
	],

})
export class SharedModule { }
