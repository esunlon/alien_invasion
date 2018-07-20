class Settings():
	"""A class to store all settings for Alien Invasion."""
	
	def __init__(self):
		"""Init the game's static settings."""
		# Screen settings
		self.screen_width = 1000
		self.screen_height = 650
		self.bg_color = (230, 230, 230)
		
		# Ship Settings
		self.ship_speed_factor = 3
		self.ship_limit = 3
		# Bullet settings
		self.bullet_speed_factor = 1
		self.bullet_width = 300
		self.bullet_height = 15
		self.bullet_color = 60, 60, 60
		self.bullets_allowed = 3
		
		# Alien settings
		self.alien_speed_factor = 1
		self.fleet_drop_speed = 100
		
		# How quickly the game speeds up
		self.speedup_scale = 1.1
		# How quickly the alien point values increase
		self.score_scale = 1.5
		
		self.initialize_dynamic_settings()
		
		
		# fleet_direction of 1 represents right; -1 represents left.
		self.fleet_direction = 1
		
	def initialize_dynamic_settings(self):
		"""Init settings that change througout the game."""
		self.ship_speed_factor = 1.5
		self.bullet_speed_factor = 3
		self.alien_speed_factor = 1
		
		# fleet direction of 1 represents right; -1 represents left.
		self.fleet_direction = 1
		
		#Scoring
		self.alien_points = 50
		
	def increase_speed(self):
		"""Increase speed settings."""
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale
		
		self.alien_points = int(self.alien_points * self.score_scale)
		print(self.alien_points)
		
		
