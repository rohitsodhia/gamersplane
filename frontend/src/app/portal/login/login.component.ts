import { Component, OnInit, Output, EventEmitter } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';

import { AuthService } from 'src/app/shared/auth.service';

@Component({
	selector: 'gp-login',
	templateUrl: './login.component.html',
	styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {

	login: FormGroup;

	@Output() success: EventEmitter<{}> = new EventEmitter();

	constructor(
		private formBuilder: FormBuilder,
		private authService: AuthService,
	) { }

	ngOnInit() {
		this.login = this.formBuilder.group({
			login: [
				'',
				[Validators.required]
			],
			password: [
				'',
				[Validators.required, Validators.minLength(7)]
			],
		});
	}

	submitLogin() {
		if (this.login.invalid) {
			return false;
		}
		this.authService.login(
			this.login.get('login').value,
			this.login.get('password').value
		).subscribe(success => {
			this.success.emit(success);
		});
	}

	openRegister() {
	}

	accountRecovery() {
	}

}
