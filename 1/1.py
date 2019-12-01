import math
import sys
import time

sys.setrecursionlimit(100000)

file = open("1/input.txt", "r")

def calculatefuel(mass):
    global totalfuel
    divided = int(mass)/3
    rounded = math.floor(divided)
    if rounded > 2:
        fuelneeded = rounded - 2
        totalfuel = totalfuel + fuelneeded
        calculatefuel(fuelneeded)

def calculateinput():
    global totalfuel
    totalfuel = 0
    for mass in file:
        calculatefuel(mass)
    print(totalfuel)

calculateinput()