#Jandre Coetzee 10693077
#Jaco Bezuidenhout 11013878

from random import randint

class Game:


    def __init__(self, N, number_default_cells,Debug=False):
        self.N = N
        #player_state[0:1][ [(x,y),(x,y)...],[(x,y)...],[(x,y)...]....]
        self.player_state = {}
        self.player_state[0] = []
        self.player_state[1] = []

        print self.player_state

        #Init board with random places
        for id in self.player_state:
            x = randint(id*(N/2)+id,(id+1)*(N/2)-1-1+id)
            y = randint(0,N-1)
            self.player_state[id] = [[(x,y)]]

        print self.player_state

        for id in self.player_state:
            for i in range(0,number_default_cells-1):
                x = randint(id*(N/2)+id,(id+1)*(N/2)-1-1+id)
                y = randint(0,N-1)
                while not self.setDefaultNode(id,(x,y)):
                    #if should_print: print "Duplicate Found"
                    x = randint(id*(N/2)+id,(id+1)*(N/2)-1-1+id)
                    y = randint(0,N-1)

        print self.player_state

    def exists(self,coord):
        #return true if coord already exists
        return (coord in self.getGameCoords())

    def getPlayerCoords(self,id):
        #return all coords for a player
        arr = []
        for group in self.player_state[id]:
            arr += group
        return arr

    def getGameCoords(self):
        #return all coords for all players
        arr = []
        #print self.player_state
        for id in self.player_state:
            #print  self.player_state[id]
            #print len( self.player_state[id])
            for group in self.player_state[id]:
                arr += group
        return arr

    def coordToGroup(self,coords):
        #will take a coord array and group them
        arr = []
        for coord_a in coords:
            arr2 = []
            for coord_b in coords:
                if coord_a != coord_b:
                    if len((set(self.coordSpan(coord_a,2)) & set(self.coordSpan(coord_b,1)))) > 0:
                        arr2.append(coord_b)
                        #print arr2
            if len(arr2) > 0:
                arr.append(arr2)
            #print arr
        return arr

    def coordSpan(self,coord,n):
        # return the span of the coord
        arr = []
        minX = coord[0]-n
        minY = coord[1]-n
        maxX = coord[0]+n
        maxY = coord[1]+n

        for x in range(minX,maxX+1):
            for y in range(minY,maxY+1):
                arr.append((x,y))
        #print arr
        arr.remove((minX,minY))
        arr.remove((maxX,minY))
        arr.remove((minX,maxY))
        arr.remove((maxX,maxY))

        return arr

    def setDefaultNode(self,id,new):
        #default moves
        if not self.exists(new):
            coords = self.getPlayerCoords(id)
            coords.append(new)
            self.player_state[id] = self.coordToGroup(coords)
            return True
        else:
            return False


    def move(self,id,old,new):
        #player moves
        print old,new

class Board:

    def __init__(self, N, state, Debug=False):
        self.N = N
        self.state = state

    def changeState(self,old,new):
        return True

    def getState(self):
        return self.state

    def setState(self,state):
        self.state = state
        return True
