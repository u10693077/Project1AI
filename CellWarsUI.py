from tkinter import *

class cwStart():

    def __init__(self):

        def createGrid():
            cwPlay().run()

        def getMatrixSize():
            if matrixSize.get().strip() == "":
                messagebox.showerror("Menu", "Please Enter Grid Size (even number >8)")
            else:
                mSize = matrixSize.get().strip()
                createGrid() 

       # self.cw = Tk()
       # self.cw.title('Menu')
       # self.button = Button(self.cw, text="Start", fg="red", command=createGrid)
       # self.button.pack()    
       # self.cw.mainloop()
        self.cw = Tk()
        global entryWidget
        self.cw.title('Menu')
        self.cw["padx"] = 40
        self.cw["pady"] = 20       

        # Create a text frame to hold the text Label and the Entry widget
        textFrame = Frame(self.cw)
        
        #Create a Label in textFrame
        matrixSizeLabel = Label(textFrame)
        matrixSizeLabel["text"] = "Grid Size (even number >8):"
        matrixSizeLabel.pack(side=LEFT)

        # Create an Entry Widget in textFrame
        matrixSize = Entry(textFrame)
        matrixSize["width"] = 25
        matrixSize.pack(side=LEFT)

        textFrame.pack()

        button = Button(self.cw, text="Start", command=getMatrixSize)
        button.pack() 


class cwPlay():

    def __init__(self):


        self.matrix = [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ]

        '''for i in range(mSize):
            for j in range(mSize):
                c = table[i][j]'''
    

        self.all_buttons = []

        self.cw = Tk()
        self.cw.title('Cell Wars')

        #self.long_x = len(self.matriz)

        #self.long_y = len(self.matriz[0])

        self.creatMatrix()

    def run(self):
        self.cw.mainloop()


    def creatMatrix(self):
        for y, row in enumerate(self.matrix):
            buttons_row = []
            for x, element in enumerate(row):
                boton = Button(self.cw, width=10, height=5, command=lambda a=x,b=y: self.onButtonPressed(a,b))
                boton.grid(row=y, column=x)
                buttons_row.append( boton )
            self.all_buttons.append( buttons_row )

    def onButtonPressed(self, x, y):
        print( "pressed: x=%s y=%s" % (x, y) )
        if self.all_buttons[y][x]['bg'] == 'red':
            self.all_buttons[y][x]['bg'] = 'green'
        else:
            self.all_buttons[y][x]['bg'] = 'red'

#cwPlay().run()

cwStart()
