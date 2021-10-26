from actor import Actor
from movie import Movie
from queue import Queue
from collections import deque
from heapq import heappush, heappop
from collections import defaultdict

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
		print( "Nodes:", len( self.actors ) )

		count = 0

		for id, actor in self.actors.items():
			count += len( actor.edges )

		print( "Edges:", count )

	def findShortestPath( self, nmid1, nmid2 ):
		actor1 = self.actors[ nmid1 ]
		actor2 = self.actors[ nmid2 ]
		def bfs_parents( ):
			parents = { actor1: False }
			queue = deque( [ actor1 ] )
			visited = set()

			while queue:
				actor = deque.popleft( queue )

				if actor == actor2:
					continue

				if actor not in visited:
					visited.add( actor )

					for edge in actor.edges:
						other = edge.actor2
						
						if other not in parents:
							parents[ other ] = edge
							queue.append( other )

			return parents

		parents = bfs_parents()
		actor = actor2
		path = []

		if actor2 not in parents:
			return

		while actor:
			if parents[ actor ]:
				movie = parents[ actor ].movie
				path.append( "===[ " + movie.name + " (" +  str( movie.rating )  + ") ] ===> " +  actor.name )
			else:
				path.append( "\n" + actor.name )
				
			actor = parents[ actor ].actor1 if parents[ actor ] else False
		
		for x in path[::-1]:
			print( x )	
				
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

		print( "\n", actor1.name )
		for x in path:
			print( "===[", x.movie.name, "(", x.movie.rating, ") ] ===>", x.actor2.name )
		print( "Total weight:", weight )

	def dfs_full( self ):
		visited = set()
		components = defaultdict( lambda: 0 )

		def dfs_rec(start, visited2):
			visited2.add(start)
			
			for edge in start.edges:
				actor = edge.actor2
				if edge not in visited2:
					dfs_rec( actor, visited2 )
			
			return visited2

		for actor in self.actors.values():
			if actor not in visited:
				visited.add( actor )
				test = dfs_rec( actor, set() )
				components[ len( test ) ] += 1
		
		for x, y in components.items():
			print( x, y )
