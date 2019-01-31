export class User {

	userId: number;
	username: string;
	avatar: string;
	private readonly defaultAvatar: string = '/assets/images/avatar.png';

	constructor(details: {
		userId?: number,
		username?: string,
		avatar?: string,
	}) {
		for (const key in details) {
			this[key] = details[key];
		}
	}

	getAvatar(): string
	{
		return this.avatar ? this.avatar : this.defaultAvatar;
	}

}
