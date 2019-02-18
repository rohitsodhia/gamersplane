export class System {
	_id: string;
	name: string;
	publisher?: {
		name: string,
		site: string
	};
	genres?: string[];
	lfg?: number;
	basics?: {
		text: string,
		site: string
	}[];
	hasCharSheet: boolean;
	enabled?: boolean;
}
