class Movie:
	def __init__( self, id, title, rating ):
		self.id     = id
		self.name   = title
		self.rating = rating
		self.actors = []

	def addActor( self, actor ):
		self.actors.append( actor )

	def actorsSize( self ):
		return len( self.actors )

	def getActors( self ):
		return self.actors