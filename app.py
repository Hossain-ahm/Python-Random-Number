import random
from tkinter import *
from tkinter import ttk


#function that gives me string full of random numbers
def random_Numbers(len,min,max):
    numbers = ""
    for i in range(int(len)):
        if i==len-1:
            numbers = numbers + str(random.randint(int(min),int(max)))
        else:
            numbers = numbers + str(random.randint(int(min),int(max))) + ", "
    return numbers

#functions that present the random number or random numbers on the gui
def random_Number():

    min = float(min1.get())
    max = float(max1.get())

    randomNumber.set(random.randint(int(min),int(max)))

def random_SetOfNumber():
    
    min = float(min2.get())
    max = float(max2.get())
    len = float(length.get())
    
    numbers = random_Numbers(len,min,max)
    textBox.config(state='normal')
    textBox.insert("end",numbers)
    textBox.config(state='disabled')


root = Tk()
#the titlte of the app
root.title("Random numbers")

#the main frame all the widgets for just 1 random number will be stored will be placed inside
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


ttk.Label(topframe, text="Get a random number putting the min a max of what you want").grid(column=0, row=0)
#A button when preseed will give the random number
ttk.Button(topframe, text="Randomize",command=random_Number).grid(column=0, row=2, sticky=W)

#this label present the random number
randomNumber = StringVar()
ttk.Label(topframe, textvariable=randomNumber).grid(column=2, row=2, sticky=(W, E))


#the main frame all the widgets for multipe random number will be stored will be placed inside
bottomframe = ttk.Frame(root, padding=(3,3,12,12))
bottomframe.grid(column=0, row=1)

ttk.Label(bottomframe, text="Get a list of random numbers based on you min and max values").grid(column=0, row=0)


#field to put the min input for multiple random numbers
min2 = StringVar()
min2_entry = ttk.Entry(bottomframe, textvariable=min2)
ttk.Label(bottomframe, text="minimum number").grid(column=0, row=1)
min2_entry.grid(column=1, row=1)

#field to put the min input for multiple random numbers
max2 = StringVar()
max2_entry = ttk.Entry(bottomframe, textvariable=max2)
ttk.Label(bottomframe, text="minimum number").grid(column=2, row=1)
max2_entry.grid(column=3, row=1)

#field to put the amount of random random numbers
length = StringVar()
len_entry = ttk.Entry(bottomframe, textvariable=length)
ttk.Label(bottomframe, text="How many numbers").grid(column=4, row=1)
len_entry.grid(column=5, row=1)

#A button when preseed will give the random number
ttk.Button(bottomframe, text="Randomize",command=random_SetOfNumber).grid(column=0, row=2, sticky=W)

textBox = Text(bottomframe, width = 50)
textBox.grid(column=0,row=3)
textBox.config(state='disabled')


root.mainloop()
