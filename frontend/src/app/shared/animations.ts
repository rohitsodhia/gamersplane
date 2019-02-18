import { trigger, state, style, transition, animate } from "@angular/animations";

// import { trigger, state, style, transition, animate } from '@angular/core';

export function slideHeight(duration: string | number) {
	return trigger(
		'slideHeight',
		[
			state('closed', style({
				display: 'none',
				height: 0
			})),
			state('open', style({
				display: 'block',
				height: '*'
			})),
			// transition('void => closed', [
			// 	style({
			// 		display: 'none'
			// 	}),
			// 	animate('0')
			// ]),
			transition('closed <=> open', [
				animate(duration + ' ease')
			])
		]
	);
}