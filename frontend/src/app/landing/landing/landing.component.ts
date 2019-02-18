import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { ScreenWidthService } from 'src/app/shared/screen-width.service';
import { SystemService } from 'src/app/shared/system.service';
import { GameService } from 'src/app/shared/game.service';
import { System } from 'src/app/shared/System.class';

@Component({
	selector: 'gp-landing',
	templateUrl: './landing.component.html',
	styleUrls: ['./landing.component.scss']
})
export class LandingComponent implements OnInit {

	systems: {}[] = [];
	loadingGames: boolean = true;
	games: {}[] = [];
	focusOn: string = null;
	whatIsLogos: string[];
	screenWidth: Observable<number>;

	constructor(
		private screenWidthService: ScreenWidthService,
		private systemService: SystemService,
		private gameService: GameService
	) { }

	ngOnInit() {
		this.screenWidth = this.screenWidthService.get();
		this.screenWidth.subscribe(width => {
			if (width >= 1024) {
				this.whatIsLogos = ['dnd5', 'thestrange', 'pathfinder', 'starwarsffg', '13thage', 'numenera', 'shadowrun5', 'fate', 'savageworlds'];
			} else {
				this.whatIsLogos = ['dnd5', 'thestrange', 'pathfinder', 'starwarsffg', '13thage', 'numenera', 'shadowrun5', 'fate'];
			}
		});
		this.systemService.get().subscribe((systems) => {
			this.systems = [{ value: 'all', 'display': 'All' }];
			systems.forEach((system: System) => {
				this.systems.push({ value: system._id, 'display': system.name });
			})
		});
	}

	getGames(system?: string): Observable<{}> {
		return this.gameService.get({
			system: system !== undefined ? system : null,
			orderBy: 'created',
			orderByDir: 'desc',
			limit: 3,
			fields: 'title,gm,system,numPlayers,playerCount'
		});
	}

	setSystem(system: string) {
		if (system === 'all') {
			system = null;
		}
		this.loadingGames = true;
		this.games = [];
		this.getGames(system).subscribe(data => {
			this.games = data['games'];
			this.loadingGames = false;
		});
	}

}
