import { APIResponse } from '../../shared/api-response.interface';

export interface LoginPostAPIResponse extends APIResponse {
	data?: {
		jwt: string;
	}
}
