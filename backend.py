#Jandre Coetzee 10693077
#Jaco Bezuidenhout 11013878

from random import randint

should_print = False

class Game:
    turn = 0
    def __init__(self, N, number_default_cells,Debug=False):
        self.N = N
        self.players = {}
        self.currPlayer = 0
        Player.player_count= 0
        self.players[Player("Player 1")] = []
        self.players[Player("Player 2")] = []

        if not Debug:
            for player in self.players:
                id = player.getPlayerID()
                if should_print: print "Player:",id
                for i in range(0,number_default_cells):
                    x = randint(id*(N/2)+id,(id+1)*(N/2)-1-1+id)
                    y = randint(0,N-1)
                    while self.hasCoord((x,y)):
                        #if should_print: print "Duplicate Found"
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
        if should_print: print "Player", player.getPlayerID(), self.getCurrentPlayer()

        if player.getPlayerID() == self.getCurrentPlayer() or coord_old == (-1,-1):
            if coord_old == (-1,-1):
                #if should_print: print "Added new coord at", coord_new
                group = self.findGroup(coord_new,player)
                group.addCoord(coord_new)

            else:
                if should_print: print "coord"
                if should_print: print coord_new
                if should_print: print coord_old[0]
                if should_print: print ""

                group = self.findCoordGroup(coord_old,player)

                valid = self.isValidMove(coord_new,coord_old,group)

                if not valid[0]:
                    return [False,valid[1]]


                if should_print: print "Found group"
                if should_print: print group.getCoords()



                new_group = self.findGroup(coord_new,player)
                new_group.addCoord(coord_new)

                group.removeCoord(coord_old)

                for pair in self.isTouching(new_group):
                    coord = pair[0]
                    group = pair[1]
                    group.removeCoord(coord)
                    new_group.addCoord(coord)

                if should_print: print "Moved from", coord_old, "==>", coord_new

                if(self.getCurrentPlayer() == 0):
                        self.setCurrenPlayer(1)
                else:
                        self.setCurrenPlayer(0)
                if should_print: print "Next_Player",self.getCurrentPlayer()

                for p in self.players:
                    if (self.getNodesLeft(p) == 0):
                        return [True,"Loser: Player",p.getPlayerID]


    def isValidMove(self,new,old,group):
        #is it the current players turn to make a move
        if group == False:
            if should_print: print "Not your turn to play"
            return [False,"Not your turn to play"]

        #is the move in a straight line (left/right/up/down)
        if not ((new[0]!=old[0] and new[1]==old[1]) or (new[1]!=old[1] and new[0]==old[0])):
            return [False,"No diagonal moves allowed"]

        #is the move within the max number of allowed cells that can be moved
        allowed_max = len(group.getCoords())
        if max(abs(old[0]-new[0]),abs(old[1]-new[1])) > allowed_max:
            return [False,"You tried to move more cells than allowed"]

        #Will the move cover another occupied cell?
        if (self.findCoordGroup(new,0,True)):
            return [False,"You cannot move to an occupied cell"]

        return [True,""]

    def isTouching(self,group):
        arr = []
        for player in self.players:
            if player.getPlayerID() == self.getCurrentPlayer():
                span = group.getSpanWithCorners()
                for group in self.players[player]:
                    for coord in group.getSpan():
                        if coord in span:
                            print "My Own Group in span", group.getCoords()
                            for coord in group.getCoords():
                                arr.append((coord,group))
                            break
            else:
                span = group.getSpanMinCorners()
                for group in self.players[player]:
                    for coord in group.getCoords():
                        if coord in span:
                            if should_print: print "Group in span", group.getCoords()
                            for coord in group.getCoords():
                                arr.append((coord,group))
                            break
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
                ##if should_print: print (x,y)
                span.append((x,y))
        if not all:
        #for player in self.players:
            for group in self.players[player]:
                if group.intersects(span):
                    #if should_print: print "Group Found"
                    return group
            group = Group()
            self.players[player].append(group)
            return group
        else:
            for player in self.players:
                for group in self.players[player]:
                    if group.intersects(span):
                        #if should_print: print "Group Found"
                        return [group,player]

    def findCoordGroup(self,coord,p,all=False):
        if all:
            for player in self.players:
                for group in self.players[player]:
                    if coord in group.getCoords():
                        #if should_print: print "Group Found"
                        return True
        else:
            for group in self.players[p]:
                if coord in group.getCoords():
                    #if should_print: print "Group Found"
                    return group
        return False


    # returns the board as an array
    def getBoard(self):
        if should_print: print "\n\n"
        board = {}
        for x in range(0,self.N):
            for y in range(0,self.N):
                board[(x,y)] = ' '

        for player in self.players:
            player.displayPlayer()
            for group in self.players[player]:
                print "Group: ",group.getCoords()
                if len(group.getCoords()) > 0:
                    for coord in group.getSpan():
                        board[coord] = str(player.getPlayerID())+'*'
                else:
                    self.players[player].remove(group)

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

    #return the number of nodes in the players hand
    def getNodesLeft(self,player):
        total = 0
        for group in self.players[player]:
            total += len(group.getCoords())

        return total

    def miniMax(self, player):
                if should_print: print ''

class Player:
    'Common base class for all games'
    player_count = 0

    def __init__(self, name):
        self.name = name
        Player.player_count += 1
        self.player_id = Player.player_count - 1
        if should_print: print "Player Joined: Name : ", self.name,  ", Player ID: ", self.player_id

    def displayPlayer(self):
        print self.name + "," +  str(self.player_id)

    def getPlayerID(self):
        return self.player_id

class Group:
    def __init__(self):
        self.coords = []
        if should_print: print self.coords

    def getCoords(self):
        #if should_print: print self.coords
        return self.coords

    def removeCoord(self,coord):
        if should_print: print "Removing",coord
        if should_print: print self.coords
        self.coords.remove(coord)
        if should_print: print self.coords

    def addCoord(self,coord):
        #if should_print: print "Adding",coord
        self.coords.append(coord)

    def getCount(self):
        if should_print: print len(self.coords)

    def contains(self,coord):
        return (coord in self.coords)

    def intersects(self,coords):
        return len(set(self.getSpan())&set(coords))

    def viewCoords(self):
                if should_print: print self.coords

    def getSpan(self):
        arr = []
        x = []
        y = []
        if len(self.coords) > 0:
            for coord in self.coords:
                x.append(coord[0])
                y.append(coord[1])

            #if should_print: print "Span"
            #if should_print: print x
            #if should_print: print y

            for c_x in range(max(0,min(x)-1),max(x)+1+1):
                tmp = ""
                for c_y in range(max(0,min(y)-1),max(y)+1+1):
                    tmp += '(%s,%s);' % (c_x,c_y)
                    arr.append((c_x,c_y))
                if should_print: print tmp
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
            if should_print: print tmp

        #removing edges
        arr.remove((max(x)+2,max(y)+2))
        arr.remove((max(x)+2,max(0,min(y)-2)))
        arr.remove((max(0,min(x)-2),max(y)+2))
        arr.remove((max(0,min(x)-2),max(0,min(y)-2)))

        return arr

    def getSpanWithCorners(self):
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
            if should_print: print tmp

        return arr

    def inSpan(self,coord):
        return (coord in self.getSpan())

    def overlap(self,coord):
        return (coord in self.coords)
