import { Component, OnInit, Input } from '@angular/core';

@Component({
	selector: 'rs-combobox',
	templateUrl: './combobox.component.html',
	styleUrls: ['./combobox.component.scss']
})
export class ComboboxComponent implements OnInit {

	@Input() options: {};

	constructor() { }

	ngOnInit() {
	}

}
