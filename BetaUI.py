import Tkinter as tk
from Tkinter import *
import time
from random import randint
from backend import Game

TITLE_FONT = ("Helvetica", 18, "bold")


class CellWars(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PlayerVsPlayer, PlayerVsAI, AIvsAI):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, c):
        '''Show a frame for the given class'''
        frame = self.frames[c]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Welcome To Cell Wars", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Player vs. Player", width=20,
                            command=lambda: controller.show_frame(PlayerVsPlayer))
        button2 = tk.Button(self, text="Player vs. AI", width=20,
                            command=lambda: controller.show_frame(PlayerVsAI))
        button3 = tk.Button(self, text="AI vs. AI", width=20,
                            command=lambda: controller.show_frame(AIvsAI))
        button1.pack()
        button2.pack()
        button3.pack()



class PlayerVsPlayer(tk.Frame):
    def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Player vs. Player", font=TITLE_FONT)
		label.pack(side="top", fill="x", pady=10)
		buttonBack = tk.Button(self, text="Back", width=20,
						   command=lambda: controller.show_frame(StartPage))
		buttonStart = tk.Button(self, text="Start", width=20, bg="red",
						   command=lambda: self.start(gridSize, initialCell))

		labelGridSize = tk.Label(self, text="Grid Size (even number >8):", font=12)

		labelInitialCell = tk.Label(self, text="Initial Cells:", font=12)

		gridSize = tk.Entry(self, bd=5, justify=CENTER, textvariable=StringVar())
		gridSize.delete(0, END)
		gridSize.insert(0,"12")



		initialCell = tk.Entry(self, bd=5, justify=CENTER, textvariable=StringVar())
		initialCell.delete(0, END)
		initialCell.insert(0,"5")

		labelGridSize.pack()
		gridSize.pack()
		labelInitialCell.pack()
		initialCell.pack()
		buttonStart.pack()
		buttonBack.pack()

    def start(self, gridSize, initialCell):
        CreatBoard(gridSize.get().strip(), initialCell.get().strip())

class PlayerVsAI(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Player vs. AI", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        buttonBack = tk.Button(self, text="Back", width=20,
                           command=lambda: controller.show_frame(StartPage))
        buttonStart = tk.Button(self, text="Start", width=20, bg="red",
                           command=lambda: controller.show_frame(StartPage))

        labelGridSize = tk.Label(self, text="Grid Size (even number >8):", font=12)
        gridSize = Entry(self, bd=5, justify=CENTER, textvariable=StringVar())
        gridSize.delete(0, END)
        gridSize.insert(0,"12")

        labelInitialCell = tk.Label(self, text="Initial Cells:", font=12)
        initialCell = tk.Entry(self, bd=5, justify=CENTER, textvariable=StringVar())
        initialCell.delete(0, END)
        initialCell.insert(0,"5")

        labelPlyDepth= tk.Label(self, text="Ply Depth:", font=12)
        plyDepth = Entry(self, bd=5, justify=CENTER, textvariable=StringVar())

        aiType = IntVar()

        minimax = Radiobutton(self, text="Minimax", variable=aiType, value=1)

        minimaxAlpBe = Radiobutton(self, text="Minimax with alpha-beta pruning", variable=aiType, value=2)

        labelGridSize.pack()
        gridSize.pack()
        labelInitialCell.pack()
        initialCell.pack()
        labelPlyDepth.pack()
        plyDepth.pack()
        minimax.pack(anchor = W)
        minimaxAlpBe.pack(anchor = W)
        buttonStart.pack()
        buttonBack.pack()



class AIvsAI(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="AI vs. AI", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        buttonBack = tk.Button(self, text="Back", width=20,
                           command=lambda: controller.show_frame(StartPage))
        buttonStart = tk.Button(self, text="Start", width=20, bg="red",
                           command=lambda: controller.show_frame(StartPage))

        labelGridSize = tk.Label(self, text="Grid Size (even number >8):", font=12)
        gridSize = Entry(self, bd=5, justify=CENTER, textvariable=StringVar())
        gridSize.delete(0, END)
        gridSize.insert(0,"12")

        labelInitialCell = tk.Label(self, text="Initial Cells:", font=12)
        initialCell = tk.Entry(self, bd=5, justify=CENTER, textvariable=StringVar())
        initialCell.delete(0, END)
        initialCell.insert(0,"5")

        labelPlyDepth= tk.Label(self, text="Ply Depth:", font=12)
        plyDepth = Entry(self, bd=5, justify=CENTER, textvariable=StringVar())

        aiType = IntVar()

        minimax = Radiobutton(self, text="Minimax", variable=aiType, value=1)

        minimaxAlpBe = Radiobutton(self, text="Minimax with alpha-beta pruning", variable=aiType, value=2)

        labelGridSize.pack()
        gridSize.pack()
        labelInitialCell.pack()
        initialCell.pack()
        labelPlyDepth.pack()
        plyDepth.pack()
        minimax.pack(anchor = W)
        minimaxAlpBe.pack(anchor = W)
        buttonStart.pack()
        buttonBack.pack()


class CreatBoard():
    pressed_count = 0
    play_turn = 0
    
    def __init__(self, grSize, inCell):

        self.N = int(grSize)
        self.matrix = [[0 for x in range(self.N)] for x in range(self.N)]
        self.all_buttons = []

        self.game = Game(self.N,int(inCell))
        print int(inCell)

        self.board = Tk()
        self.board.title('Turn: Player Red')
        
        self.creatMatrix()
        board= self.game.getBoard()

    def run(self):
        self.board.mainloop()


    def creatMatrix(self):
        for y, row in enumerate(self.matrix):
            buttons_row = []
            for x, element in enumerate(row):
                boton = Button(self.board, width=6, height=2, command=lambda a=x,b=y: self.onButtonPressed(a,b))
                boton.grid(row=y, column=x)
                buttons_row.append( boton )
            self.all_buttons.append( buttons_row )
        self.draw()


    def onButtonPressed(self, y, x):
        print "pressed: x=%s y=%s" % (x, y)
        CreatBoard.pressed_count += 1
        
        
        if (CreatBoard.pressed_count == 1):
            self.old_coord = (x,y)
            self.all_buttons[x][y]['bg'] = '#%02x%02x%02x' % (0, 255, 0)
        if (CreatBoard.pressed_count == 2):
            if self.old_coord == (x,y):
                CreatBoard.pressed_count = 0
                self.old_coord = (0,0)
                self.draw()
            else:
                CreatBoard.pressed_count = 0  
                self.game.move(self.old_coord,(x,y),self.game.getPlayers(CreatBoard.play_turn))
                if (CreatBoard.play_turn == 0):
                    CreatBoard.play_turn = 1
                else:
                    CreatBoard.play_turn = 0

                if(self.game.getCurrentPlayer() == 0):
                    self.board.title("Turn: Player Red")
                else:
                    self.board.title("Turn: Player Blue")

                self.draw()

        #print " "
        #print "%d  %d" % (x,y)        
        #print "Press_Count: %d" % (CreatBoard.pressed_count)
        #print self.old_coord
        #print " "
        
        # Light Red: '#%02x%02x%02x' % (255, 229, 204)
        # ReD: '#%02x%02x%02x' % (255, 0, 0)
        # Blue: '#%02x%02x%02x' % (0, 0, 255)
        # Light Blue: '#%02x%02x%02x' % (204, 204, 255)

    def draw(self):
        board = self.game.getBoard()
        for c_x in range(self.N):
			tmp = ""
			for c_y in range(self.N):
				if "0*" == board[(c_x,c_y)]:
					#print "LightRed"
					self.all_buttons[c_x][c_y]['bg'] = '#%02x%02x%02x' % (255, 229, 204)
				elif "1*" == board[(c_x,c_y)]:
					#print "LightBlue"
					self.all_buttons[c_x][c_y]['bg'] = '#%02x%02x%02x' % (204, 204, 255)
				elif " " == board[(c_x,c_y)]:
					#print "Clear"
					self.all_buttons[c_x][c_y]['bg'] = '#%02x%02x%02x' % (216, 216, 216)
				elif len(str(board[(c_x,c_y)])) == 1:
					p_id = int(board[(c_x,c_y)])
					#print p_id
					self.all_buttons[c_x][c_y]['bg'] = '#%02x%02x%02x' % (255*abs(p_id-1), 0, p_id*255)
				else:
					#print "Green"
					self.all_buttons[c_x][c_y]['bg'] = '#%02x%02x%02x' % (0, 255, 0)


if __name__ == "__main__":
    cw = CellWars()
    cw.title("Cell Wars")
    cw.geometry("300x350")
    cw.mainloop()
