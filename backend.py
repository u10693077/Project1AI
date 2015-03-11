import time
from random import randint

N = 8

class Game:
	'Common base class for all games'
	player_count = 0
	turn = 0
	board = {}
	print "\n*** Init Board *** \n"
	for x in range(N):
		tmp = ""
		for y in range(N):
			board[(x,y)] = " "
			tmp = tmp + str(board[(x,y)]) + "," 
		print tmp 
	
	print "\n****** Done ****** \n"
	
	def __init__(self, name):
		self.name = name
		Game.player_count += 1
		self.player_id = Game.player_count - 1
		print "Player Joined: Name : ", self.name,  ", Player ID: ", self.player_id
		Game.displayBoard(self)
		
	def displayBoard(self):
		print "\n****** Board ****** \n"
		for x in range(N):
			tmp = ""
			for y in range(N):
				tmp = tmp + str(Game.board[(x,y)]) + "," 
			print tmp 

	def displayPlayer(self):
		print self.name + "," +  str(self.player_id)
	
	def move(self,coord):
		if Game.turn == self.player_id:
			print "\nPlayer",self.player_id, "made a move to", coord
			#Game.board[coord] = self.player_id
			for x in range(coord[0]-1,coord[0]+2):
				for y in range(coord[1]-1,coord[1]+2):
					if x < N and y < N and x >= 0 and y >= 0:
						if Game.board[(x,y)] == " ":
							Game.board[(x,y)] = self.player_id
						else:
							Game.board[(x,y)] = "*"
			Game.displayBoard(self)
			Game.turn = abs(Game.turn - 1)
			return True
		else:
			return False
		
player_1 = Game("Jaco")
player_2 = Game("Piet")

for k in range(10):
	if not player_1.move((randint(0,N-1),randint(0,N-1))):
		print "\n\n Its not your turn \n\n"
	time.sleep(0.5)

	if not player_2.move((randint(0,N-1),randint(0,N-1))):
		print "\n\n Its not your turn \n\n"
	time.sleep(0.5)