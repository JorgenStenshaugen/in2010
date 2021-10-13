class Movie:
	def __init__( self, id, title, rating ):
		self.id     = id
		self.name   = title
		self.rating = float( rating )
		self.actors = set()

	def addActor( self, actor ):
		self.actors.add( actor )

	def actorsSize( self ):
		return len( self.actors )

	def getActors( self ):
		return self.actors