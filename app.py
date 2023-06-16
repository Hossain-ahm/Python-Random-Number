import random
from tkinter import *
from tkinter import ttk


def random_Numbers(len,min,max):
    numbers = []
    for i in range(int(len)):
        numbers.append(random.randint(int(min),int(max)))
    return numbers


def random_Number():

    min = float(min1.get())
    max = float(max1.get())

    randomNumber.set(random.randint(int(min),int(max)))

def random_SetOfNumber():
    print("Give me how much random number would you like:")
    len = input("length: ")
    print("What are the minimum and maximum values you would like")
    
    min = input("min: ")
    max = input("max: ")
    
    numbers = random_Numbers(len,min,max)
    return numbers


root = Tk()
#the titlte of the app
root.title("Random numbers")

#the main frame all the widgets will be placed inside
topframe = ttk.Frame(root, padding=(3,3,12,12))
topframe.grid(column=0, row=0)

#field to put the min input for singular random number
min1 = StringVar()
min1_entry = ttk.Entry(topframe, textvariable=min1)
ttk.Label(topframe, text="minimum number").grid(column=0, row=1)
min1_entry.grid(column=1, row=1)


#field to put the max input for singular random number
max1 = StringVar()
max1_entry = ttk.Entry(topframe, textvariable=max1)
ttk.Label(topframe, text="maximum number").grid(column=2, row=1)
max1_entry.grid(column=3, row=1)


ttk.Label(topframe, text="Random number").grid(column=0, row=0)
#A button when preseed will give the random number
ttk.Button(topframe, text="Calculate",command=random_Number).grid(column=0, row=2, sticky=W)

randomNumber = StringVar()
ttk.Label(topframe, textvariable=randomNumber).grid(column=2, row=2, sticky=(W, E))


root.mainloop()
