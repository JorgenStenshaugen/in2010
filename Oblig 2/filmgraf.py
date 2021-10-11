from actor import Actor
from movie import Movie

class FilmGraf:
	actors = []
	movies = []

	def __init__( self ):
		self.actors = []
		self.movies = []
	
	def readActorFile( self ):
		# nm-id Navn tt-id1 tt-id2 . . . tt-idk
		file = open( "actors.tsv", "r" )
		for line in file:
			actor = line.rstrip("\n").split( "\t" )
			
			id     = actor[0]
			name   = actor[1]
			movies = actor[2:]

			self.actors.append( Actor( id, name, movies ) )

		file.close()
	
	def readMoviesFile( self ):
	  	# tt-id Tittel Rating
		file = open( "movies.tsv", "r" )
		for line in file:
			movie = line.rstrip("\n").split( "\t" )
			id     = movie[0]
			title  = movie[1]
			rating = movie[2]

			self.movies.append( Movie( id, title, rating ) )

		file.close()
	
	def countNodesEdges( self ):
		print( "Oppgave 1:\n" )
		print( "Nodes:", len( self.actors ) )
		count = 0
		# for key, value in self.movies.items():
		# 	count += len( value[2] ) * ( len( value[2] ) - 1) // 2
		
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