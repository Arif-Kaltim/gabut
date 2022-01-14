from tkinter import *
import pygame
from tkinter.filedialog import *



root = Tk()
root.title("Test Sound")
frame = Frame(root,bd=2,relief=SOLID,bg="black")
frame.pack()

fileName = askopenfilename(filetypes=(("audio mp3","*.mp3"),("All Files","*.*")))
pygame.mixer.init()
pygame.mixer.music.load("{}".format(fileName))
pygame.mixer.music.play(loops=0)

label = Text(frame,width=50,height=10,font="Times 6",bg="black",fg="white")
label.insert(END,fileName)
label.insert(END,"\n")
label.insert(END,"-"*86)
label.insert(END,"\n")
label.insert(END,"Powered By : Arif©2022")
label.pack()
def stop():
    pygame.mixer.music.stop()
    sys.exit()
Button(frame,text="Stop",font="Times 6",bg="black",fg="white",command=stop).pack(side=LEFT)
root.mainloop()