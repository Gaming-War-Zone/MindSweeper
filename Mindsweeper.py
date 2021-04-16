import numpy as np
import random
import math
import time

#--------------------------FUNCTIONS------------------------------------------------------------------------

# function to explain rules before game board
def RULES():
    print(" Welcome to Minesweeper!\n")
    print("Rule 1 - Each co-ordinate represents a space - No. 1-9 represent bomb promiximity\n")
    print("Rule 2 - Avoid all the bombs - bombs are represented by 10\n")
    print("Rule 3 - Bomb are placed randomly - No. 0 has no bombs surrounding it\n")
    print("Rule 4 - Expose all the empty spaces - empty spaces are represented by -8\n")
    print("Goodluck!\n")

# function to print credits at end of game


# function to determine size and difficulty
def boardSizeDifficulty():
    while selection == False:
        print("Option A = 4x4")
        print("Option B = 6x6")
        print("Option C = 8x8")
        user_input = int(input("Enter 1 for option A, 2 for Option B and 3 for Option C: "))
        if user_input == 1:
            selection = True
        elif user_input == 2:
            selection = True
        elif user_input == 3:
            selection = True
        else: 
            selection = False


# function to reset all numbers to 0 for game array
def resetValues(arr):
    for i in range(0,len(arr)): #set range to loop through the array
        if arr[i] < 1000:   # any number smaller than 1000 are changed to 0
            arr[i] = 0

# function to reset all numbers to -8 for show array
def resetValuesNeg(arr):
    for i in range(0,len(arr)): #set range to loop through the array
        if arr[i] < 1000:   # any number smaller than 1000 are changed to 0
            arr[i] = -8

# function to generate bombs on game array
def bombCreate(arr):
    bombCounter = 8 # bomb counter to be set to however many bombs the user chooses
    bombLimit = False 
    while bombLimit == False:
        for d in range(0,len(arr)):
            randNum = random.randint(0, 100)    # generate random number between 0 & 100
            if randNum <= 5 and arr[d] != 10:   # if random number is below 5 (5%), the value of array element becomes the bomb 
                arr[d] = 10 # 10 is the number that denotes the bomb
                bombCounter = bombCounter - 1   # remove 1 from counter for every bomb created
            if bombCounter == 0:    # break out of loop when there's no counters left
                bombLimit = True    
                break

# function to generate proximity counter numbers on game array
def bombProxNumbersGenerator(arr):
    for c in range(0,len(arr)): # loop through 
        bombProxCounter = 0
        if c >= 1 and c - 1 < len(arr):
            if arr[c - 1] == 10:
                bombProxCounter = bombProxCounter + 1
        if c >= 8 and c - 9 < len(arr):
            if arr[c - 9] == 10:
                bombProxCounter = bombProxCounter + 1
        if c >= 7 and c - 8 < len(arr):
            if arr[c - 8] == 10:
                bombProxCounter = bombProxCounter + 1
        if c >= 6 and c - 7 < len(arr):
            if arr[c - 7] == 10:
                bombProxCounter = bombProxCounter + 1
        if c >= 0 and c + 1 < len(arr):
            if arr[c + 1] == 10:
                bombProxCounter = bombProxCounter + 1
        if c >= 0 and c + 7 < len(arr):
            if arr[c + 7] == 10:
                bombProxCounter = bombProxCounter + 1
        if c >= 0 and c + 8 < len(arr):
            if arr[c + 8] == 10:
                bombProxCounter = bombProxCounter + 1
        if c >= 0 and c + 9 < len(arr):
            if arr[c + 9] == 10:
                bombProxCounter = bombProxCounter + 1
        if arr[c] != 10:
            arr[c] = bombProxCounter

# function to generate bomb proximity numbers
def bombProxNumbersGenerator16(arr):
    for c in range(0,len(arr)):
        bombProxCounter = 0
        # if c >= 0 and <= 9
        if c >= 1 and c - 1 < len(arr):
            if arr[c - 1] == 10:
                bombProxCounter = bombProxCounter + 1
        if c >= 8 and c - 9 < len(arr):
            if arr[c - 9] == 10:
                bombProxCounter = bombProxCounter + 1
        if c >= 7 and c - 8 < len(arr):
            if arr[c - 8] == 10:
                bombProxCounter = bombProxCounter + 1
        if c >= 6 and c - 7 < len(arr):
            if arr[c - 7] == 10:
                bombProxCounter = bombProxCounter + 1
        if c >= 0 and c + 1 < len(arr):
            if arr[c + 1] == 10:
                bombProxCounter = bombProxCounter + 1
        if c >= 0 and c + 7 < len(arr):
            if arr[c + 7] == 10:
                bombProxCounter = bombProxCounter + 1
        if c >= 0 and c + 8 < len(arr):
            if arr[c + 8] == 10:
                bombProxCounter = bombProxCounter + 1
        if c >= 0 and c + 9 < len(arr):
            if arr[c + 9] == 10:
                bombProxCounter = bombProxCounter + 1
        if arr[c] != 10:
            arr[c] = bombProxCounter
# function to check if inputs are valid
def inputCheck(x,y):
    check = True
    if x >= 0 and x < reshapeSize - 1 and y >= 0 and y < reshapeSize - 1:
        print ("Coordinate inputs are valid")     
    else:
        print ("Coordinate inputs are invalid")
        check = False
    return check

#--------------------------MAIN FUNCTION------------------------------------------------------------------------
    
# Game variables
list1 = []
list2 = []
start = time.time()
moveCounter = 0
boardSize = 64
reshapeSize = 8   

# Game array
arrMineNum = np.arange(boardSize) # create array of elements
resetValues(arrMineNum) # call reset function to set all values to 0
bombCreate(arrMineNum) # call bomb create function to create bombs
bombProxNumbersGenerator(arrMineNum) # call bomb proximity number function to generate bomb proximity numbers
arrMineNum = arrMineNum.reshape(reshapeSize,reshapeSize)    # resize into 2d array of 8 rows of 8 elements

# show array
arr = np.arange(boardSize) # create array of elements
resetValuesNeg(arr) # call reset array to set all values to 0
arr = arr.reshape(reshapeSize,reshapeSize)  # resize into 2d array of 8 rows of 8 elements
RULES() # calls rules function 
print(arr)
#print(arrMineNum)

gameOver = False
movesCounter = 0
#movesCounter = 53 # To test Win Condition
while gameOver == False:
    x,y =  input("Enter your co-ordinates: ").split()
    X,Y = (x,y)

    print("Row: " + x)
    print("Element: " + y)
    check = inputCheck(int(x),int(y)) # calls input check function
    if check != True:   # if user input is false, restart loop
        print("Try again")
        continue
    coord = arr[int(x),int(y)]
    #print (coord)
    User_input = (X,Y)
    arr[int(x),int(y)] = arrMineNum[int(x),int(y)]
 

    moveCounter += 1 
    #movesCounter = movesCounter + 1
    print(arr)
    print("Moves: " + str(moveCounter))
    # Fail condition
    if arr[int(x),int(y)] == 10:
        print ("Boom! You've hit the landmine in " + str(moveCounter) + " moves.")
        end = time.time()
        print ("The game has been running for " , round((end-start)) , " seconds\n") # Timer code block
        print ("    GAME OVER")
        credits()   # calls credits function 
        gameOver = True
        break

    # Duplicate move check 
    if User_input  in list1:
       moveCounter -=1
       print("You've played move before")
       continue
    else:
       list1.append(User_input)

    # Win condition
    if moveCounter == 64 - 8:
        print ("Congratulations, You WIN!")  # if moves counter = 64 - 8, win game
        credits()   # calls credits function
        gameOver = True
        break

