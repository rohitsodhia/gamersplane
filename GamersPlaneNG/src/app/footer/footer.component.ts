import { Component, OnInit } from '@angular/core';

import { ReferralLinksService } from '../shared/referral-links.service';

import { ReferralLink } from '../shared/referral-link.interface';

@Component({
	selector: 'gp-footer',
	templateUrl: './footer.component.html',
	styleUrls: ['./footer.component.scss']
})
export class FooterComponent implements OnInit {

	referralLinks: ReferralLink[] = [];
	menu: MenuItem[][] = [
		[
			{
				'label': 'Tools',
				'link': 'tools'
			},
			{
				'label': 'Systems',
				'link': 'systems'
			},
			{
				'label': 'Characters',
				'link': 'characters'
			},
			{
				'label': 'Games',
				'link': 'games'
			},
			{
				'label': 'Forums',
				'link': 'forums'
			},
			{
				'label': 'The Gamers',
				'link': 'gamersList'
			},
			{
				'label': 'Links',
				'link': 'link'
			},
		],
		[
			{
				'label': 'FAQs',
				'link': 'faqs'
			},
			{
				'label': 'About GP',
				'link': 'about'
			},
			{
				'label': 'Contact Us',
				'link': 'contact'
			},
		]
	];
	socialLinks: MenuItem[] = [
		{
			'label': 'Twitter',
			'link': 'https://twitter.com/GamersPlane'
		},
		{
			'label': 'Facebook',
			'link': 'https://www.facebook.com/Gamers-Plane'
		},
		{
			'label': 'Twitch',
			'link': 'https://www.twitch.tv/gamersplane'
		},
	];
	admin: boolean = false;

	constructor(
		private referralLinksService: ReferralLinksService
	) { }

	ngOnInit() {
		console.log(this.referralLinksService);
		this.referralLinksService.get().subscribe(links => this.referralLinks = links);
	}

}

interface MenuItem {
	'label': string;
	'link': string;
}
