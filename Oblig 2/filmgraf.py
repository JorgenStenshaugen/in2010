from actor import Actor
from movie import Movie
from queue import Queue
from collections import deque
from heapq import heappush, heappop
from collections import defaultdict
import timeit

class FilmGraf:
	def __init__( self ):
		self.actors = {}
		self.movies = {}
	
	def readActorFile( self ):
		# nm-id Navn tt-ID1 tt-ID2 . . . tt-IDn
		file = open( "actors.tsv", "r" )
		for line in file:
			actorInfo = line.rstrip( "\n" ).split( "\t" )

			id           = actorInfo[0]
			name         = actorInfo[1]
			movieList    = actorInfo[2:]
			movieObjects = []


			# TODO: optimize this:
			for movieID in movieList:
				if movieID in self.movies:
					movieObjects.append( self.movies[ movieID ] )
			
			actor = Actor( id, name, movieObjects )

			for movieID in movieList:
				if movieID in self.movies:
					self.movies[ movieID ].addActor( actor )

			actor.add_edges()

			self.actors[id] = actor

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

		for id, actor in self.actors.items():
			count += len( actor.edges )

		print( "Edges:", count )

	
	def findShortestPath( self, graph, nmid1, nmid2): #BFS
		# Implementer BFS algoritmen her.

		# for å få alle edges til en skuespiller så kaller du på skuespillerens edges ( actor.edges ).
		# Edges inneholder både referanse til v ( actor 1 ) og u ( actor 2 ), f.eks: edge.actor2
		
		# Fjern denne:
		pass
				
	def findChillestPath( self, id1, id2 ):
		# Du trenger egentlig bare objektet til actor id1 når du starter

		def dijkstra():
			# Jeg valgte å ha en hjelpefunksjon for selve algoritmen. ( men du velger helt selv )
			# både edges og actors er comperable. så f.eks actor1 < actor2 eller edges1 <= edges2 er lov

			return [], 0

		path, weight = dijkstra()

		# Print ut stien her:

	
start = timeit.default_timer()
test = FilmGraf()
test.readMoviesFile()
test.readActorFile()
test.countNodesEdges()

test.findChillestPath( "nm2255973", "nm0000460" )

stop = timeit.default_timer()
print('Time: ', stop - start)
