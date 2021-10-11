from actor import Actor
from movie import Movie

import timeit

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
			movieList2 = []

			

			for movieID in movieList:
				if movieID in self.movies:
					movieList2.append( self.movies[ movieID ] )
			
			actor = Actor( id, name, movieList2 )
			for movieID in movieList:
				if movieID in self.movies:
					self.movies[ movieID ].addActor( actor )

			actor.add_edges()

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
		for actor in self.actors:
			for movie, edges in actor.edges.items():
				count += len( edges )
		
		print( "Edges:", count )

	
	def findShortestPath( self ):
		movie = None
		actor = None
		print( "===[ ", movie, "(", movie.rating ,") ] ===>", actor )

	def findChillestPath( self ):
		movie = None
		actor = None
		print( "===[ ", movie, "(", movie.rating ,") ] ===>", actor )
	
test = FilmGraf()
start = timeit.default_timer()
test.readMoviesFile()
test.readActorFile()
test.countNodesEdges()
stop = timeit.default_timer()

print('Time: ', stop - start)