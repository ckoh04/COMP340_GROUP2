# COMP340_GROUP2

## README

This project is the backend for a game service.

This service will allow a game to add and remove users, maintain scores,
keep a history of usage, the user contact info and level, and an inventory of what the user has earned or found.
The administrator will have the ability to disable and re-enable a user, get a report of high scores, usage info, and time spent in the game.
An admin can also wipe the game of all data.

A Local Consol will be used to call the game service to test and control it.

Communication between a game (or test program) and the game service will be through a RESTful API.
Additional	data	needed	by	any	commands	will	be	sent	as	a	JSON	string.		Data	being	returned	will	be	
as	a	JSON	string	and	return	status	should	be	correct	based	on	the	status	of	the	operation.

The	RESTful	API	will support	the	CRUD	operations	and	follow	a	standard	resource	layout.

The	bulk	of	the	work	will	be	written	in	Python	using	the	Django	framework	and	be	handled	in	various	Python	files.	
The files include
1. Users.py	– manages	the	user	API	
2. Admin.py	– manages	the	admin	API
3. Inventory.py	– manages	the	inventory/list	API
4. Scores.py	– manages	the	scores	for	each	user
