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

	def findShortestPath( self, nmid1, nmid2): #BFS
		start = self.actors[ nmid1 ]
		end = self.actors[ nmid2 ]
		visited = []
		queue = [[start]]
		q = []
		if start == end:
			return
		while queue:
			path = queue.pop(0)
			node = path[-1]
			if node not in visited:
				for edge in node.edges:
					shortest_path = list(path)
					shortest_path.append(edge.actor2)
					queue.append(shortest_path)
					q.append([edge.actor2, edge.movie])
					if edge.actor2 == end:
						q.append([edge.actor2, edge.movie])
						print(start.name)
						for i in range(len(shortest_path)+1):
							print( "===[", q[i][1].name, "(", q[i][1].rating, ") ] ===>", q[i][0].name)
							print( "===[", q[-1][1].name, "(", q[-1][1].rating, ") ] ===>", q[-1][0].name)
							return
				visited.append(node)
				
	def findChillestPath( self, id1, id2 ):
		actor1 = self.actors[ id1 ]

		def dijkstra():
			queue = [ ( 0, actor1 ) ]
			path = { id1: [] }
			costs = defaultdict( lambda: float('inf') )
			costs[ id1 ] = 0

			while queue:
				cost, actor = heappop( queue )

				if actor.id == id2:
					return path[id2], cost

				for edge in actor.edges:
					other = edge.actor2
	
					c = cost + edge.weight
					if c < costs[ other.id ]:
						costs[ other.id ] = c
						heappush( queue, ( c,  other ) )
						path[ other.id ] = path[actor.id] + [edge]

			return path[id2], costs[ id2 ]

		path, weight = dijkstra()

		for x in path:
			print( "===[", x.movie.name, "(", x.movie.rating, ") ] ===>", x.actor2.name )
		print( "Total weight:", weight )
	
start = timeit.default_timer()
test = FilmGraf()
test.readMoviesFile()
test.readActorFile()
test.countNodesEdges()

test.findShortestPath("nm2255973", "nm0000460")

test.findChillestPath( "nm2255973", "nm0000460" )

stop = timeit.default_timer()
print('Time: ', stop - start)
