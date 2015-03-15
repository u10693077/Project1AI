import Tkinter as tk
from Tkinter import *
import time
from random import randint

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
        gridSize.insert(0,"8")

        initialCell = tk.Entry(self, bd=5, justify=CENTER, textvariable=StringVar())
        initialCell.delete(0, END)
        initialCell.insert(0,"0")

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
        gridSize.insert(0,"8")

        labelInitialCell = tk.Label(self, text="Initial Cells:", font=12)
        initialCell = tk.Entry(self, bd=5, justify=CENTER, textvariable=StringVar())
        initialCell.delete(0, END)
        initialCell.insert(0,"0")
           
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
        gridSize.insert(0,"8")

        labelInitialCell = tk.Label(self, text="Initial Cells:", font=12)
        initialCell = tk.Entry(self, bd=5, justify=CENTER, textvariable=StringVar())
        initialCell.delete(0, END)
        initialCell.insert(0,"0")
       
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
    def __init__(self, grSize, inCell):

        self.N = int(grSize)
        self.matrix = [[0 for x in range(self.N)] for x in range(self.N)] 
        self.all_buttons = []

        self.board = Tk()
        self.board.title('Cell Wars')
        self.creatMatrix()
        CreatGameMatrix(self.N, self.matrix, inCell)
        
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


    def onButtonPressed(self, x, y):
        print "pressed: x=%s y=%s" % (x, y)
        #if self.all_buttons[y][x]['bg'] == '#%02x%02x%02x' % (0, 0, 255):
        #    self.all_buttons[y][x]['bg'] = '#%02x%02x%02x' % (204, 204, 255)
        #else:
        #    self.all_buttons[y][x]['bg'] = '#%02x%02x%02x' % (0, 0, 255)

        #Light Red: '#%02x%02x%02x' % (255, 229, 204)
        #ReD: '#%02x%02x%02x' % (255, 0, 0)
        #Blue: '#%02x%02x%02x' % (0, 0, 255)
        #Light Blue: '#%02x%02x%02x' % (204, 204, 255)



class CreatGameMatrix():
    def __init__(self, grSize, guiMat, inCell):
        self.N = int(grSize)
        self.initCell = int(inCell)
        self.matrixGame = [["0" for x in range(self.N)] for x in range(self.N)]

        for i in range(self.initCell):
            #self.matrixGame[0][0] = "5"
            self.matrixGame[randint(1,(self.N/2)-1)][randint(1,(self.N/2)-1)] = "A"
            self.matrixGame[randint((self.N/2)+1, self.N-1)][randint((self.N/2)+1, self.N-1)] = "B"
            
        Update(guiMat, self.matrixGame, grSize)
        

class Update():
    def __init__(self, matrixGui, matrixGame, grSize):

        for i in range(grSize):
            for j in range(grSize):
                if matrixGame[i][j] == "A":
                    print ""
                    
                if matrixGame[i][j] == "B":    
                    print ""
            
        print "GUIMatrix"
        print matrixGui
        print "GameMatrix"
        print matrixGame
        
        
if __name__ == "__main__":
    cw = CellWars()
    cw.title("Cell Wars")
    cw.geometry("300x350")
    cw.mainloop()
