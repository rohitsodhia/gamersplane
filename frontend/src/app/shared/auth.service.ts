import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

import * as jwtDecode from 'jwt-decode';

import { ApiService } from './api.service';
import { LoginPostAPIResponse } from '../portal/login/login-post-api-response';

import { User } from './User.class';

@Injectable({
	providedIn: 'root'
})
export class AuthService {

	constructor(
		private api: ApiService,
	) { }

	login(login: string, password: string): Observable<string> {
		return this.api
			.post<LoginPostAPIResponse>('/auth/validateCredentials', { login: login, password: password })
			.pipe(
				map(response => response.data ? response.data.jwt : null)
			)
	}

	validateToken(jwt) {
		if (jwt && jwt.length) {
			let decoded: UserJWT = jwtDecode(jwt);
			let newUser = new User({
				userId: decoded.userId,
				username: decoded.username,
				avatar: decoded.avatar
			});
			return newUser;
		} else {
			return null;
		}
	}

}

export interface UserJWT extends User {
	iss: string,
	iat: number,
	exp: number,
}
