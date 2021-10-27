from actor import Actor
from movie import Movie
from queue import Queue
from collections import deque
from heapq import heappush, heappop
from collections import defaultdict
from edge import Edge

class FilmGraf:
	def __init__( self ):
		self.actors = {}
		self.movies = {}

	def readActorFile( self ):
		# nm-id Navn tt-ID1 tt-ID2 . . . tt-IDn
		file = open( "actors.tsv", "r", encoding="utf-8" )
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

			self.actors[id] = actor

		file.close()

	def readMoviesFile( self ):
		# tt-id Tittel Rating
		file = open( "movies.tsv", "r", encoding="utf-8" )
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

		for movie in self.movies.values():
			count += ( len( movie.actors ) * ( len( movie.actors ) - 1 ) ) // 2

		print( "Edges:", count )

	def findShortestPath( self, nmid1, nmid2 ):
		actor1 = self.actors[ nmid1 ]
		actor2 = self.actors[ nmid2 ]
		def bfs_parents( ):
			parents = { actor1: False }
			queue = deque( [ actor1 ] )
			visited = set()

			while queue:
				actor = deque.popleft(queue)

				if actor == actor2:
					break

				if actor not in visited:
					visited.add(actor)

					for movie in actor.movies:
						for other in movie.actors:
							if other != actor:
								if other not in parents:
									parents[other] = [actor, movie]
									queue.append(other)

			return parents

		parents = bfs_parents()
		actor = actor2
		path = []

		if actor2 not in parents:
			return

		while actor:
			if parents[ actor ]:
				movie = parents[ actor ][1]
				path.append( "===[ " + movie.name + " (" +  str( movie.rating )  + ") ] ===> " +  actor.name )
			else:
				path.append( "\n" + actor.name )
				
			actor = parents[ actor ][0] if parents[ actor ] else False
		
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
				cost, actor = heappop(queue)

				if actor.id == id2:
					return path[id2], cost

				for movie in actor.movies:
					for other in movie.actors:
						if other != actor:

							c = cost + (10 - movie.rating)
							if c < costs[other.id]:
								costs[other.id] = c
								heappush(queue, (c, other))
								path[other.id] = path[actor.id] + [ [other, movie] ]

			return path[id2], costs[ id2 ]

		path, weight = dijkstra()

		print( "\n", actor1.name )
		for x in path:
			print( "===[", x[1].name, "(", x[1].rating, ") ] ===>", x[0].name )
		print( "Total weight:", weight )

	def count_components(self):
		def bfs( node, visited ):
			visited.add( node )
			queue = deque( [ node ] )
			result = []

			while queue:
				next_node = deque.popleft(queue)
				result.append( next_node )
				for movie in next_node.movies:
					for other in movie.actors:
						if other != next_node and other not in visited:
							visited.add( other )
							queue.append( other )
			return result

		visited = set()
		components = defaultdict( lambda: 0 )

		for node in self.actors.values():
			if node not in visited:
				components[ len( bfs( node, visited ) ) ] += 1
		
		for size, component_amount in reversed( sorted( components.items() ) ):
			print( "There are", component_amount, "components of size", size )
