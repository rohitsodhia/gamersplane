import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { StoreModule } from '@ngrx/store';
// import { CurrentUserStoreModule } from '../shared/store/current-user-store/current-user-store.module';

@NgModule({
	imports: [
		CommonModule,

		StoreModule.forRoot({}),
	],
	declarations: []
})
export class RootStoreModule { }
