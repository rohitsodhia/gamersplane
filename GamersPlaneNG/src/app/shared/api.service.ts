import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';

import { environment } from '../../environments/environment';

@Injectable({
	providedIn: 'root'
})
export class ApiService {

	constructor(private http: HttpClient) { }

	private addToken(headers: HttpHeaders) {
		let token = localStorage.getItem('jwt');
		if (token) {
			headers = headers.set('Authorization', 'Bearer ' + token);
		}
		return headers;
	}

	private constructParams(data?: Object) {
		// Object.keys(data).reduce((params, key) => params.set(key, data[key]), new HttpParams());
		let params = new HttpParams();
		for (let key in data) {
			if (typeof data[key] !== 'object') {
				params = params.set(key, data[key]);
			} else {
				for (let oKey in data[key]) {
					params = params.set(key + '[' + oKey + ']', data[key][oKey]);
				}
			}
		}

		return params;
	}

	get<T = any>(path: string, data?: Object): Observable<T> {
		let headers = new HttpHeaders();
		headers = this.addToken(headers);
		return this.http
			.get<T>(environment.apiDomain + path, {
				headers: headers,
				params: this.constructParams(data)
			});
	}

	post<T = any>(path, data): Observable<T> {
		let headers = new HttpHeaders({
			'Content-Type': 'application/json'
			// 'Content-Type': 'application/x-www-form-urlencoded'
		});
		headers = this.addToken(headers);
		return this.http
			.post<T>(environment.apiDomain + path, JSON.stringify(data), {
				headers: headers,
			});
	}

	delete<T = any>(path: string, data?: Object): Observable<T> {
		let headers = new HttpHeaders();
		headers = this.addToken(headers);
		return this.http
			.delete<T>(environment.apiDomain + path, {
				headers: headers,
				params: this.constructParams(data)
			});
	}

	patch<T = any>(path: string, data?: Object): Observable<T> {
		let headers = new HttpHeaders({
			'Content-Type': 'application/x-www-form-urlencoded'
		});
		headers = this.addToken(headers);
		return this.http
			.patch<T>(environment.apiDomain + path, JSON.stringify(data), {
				headers: headers,
			});
	}

}
