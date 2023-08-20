

class TrackModel:
	def __init__(self, name, city, country, length, no_of_laps, track_map, description,
					downforce, grip, top_speed, braking):
		self.name = name
		self.city = city
		self.country = country
		self.length = length
		self.no_of_laps = no_of_laps
		self.track_map = track_map
		self.description = description
        
		self.downforce = downforce
		self.grip = grip
		self.top_speed = top_speed
		self.braking = braking
        
		