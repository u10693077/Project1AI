from random import randint

class Game:
	turn = 0
	def __init__(self, N, number_default_cells,Debug=False):
		self.N = N
		self.players = {}
		self.currPlayer = 0

		self.players[Player("Player 1")] = []
		self.players[Player("Player 2")] = []

		if not Debug:
			for player in self.players:
				id = player.getPlayerID()
				print "Player:",id
				for i in range(0,number_default_cells):
					x = randint(id*(N/2)+id,(id+1)*(N/2)-1-1+id)
					y = randint(0,N-1)
					while self.hasCoord((x,y)):
						#print "Duplicate Found"
						x = randint(id*(N/2)+id,(id+1)*(N/2)-1-1+id)
						y = randint(0,N-1)
					self.move((-1,-1),(x,y),player)

	def getPlayers(self,id=-1):
		if id == -1:
			return self.players
		else:
			for player in self.players:
				if player.getPlayerID() == id:
					return player

	def getCurrentPlayer(self):
                return self.currPlayer

        def setCurrenPlayer(self, nextPlayer):
                self.currPlayer = nextPlayer

	def move(self,coord_old,coord_new,player):
		if coord_old == (-1,-1):
			#print "Added new coord at", coord_new
			group = self.findGroup(coord_new,player)
			group.addCoord(coord_new)

		else:
                        print "coord"
                        print coord_old
                        print coord_new
                        print coord_old[0]
                        print ""

                       
			group = self.findGroup(coord_old,player)
			
			new_group = self.findGroup(coord_new,player)
			new_group.addCoord(coord_new)

                        group.removeCoord(coord_old)
                        
			for pair in self.isTouching(new_group):
				coord = pair[0]
				group = pair[1]
				group.removeCoord(coord)
				new_group.addCoord(coord)

			print "Moved from", coord_old, "==>", coord_new

			if(self.getCurrentPlayer() == 0):
                                self.setCurrenPlayer(1)
                        else:
                                self.setCurrenPlayer(0)
                                

	def isTouching(self,group):
		span = group.getSpanMinCorners()
		arr = []
		for player in self.players:
			for group in self.players[player]:
				for coord in group.getCoords():
					if coord in span:
						arr.append((coord,group))
		return arr
	def hasCoord(self,coord):
		for player in self.players:
			for group in self.players[player]:
				if group.contains(coord):
					return True
			return False

	def findGroup(self,coord,player,all=False):
		span = []
		for x in range(max(0,coord[0]-2),min(self.N-1,coord[0]+2+1)):
			for y in range(max(0,coord[1]-2),min(self.N-1,coord[1]+2+1)):
				##print (x,y)
				span.append((x,y))
		if not all:
		#for player in self.players:
			for group in self.players[player]:
				if group.intersects(span):
					#print "Group Found"
					return group
			group = Group()
			self.players[player].append(group)
			return group
		else:
			for player in self.players:
				for group in self.players[player]:
					if group.intersects(span):
						#print "Group Found"
						return [group,player]



	def getBoard(self):
		print "\n\n"
		board = {}
		for x in range(0,self.N):
			for y in range(0,self.N):
				board[(x,y)] = ' '

		for player in self.players:
			for group in self.players[player]:
				if len(group.getCoords()) > 0:
					for coord in group.getSpan():
						board[coord] = str(player.getPlayerID())+'*'

		for player in self.players:
			for group in self.players[player]:
				for coord in group.getCoords():
					board[coord] = player.getPlayerID()

		for x in range(0,self.N):
			tmp = ""
			for y in range(0,self.N):
				tmp = "%s|%3s|" % (tmp, str(board[(x,y)]))
			print tmp

		return board

class Player:
	'Common base class for all games'
	player_count = 0

	def __init__(self, name):
		self.name = name
		Player.player_count += 1
		self.player_id = Player.player_count - 1
		print "Player Joined: Name : ", self.name,  ", Player ID: ", self.player_id

	def displayPlayer(self):
		print self.name + "," +  str(self.player_id)

	def getPlayerID(self):
		return self.player_id

class Group:
	def __init__(self):
		self.coords = []
                print self.coords
	def getCoords(self):
		#print self.coords
		return self.coords

	def removeCoord(self,coord):
		#print "Removing",coord
                #print self.coords
		self.coords.remove(coord)
		#print self.coords

	def addCoord(self,coord):
		#print "Adding",coord
		self.coords.append(coord)

	def getCount(self):
		print len(self.coords)

	def contains(self,coord):
		return (coord in self.coords)

	def intersects(self,coords):
		return len(set(self.getSpan())&set(coords))

	def viewCoords(self):
                print self.coords

	def getSpan(self):
		arr = []
		x = []
		y = []

		for coord in self.coords:
			x.append(coord[0])
			y.append(coord[1])

                #print "Span"
		#print x
		#print y

		for c_x in range(max(0,min(x)-1),max(x)+1+1):
			tmp = ""
			for c_y in range(max(0,min(y)-1),max(y)+1+1):
				tmp += '(%s,%s);' % (c_x,c_y)
				arr.append((c_x,c_y))
			#print tmp
		return arr

	def getSpanMinCorners(self):
		arr = []
		x = []
		y = []

		for coord in self.coords:
			x.append(coord[0])
			y.append(coord[1])

		for c_x in range(max(0,min(x)-2),max(x)+1+2):
			tmp = ""
			for c_y in range(max(0,min(y)-2),max(y)+1+2):
				tmp += '(%s,%s);' % (c_x,c_y)
				arr.append((c_x,c_y))
			print tmp

		arr.remove((max(x)+2,max(y)+2))
		arr.remove((max(x)+2,max(0,min(y)-2)))
		arr.remove((max(0,min(x)-2),max(y)+2))
		arr.remove((max(0,min(x)-2),max(0,min(y)-2)))

		return arr

	def inSpan(self,coord):
		return (coord in self.getSpan())

	def overlap(self,coord):
		return (coord in self.coords)
