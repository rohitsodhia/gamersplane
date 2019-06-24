ALTER DATABASE gamersplane CHARACTER SET utf8 COLLATE utf8_unicode_ci;

CREATE TABLE `acpPermissions` (
  `userID` int(11) NOT NULL,
  `permission` varchar(20) NOT NULL,
  PRIMARY KEY (`userID`,`permission`)
);

CREATE TABLE `charAutocomplete` (
  `itemID` int(11) NOT NULL AUTO_INCREMENT,
  `type` varchar(10) NOT NULL,
  `name` varchar(50) NOT NULL,
  `searchName` varchar(50) NOT NULL,
  `userDefined` int(11) DEFAULT NULL,
  PRIMARY KEY (`itemID`),
  UNIQUE KEY `type` (`type`,`name`)
);

CREATE TABLE `characterHistory` (
  `actionID` int(11) NOT NULL AUTO_INCREMENT,
  `characterID` int(11) NOT NULL,
  `enactedBy` int(11) NOT NULL,
  `enactedOn` datetime NOT NULL,
  `gameID` int(11) DEFAULT NULL,
  `action` varchar(30) NOT NULL,
  `additionalInfo` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`actionID`)
);

CREATE TABLE `characterLibrary` (
  `characterID` int(11) NOT NULL,
  `inLibrary` tinyint(1) NOT NULL DEFAULT '1',
  `viewed` int(11) NOT NULL,
  PRIMARY KEY (`characterID`)
);

CREATE TABLE `characterLibrary_favorites` (
  `userID` int(11) NOT NULL,
  `characterID` int(11) NOT NULL,
  `updateDate` datetime NOT NULL,
  PRIMARY KEY (`userID`,`characterID`)
);

CREATE TABLE `characters` (
  `characterID` int(11) NOT NULL AUTO_INCREMENT,
  `userID` int(11) NOT NULL,
  `label` varchar(50) NOT NULL,
  `charType` varchar(3) NOT NULL,
  `systemID` int(11) NOT NULL,
  `system` varchar(30) NOT NULL,
  `gameID` int(11) DEFAULT NULL,
  `approved` tinyint(1) NOT NULL,
  `retired` date DEFAULT NULL,
  PRIMARY KEY (`characterID`),
  KEY `userID` (`userID`),
  KEY `gameID` (`gameID`)
);

CREATE TABLE `contact` (
  `contactID` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `date` datetime NOT NULL,
  `username` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `subject` mediumtext NOT NULL,
  `comment` mediumtext NOT NULL,
  PRIMARY KEY (`contactID`)
);

CREATE TABLE `deckDraws` (
  `drawID` int(11) NOT NULL AUTO_INCREMENT,
  `postID` int(11) NOT NULL,
  `deckID` int(11) NOT NULL,
  `type` varchar(10) NOT NULL,
  `cardsDrawn` varchar(200) NOT NULL,
  `reveals` varchar(20) NOT NULL,
  `reason` varchar(50) NOT NULL,
  PRIMARY KEY (`drawID`),
  KEY `postID` (`postID`),
  KEY `deckID` (`deckID`)
);

CREATE TABLE `deckPermissions` (
  `deckID` int(11) NOT NULL,
  `userID` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`deckID`,`userID`),
  KEY `userID` (`userID`)
);

CREATE TABLE `deckTypes` (
  `short` varchar(10) NOT NULL,
  `name` varchar(50) NOT NULL,
  `deckSize` tinyint(4) NOT NULL,
  `class` varchar(20) NOT NULL,
  `image` varchar(20) NOT NULL,
  `extension` varchar(4) NOT NULL,
  PRIMARY KEY (`short`)
);

CREATE TABLE `decks` (
  `deckID` int(11) NOT NULL AUTO_INCREMENT,
  `gameID` int(11) NOT NULL,
  `label` varchar(50) NOT NULL,
  `type` varchar(10) NOT NULL,
  `deck` varchar(200) NOT NULL,
  `position` tinyint(4) NOT NULL,
  `lastShuffle` datetime NOT NULL,
  PRIMARY KEY (`deckID`),
  KEY `gameID` (`gameID`)
);

CREATE TABLE `dispatch` (
  `url` varchar(100) NOT NULL,
  `pageID` varchar(50) DEFAULT NULL,
  `ngController` varchar(50) DEFAULT NULL,
  `file` varchar(100) NOT NULL,
  `title` varchar(50) DEFAULT NULL,
  `description` text,
  `loginReq` tinyint(1) NOT NULL DEFAULT '1',
  `fixedGameMenu` tinyint(4) NOT NULL,
  `bodyClass` varchar(50) DEFAULT NULL,
  `active` tinyint(1) NOT NULL DEFAULT '1',
  `modalWidth` smallint(4) DEFAULT NULL,
  PRIMARY KEY (`url`)
);

CREATE TABLE `featsList` (
  `featID` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `searchName` varchar(50) DEFAULT NULL,
  `userDefined` int(11) DEFAULT NULL,
  PRIMARY KEY (`featID`),
  UNIQUE KEY `name` (`name`)
);

CREATE TABLE `forumAdmins` (
  `userID` int(11) NOT NULL,
  `forumID` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`userID`,`forumID`),
  KEY `forumID` (`forumID`)
);

CREATE TABLE `forumSubs` (
  `userID` int(11) NOT NULL,
  `type` varchar(1) NOT NULL,
  `ID` int(11) NOT NULL,
  PRIMARY KEY (`userID`,`type`,`ID`)
);

CREATE TABLE `forums` (
  `forumID` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(200) NOT NULL,
  `description` text,
  `forumType` varchar(1) DEFAULT 'f',
  `parentID` int(11) DEFAULT NULL,
  `heritage` varchar(25) NOT NULL,
  `order` int(5) NOT NULL,
  `gameID` int(11) DEFAULT NULL,
  `threadCount` int(11) NOT NULL,
  PRIMARY KEY (`forumID`),
  UNIQUE KEY `heritage` (`heritage`),
  KEY `parentID` (`parentID`)
);

CREATE TABLE `forums_heritage` (
  `parentID` int(11) NOT NULL,
  `childID` int(11) NOT NULL,
  PRIMARY KEY (`parentID`,`childID`)
);

CREATE TABLE `forums_groupMemberships` (
  `groupID` int(11) NOT NULL,
  `userID` int(11) NOT NULL,
  PRIMARY KEY (`groupID`,`userID`),
  KEY `userID` (`userID`)
);

CREATE TABLE `forums_groups` (
  `groupID` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `status` tinyint(4) NOT NULL,
  `ownerID` int(11) NOT NULL,
  `gameID` int(11) DEFAULT NULL,
  PRIMARY KEY (`groupID`),
  KEY `ownerID` (`ownerID`)
);

CREATE TABLE `forums_permissions_general` (
  `forumID` int(11) NOT NULL,
  `read` tinyint(1) NOT NULL,
  `write` tinyint(1) NOT NULL,
  `editPost` tinyint(1) NOT NULL,
  `deletePost` tinyint(1) NOT NULL,
  `createThread` tinyint(1) NOT NULL,
  `deleteThread` tinyint(1) NOT NULL,
  `addPoll` tinyint(1) NOT NULL,
  `addRolls` tinyint(1) NOT NULL DEFAULT '-1',
  `addDraws` tinyint(1) NOT NULL DEFAULT '-1',
  `moderate` tinyint(1) NOT NULL DEFAULT '-1',
  PRIMARY KEY (`forumID`)
);

CREATE TABLE `forums_permissions_groups` (
  `groupID` int(11) NOT NULL,
  `forumID` int(11) NOT NULL,
  `read` tinyint(1) NOT NULL,
  `write` tinyint(1) NOT NULL,
  `editPost` tinyint(1) NOT NULL,
  `deletePost` tinyint(1) NOT NULL,
  `createThread` tinyint(1) NOT NULL,
  `deleteThread` tinyint(1) NOT NULL,
  `addPoll` tinyint(1) NOT NULL,
  `addRolls` tinyint(1) NOT NULL,
  `addDraws` tinyint(1) NOT NULL,
  `moderate` tinyint(1) NOT NULL,
  PRIMARY KEY (`groupID`,`forumID`),
  KEY `forumID` (`forumID`)
);

CREATE TABLE `forums_permissions_users` (
  `userID` int(11) NOT NULL,
  `forumID` int(11) NOT NULL,
  `read` tinyint(1) NOT NULL DEFAULT '0',
  `write` tinyint(1) NOT NULL DEFAULT '0',
  `editPost` tinyint(1) NOT NULL DEFAULT '0',
  `deletePost` tinyint(1) NOT NULL DEFAULT '0',
  `createThread` tinyint(1) NOT NULL DEFAULT '0',
  `deleteThread` tinyint(1) NOT NULL DEFAULT '0',
  `addPoll` tinyint(1) NOT NULL DEFAULT '0',
  `addRolls` tinyint(1) NOT NULL,
  `addDraws` tinyint(1) NOT NULL,
  `moderate` tinyint(1) NOT NULL,
  PRIMARY KEY (`userID`,`forumID`),
  KEY `forumID` (`forumID`)
);

CREATE TABLE `forums_pollOptions` (
  `pollOptionID` int(11) NOT NULL AUTO_INCREMENT,
  `threadID` int(11) NOT NULL,
  `option` varchar(200) NOT NULL,
  PRIMARY KEY (`pollOptionID`)
);

CREATE TABLE `forums_pollVotes` (
  `userID` int(11) NOT NULL,
  `pollOptionID` int(11) NOT NULL,
  `votedOn` datetime NOT NULL,
  PRIMARY KEY (`userID`,`pollOptionID`)
);

CREATE TABLE `forums_polls` (
  `threadID` int(11) NOT NULL,
  `poll` varchar(200) NOT NULL,
  `optionsPerUser` tinyint(4) NOT NULL DEFAULT '1',
  `pollLength` tinyint(4) NOT NULL,
  `allowRevoting` tinyint(1) NOT NULL,
  PRIMARY KEY (`threadID`)
);

CREATE TABLE `forums_readData` (
  `userID` int(11) NOT NULL,
  `forumData` mediumtext NOT NULL,
  `threadData` mediumtext NOT NULL,
  PRIMARY KEY (`userID`)
);

CREATE TABLE `forums_readData_forums` (
  `userID` int(11) NOT NULL,
  `forumID` int(11) NOT NULL,
  `markedRead` int(11) NOT NULL,
  PRIMARY KEY (`userID`,`forumID`)
);

CREATE TABLE `forums_readData_threads` (
  `userID` int(11) NOT NULL,
  `threadID` int(11) NOT NULL,
  `lastRead` int(11) NOT NULL,
  PRIMARY KEY (`userID`,`threadID`)
);

CREATE TABLE `gameHistory` (
  `actionID` int(11) NOT NULL AUTO_INCREMENT,
  `gameID` int(11) NOT NULL,
  `enactedBy` int(11) NOT NULL,
  `enactedOn` datetime NOT NULL,
  `action` varchar(20) NOT NULL,
  `affectedType` varchar(20) DEFAULT NULL,
  `affectedID` int(11) DEFAULT NULL,
  PRIMARY KEY (`actionID`)
);

CREATE TABLE `gameInvites` (
  `gameID` int(11) NOT NULL,
  `invitedID` int(11) NOT NULL,
  `invitedOn` datetime NOT NULL,
  PRIMARY KEY (`gameID`,`invitedID`)
);

CREATE TABLE `games` (
  `gameID` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(50) NOT NULL,
  `systemID` int(11) NOT NULL,
  `system` varchar(30) NOT NULL,
  `gmID` int(11) NOT NULL,
  `created` datetime NOT NULL,
  `start` datetime NOT NULL,
  `end` datetime NOT NULL,
  `postFrequency` varchar(4) NOT NULL,
  `numPlayers` tinyint(4) NOT NULL,
  `charsPerPlayer` tinyint(4) NOT NULL DEFAULT '1',
  `description` mediumtext NOT NULL,
  `charGenInfo` mediumtext NOT NULL,
  `forumID` int(11) DEFAULT NULL,
  `groupID` int(11) NOT NULL,
  `logForumID` int(11) DEFAULT NULL,
  `status` tinyint(1) NOT NULL DEFAULT '1',
  `public` tinyint(1) NOT NULL,
  `retired` datetime DEFAULT NULL,
  PRIMARY KEY (`gameID`),
  KEY `gmID` (`gmID`),
  KEY `forumID` (`forumID`),
  KEY `groupID` (`groupID`)
);

CREATE TABLE `lfg` (
  `userID` int(11) NOT NULL,
  `systemID` int(11) NOT NULL,
  `system` varchar(30) NOT NULL,
  PRIMARY KEY (`userID`,`system`),
  UNIQUE KEY `userID` (`userID`,`system`) USING BTREE
);

CREATE TABLE `loginRecords` (
  `userID` int(11) NOT NULL,
  `attemptStamp` datetime NOT NULL,
  `ipAddress` varchar(15) NOT NULL,
  `successful` tinyint(1) NOT NULL,
  PRIMARY KEY (`userID`,`attemptStamp`)
);

CREATE TABLE `mapData` (
  `mapID` int(11) NOT NULL,
  `col` tinyint(4) NOT NULL,
  `row` tinyint(4) NOT NULL,
  `data` mediumtext,
  PRIMARY KEY (`mapID`,`col`,`row`)
);

CREATE TABLE `maps` (
  `mapID` int(11) NOT NULL AUTO_INCREMENT,
  `gameID` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `rows` tinyint(4) NOT NULL,
  `cols` tinyint(4) NOT NULL,
  `info` varchar(300) NOT NULL,
  `visible` tinyint(1) NOT NULL,
  `deleted` tinyint(1) NOT NULL,
  PRIMARY KEY (`mapID`)
);

CREATE TABLE `maps_iconHistory` (
  `actionID` int(11) NOT NULL AUTO_INCREMENT,
  `iconID` int(11) NOT NULL,
  `mapID` int(11) NOT NULL,
  `enactedBy` int(11) NOT NULL,
  `enactedOn` datetime NOT NULL,
  `action` varchar(20) NOT NULL,
  `origin` varchar(10) DEFAULT NULL,
  `destination` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`actionID`)
);

CREATE TABLE `maps_icons` (
  `iconID` int(11) NOT NULL AUTO_INCREMENT,
  `mapID` int(11) NOT NULL,
  `label` varchar(2) NOT NULL,
  `name` varchar(50) NOT NULL,
  `description` varchar(200) NOT NULL,
  `color` varchar(6) NOT NULL,
  `location` varchar(7) NOT NULL,
  `deleted` tinyint(1) NOT NULL,
  PRIMARY KEY (`iconID`)
);

CREATE TABLE `marvel_actionsList` (
  `actionID` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `searchName` varchar(50) DEFAULT NULL,
  `cost` tinyint(4) NOT NULL,
  `magic` tinyint(1) NOT NULL,
  `source` varchar(50) NOT NULL,
  `userDefined` int(11) DEFAULT NULL,
  PRIMARY KEY (`actionID`)
);

CREATE TABLE `marvel_modifiersList` (
  `modifierID` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `searchName` varchar(50) DEFAULT NULL,
  `cost` float NOT NULL,
  `costTo` varchar(5) NOT NULL,
  `multipleAllowed` varchar(40) NOT NULL,
  `source` varchar(50) NOT NULL,
  `userDefined` int(11) DEFAULT NULL,
  PRIMARY KEY (`modifierID`)
);

CREATE TABLE `notifications` (
  `notificationID` int(11) NOT NULL AUTO_INCREMENT,
  `category` varchar(20) NOT NULL,
  `enactedBy` int(11) NOT NULL,
  `enactedOn` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `actedUpon` int(11) NOT NULL,
  PRIMARY KEY (`notificationID`)
);

CREATE TABLE `players` (
  `gameID` int(11) NOT NULL,
  `userID` int(11) NOT NULL,
  `approved` tinyint(1) NOT NULL,
  `isGM` tinyint(1) NOT NULL,
  `primaryGM` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`gameID`,`userID`)
);

CREATE TABLE `pms` (
  `pmID` int(11) NOT NULL AUTO_INCREMENT,
  `recipientID` int(11) NOT NULL,
  `senderID` int(11) NOT NULL,
  `title` varchar(100) NOT NULL,
  `message` mediumtext NOT NULL,
  `datestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `viewed` tinyint(1) NOT NULL,
  `replyTo` int(11) NOT NULL,
  PRIMARY KEY (`pmID`),
  KEY `recipientID` (`recipientID`),
  KEY `senderID` (`senderID`)
);

CREATE TABLE `posts` (
  `postID` int(11) NOT NULL AUTO_INCREMENT,
  `threadID` int(11) NOT NULL,
  `title` varchar(50) NOT NULL,
  `authorID` int(11) NOT NULL,
  `message` mediumtext NOT NULL,
  `datePosted` datetime NOT NULL,
  `lastEdit` datetime NOT NULL,
  `timesEdited` tinyint(4) NOT NULL,
  `postAs` int(11) DEFAULT NULL,
  PRIMARY KEY (`postID`),
  KEY `threadID` (`threadID`),
  KEY `authorID` (`authorID`)
);

CREATE TABLE `privilages` (
  `userID` int(11) NOT NULL,
  `privilage` varchar(20) NOT NULL,
  PRIMARY KEY (`userID`,`privilage`)
);

CREATE TABLE `referralLinks` (
  `key` varchar(255) NOT NULL,
  `title` varchar(255) DEFAULT NULL,
  `link` varchar(255) DEFAULT NULL,
  `order` int(11) DEFAULT NULL,
  PRIMARY KEY (`key`)
);

CREATE TABLE `rolls` (
  `rollID` int(11) NOT NULL AUTO_INCREMENT,
  `postID` int(11) NOT NULL,
  `type` varchar(12) NOT NULL,
  `reason` varchar(100) NOT NULL,
  `roll` varchar(50) NOT NULL,
  `indivRolls` varchar(500) NOT NULL,
  `results` varchar(250) DEFAULT NULL,
  `visibility` tinyint(1) NOT NULL,
  `extras` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`rollID`),
  KEY `postID` (`postID`)
);

CREATE TABLE `skillsList` (
  `skillID` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `searchName` varchar(50) DEFAULT NULL,
  `userDefined` int(11) DEFAULT NULL,
  PRIMARY KEY (`skillID`),
  UNIQUE KEY `name` (`name`)
);

CREATE TABLE `spycraft2_focusesList` (
  `focusID` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `searchName` varchar(50) DEFAULT NULL,
  `userDefined` int(11) DEFAULT NULL,
  PRIMARY KEY (`focusID`)
);

CREATE TABLE `starwarsffg_talentsList` (
  `talentID` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `searchName` varchar(50) NOT NULL,
  `userDefined` int(11) DEFAULT NULL,
  PRIMARY KEY (`talentID`),
  UNIQUE KEY `name` (`name`)
);

CREATE TABLE `system_charAutocomplete_map` (
  `systemID` int(11) NOT NULL,
  `system` varchar(30) NOT NULL,
  `itemID` int(11) NOT NULL,
  PRIMARY KEY (`systemID`,`itemID`)
);

CREATE TABLE `systems` (
  `id` varchar(20) NOT NULL,
  `name` varchar(40) NOT NULL,
  `sortName` varchar(40) NOT NULL,
  `publisher` json NOT NULL,
  `genres` json,
  `basics` json,
  `hasCharSheet` tinyint(1) NOT NULL DEFAULT 1,
  `enabled` tinyint(1) NOT NULL DEFAULT 0,
  `createdOn` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updatedOn` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

CREATE TABLE `threads` (
  `threadID` int(11) NOT NULL AUTO_INCREMENT,
  `forumID` int(11) NOT NULL,
  `sticky` tinyint(1) NOT NULL,
  `locked` tinyint(1) NOT NULL,
  `allowRolls` tinyint(1) NOT NULL,
  `allowDraws` tinyint(1) NOT NULL,
  `firstPostID` int(11) NOT NULL,
  `lastPostID` int(11) NOT NULL,
  `postCount` int(11) NOT NULL,
  PRIMARY KEY (`threadID`),
  KEY `forumID` (`forumID`)
);

CREATE TABLE `userAddedItems` (
  `uItemID` int(11) NOT NULL AUTO_INCREMENT,
  `itemType` varchar(10) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `itemID` int(11) DEFAULT NULL,
  `addedBy` int(11) NOT NULL,
  `addedOn` datetime NOT NULL,
  `systemID` int(11) DEFAULT NULL,
  `system` varchar(30) DEFAULT NULL,
  `action` varchar(10) DEFAULT NULL,
  `actedBy` int(11) DEFAULT NULL,
  `actedOn` datetime DEFAULT NULL,
  PRIMARY KEY (`uItemID`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `itemID` (`itemID`,`systemID`),
  UNIQUE KEY `name_2` (`name`),
  UNIQUE KEY `itemID_2` (`itemID`,`systemID`)
);

CREATE TABLE `userHistory` (
  `actionID` int(11) NOT NULL AUTO_INCREMENT,
  `userID` int(11) NOT NULL,
  `enactedBy` int(11) NOT NULL,
  `enactedOn` datetime NOT NULL,
  `action` varchar(30) NOT NULL,
  `additionalInfo` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`actionID`)
);

CREATE TABLE `usermeta` (
  `metaID` int(11) NOT NULL AUTO_INCREMENT,
  `userID` int(11) NOT NULL,
  `metaKey` varchar(50) NOT NULL,
  `metaValue` longtext NOT NULL,
  `autoload` tinyint(1) NOT NULL,
  PRIMARY KEY (`metaID`),
  UNIQUE KEY `userID` (`userID`,`metaKey`),
  KEY `autoload` (`autoload`)
);

CREATE TABLE `users` (
  `userID` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(24) NOT NULL,
  `password` varchar(64) NOT NULL,
  `salt` varchar(20) NOT NULL,
  `email` varchar(50) NOT NULL,
  `joinDate` datetime NOT NULL,
  `activatedOn` datetime DEFAULT NULL,
  `lastActivity` datetime DEFAULT NULL,
  `reference` mediumtext NOT NULL,
  `enableFilter` tinyint(1) NOT NULL DEFAULT '1',
  `showAvatars` tinyint(1) NOT NULL DEFAULT '1',
  `avatarExt` varchar(3) NOT NULL,
  `timezone` varchar(20) NOT NULL DEFAULT 'Europe/London',
  `showTZ` tinyint(1) NOT NULL,
  `realName` varchar(50) DEFAULT NULL,
  `gender` varchar(1) NOT NULL,
  `birthday` date NOT NULL,
  `showAge` tinyint(1) NOT NULL,
  `location` varchar(100) DEFAULT NULL,
  `aim` varchar(50) DEFAULT NULL,
  `gmail` varchar(50) DEFAULT NULL,
  `twitter` varchar(50) DEFAULT NULL,
  `stream` varchar(50) DEFAULT NULL,
  `games` varchar(200) DEFAULT NULL,
  `newGameMail` tinyint(1) NOT NULL DEFAULT '1',
  `postSide` varchar(1) NOT NULL DEFAULT 'r',
  `suspendedUntil` datetime DEFAULT NULL,
  `banned` tinyint(1) NOT NULL,
  PRIMARY KEY (`userID`),
  UNIQUE KEY `username` (`username`)
);

CREATE TABLE `wordFilter` (
  `wordID` int(11) NOT NULL AUTO_INCREMENT,
  `word` varchar(50) NOT NULL,
  `spam` tinyint(1) NOT NULL DEFAULT '1',
  PRIMARY KEY (`wordID`)
);

CREATE VIEW `forums_permissions` AS select 'general' AS `type`,0 AS `typeID`,`forums_permissions_general`.`forumID` AS `forumID`,`forums_permissions_general`.`read` AS `read`,`forums_permissions_general`.`write` AS `write`,`forums_permissions_general`.`editPost` AS `editPost`,`forums_permissions_general`.`deletePost` AS `deletePost`,`forums_permissions_general`.`createThread` AS `createThread`,`forums_permissions_general`.`deleteThread` AS `deleteThread`,`forums_permissions_general`.`addPoll` AS `addPoll`,`forums_permissions_general`.`addRolls` AS `addRolls`,`forums_permissions_general`.`addDraws` AS `addDraws`,`forums_permissions_general`.`moderate` AS `moderate` from `forums_permissions_general` union select 'group' AS `type`,`forums_permissions_groups`.`groupID` AS `typeID`,`forums_permissions_groups`.`forumID` AS `forumID`,`forums_permissions_groups`.`read` AS `read`,`forums_permissions_groups`.`write` AS `write`,`forums_permissions_groups`.`editPost` AS `editPost`,`forums_permissions_groups`.`deletePost` AS `deletePost`,`forums_permissions_groups`.`createThread` AS `createThread`,`forums_permissions_groups`.`deleteThread` AS `deleteThread`,`forums_permissions_groups`.`addPoll` AS `addPoll`,`forums_permissions_groups`.`addRolls` AS `addRolls`,`forums_permissions_groups`.`addDraws` AS `addDraws`,`forums_permissions_groups`.`moderate` AS `moderate` from `forums_permissions_groups` union select 'user' AS `type`,`forums_permissions_users`.`userID` AS `typeID`,`forums_permissions_users`.`forumID` AS `forumID`,`forums_permissions_users`.`read` AS `read`,`forums_permissions_users`.`write` AS `write`,`forums_permissions_users`.`editPost` AS `editPost`,`forums_permissions_users`.`deletePost` AS `deletePost`,`forums_permissions_users`.`createThread` AS `createThread`,`forums_permissions_users`.`deleteThread` AS `deleteThread`,`forums_permissions_users`.`addPoll` AS `addPoll`,`forums_permissions_users`.`addRolls` AS `addRolls`,`forums_permissions_users`.`addDraws` AS `addDraws`,`forums_permissions_users`.`moderate` AS `moderate` from `forums_permissions_users`;

CREATE VIEW `forums_permissions_groups_c` AS select `gm`.`userID` AS `userID`,`gp`.`forumID` AS `forumID`,if((max(`gp`.`read`) = 2),2,min(`gp`.`read`)) AS `read`,if((max(`gp`.`write`) = 2),2,min(`gp`.`write`)) AS `write`,if((max(`gp`.`editPost`) = 2),2,min(`gp`.`editPost`)) AS `editPost`,if((max(`gp`.`deletePost`) = 2),2,min(`gp`.`deletePost`)) AS `deletePost`,if((max(`gp`.`createThread`) = 2),2,min(`gp`.`createThread`)) AS `createThread`,if((max(`gp`.`deleteThread`) = 2),2,min(`gp`.`deleteThread`)) AS `deleteThread`,if((max(`gp`.`addPoll`) = 2),2,min(`gp`.`addPoll`)) AS `addPoll`,if((max(`gp`.`addRolls`) = 2),2,min(`gp`.`addRolls`)) AS `addRolls`,if((max(`gp`.`addDraws`) = 2),2,min(`gp`.`addDraws`)) AS `addDraws`,if((max(`gp`.`moderate`) = 2),2,min(`gp`.`moderate`)) AS `moderate` from (`forums_groupMemberships` `gm` join `forums_permissions_groups` `gp` on((`gm`.`groupID` = `gp`.`groupID`))) group by `gp`.`forumID`,`gm`.`userID`;

CREATE VIEW `threads_relPosts` AS select `posts`.`threadID` AS `threadID`,min(`posts`.`postID`) AS `firstPostID`,max(`posts`.`postID`) AS `lastPostID` from `posts` group by `posts`.`threadID`;

CREATE VIEW `userPosts` AS select `posts`.`authorID` AS `userID`,count(0) AS `numPosts` from `posts` group by `posts`.`authorID`;