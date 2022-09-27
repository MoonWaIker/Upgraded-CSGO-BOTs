from players.entity import Player
from events.hooks import Event
from mathlib import Vector

@Event('weapon_fire')
def pre_player_died(game_event):
	player = Player.from_userid(game_event['userid'])
	if player.is_bot and player.view_player:
		player.view_coordinates = Vector(*player.view_player.eye_location)