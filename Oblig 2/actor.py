from edge import Edge

class Actor:
	def __init__( self, id, name, movies ):
		self.id     = id
		self.name   = name
		self.movies = movies
		self.edges  = {}

	def add_edges( self ):
		for movie in self.movies:
			for actor in movie.getActors():
				if actor != self:
					if movie in self.edges:
						self.edges[movie].add( actor )
					else:
						self.edges[movie] = { actor }
