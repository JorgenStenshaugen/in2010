from edge import Edge
from collections import defaultdict

class Actor:
	def __init__( self, id, name, movies ):
		self.id       = id
		self.name     = name
		self.movies   = movies
		self.edges    = set()
		self.topMovie = None

		if len( self.movies ):
			self.topMovie = self.movies[0]
			for movie in movies:
				if movie.rating <= self.topMovie.rating:
					self.topMovie = movie

	def add_edges( self ):
		for movie in self.movies:
			for actor in movie.getActors():
				if self != actor:
					self.edges.add( Edge( self, actor, movie ) )
	
	def __lt__( self, other ):
		if not self.topMovie:
			return False
		if not other.topMovie:
			return True
		return self.topMovie.rating < other.topMovie.rating