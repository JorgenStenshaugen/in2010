class Movie:
	def __init__( self, id, title, rating ):
		self.id     = id
		self.name   = title
		self.rating = rating
		self.movies = []

	def edges( self ):
		return None