from actor import Actor
from movie import Movie

class FilmGraf:
	def __init__( self ):
		self.actors = []
		self.movies = {}
	
	def readActorFile( self ):
		# nm-id Navn tt-ID1 tt-ID2 . . . tt-IDn
		file = open( "actors.tsv", "r" )
		for line in file:
			actorInfo = line.rstrip( "\n" ).split( "\t" )

			id        = actorInfo[0]
			name      = actorInfo[1]
			movieList = actorInfo[2:]

			actor = Actor( id, name, movieList )

			for movieID in movieList:
				if movieID in self.movies:
					self.movies[ movieID ].addActor( actor )

			self.actors.append( actor )

		file.close()
	
	def readMoviesFile( self ):
		# tt-id Tittel Rating
		file = open( "movies.tsv", "r" )
		for line in file:
			movie = line.rstrip( "\n" ).split( "\t" )
			id     = movie[0]
			title  = movie[1]
			rating = movie[2]

			self.movies[ id ] = Movie( id, title, rating )

		file.close()
	
	def countNodesEdges( self ):
		print( "Oppgave 1:\n" )
		print( "Nodes:", len( self.actors ) )

		count = 0
		for id, movie in self.movies.items():
			count += movie.actorsSize() * ( movie.actorsSize() - 1 ) // 2
		
		print( "Edges:", count )
	
	def findShortestPath( self ):
		movie = None
		actor = None
		print( "===[", movie, "] ===>", actor )

	def findChillestPath( self ):
		movie = None
		actor = None
		print( "===[", movie, "] ===>", actor )
	
test = FilmGraf()
test.readMoviesFile()
test.readActorFile()
test.countNodesEdges()