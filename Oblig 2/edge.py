class Edge:
	def __init__( self, actor1, actor2, movie ):
		self.actor1 = actor1
		self.actor2 = actor2
		self.movie  = movie
		self.weight = 10 - float( movie.rating )

	def __bool__(self):
		return True
