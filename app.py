import random
import tkinter as tk


def random_Numbers(len,min,max):
    numbers = []
    for i in range(int(len)):
        numbers.append(random.randint(int(min),int(max)))
    return numbers


def random_Number():
    print ("Give me a min and a max value and I will give you a random number inbetween")

    min = input("min: ")
    max = input("max: ")

    return random.randint(int(min),int(max))

def random_SetOfNumber():
    print("Give me how much random number would you like:")
    len = input("length: ")
    print("What are the minimum and maximum values you would like")
    
    min = input("min: ")
    max = input("max: ")
    
    numbers = random_Numbers(len,min,max)
    return numbers

