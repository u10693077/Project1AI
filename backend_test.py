from backend import Game

game = Game(12,5,True)
game.getBoard()
player = game.getPlayers(0)

game.move((-1,-1),(2,1),player)
game.move((-1,-1),(1,10),player)
game.move((-1,-1),(0,5),player)
game.move((-1,-1),(3,6),player)
game.move((-1,-1),(2,2),player)


player = game.getPlayers(1)


game.move((-1,-1),(8,9),player)
game.move((-1,-1),(11,6),player)
game.move((-1,-1),(7,1),player)
game.move((-1,-1),(7,5),player)
game.move((-1,-1),(10,4),player)

game.getBoard()

game.move((10,4),(3,4),player)

game.getBoard()

# groups = []
# groups.append(Group(players[0].getPlayerID))
# groups[0].displayCoords()
# groups[0].addCoord((6,9))
# groups[0].addCoord((3,3))
# #groups[0].removeCoord((4,5))
# groups[0].addCoord((5,5))
# groups[0].displayCoords()
# groups[0].getCount()
# groups[0].getSpan()
#
# print groups[0].inSpan((4,5))
# print groups[0].contains((4,5))
#
# groups[0].removeCoord((6,9))
# groups[0].getCount()
# groups[0].getSpan()
#
# print groups[0].inSpan((4,5))
# print groups[0].contains((4,5))
