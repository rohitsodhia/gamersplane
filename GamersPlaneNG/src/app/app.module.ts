import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { StoreModule } from '@ngrx/store';

import { AppRoutingModule } from './app-routing.module';
import { SharedModule } from './shared/shared.module';
import { PageLoadOverlayModule } from './shared/page-load-overlay/page-load-overlay.module';

import { AppComponent } from './app.component';
import { HeaderComponent } from './header/header.component';
import { FooterComponent } from './footer/footer.component';

@NgModule({
	imports: [
		BrowserModule,
		BrowserAnimationsModule,
		HttpClientModule,
		StoreModule.forRoot({}),

		AppRoutingModule,

		SharedModule,
		PageLoadOverlayModule
	],
	declarations: [
		AppComponent,
		HeaderComponent,
		FooterComponent,
	],
	providers: [],
	bootstrap: [
		AppComponent
	]
})
export class AppModule { }
