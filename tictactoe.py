# Setup
row1 = ["a1", "a2", "a3"]
row2 = ["b1", "b2", "b3"]
row3 = ["c1", "c2", "c3"]

# Methods
def replaceRow(symbol, box): # Replaces a blank space with an X or an O
    turnDone = False
    if box == "a1": # Top left
        if row1[0] == "X" or row1[0] == "O":
            print("Box is already taken!")
        else:
            row1[0] = symbol
            turnDone = True
    elif box == "a2": # Top middle
        if row1[1] == "X" or row1[1] == "O":
            print("Box is already taken!")
        else:
            row1[1] = symbol
            turnDone = True
    elif box == "a3": # Top right
        if row1[2] == "X" or row1[2] == "O":
            print("Box is already taken!")
        else:
            row1[2] = symbol
            turnDone = True
    elif box == "b1": # Middle left
        if row2[0] == "X" or row2[0] == "O":
            print("Box is already taken!")
        else:
            row2[0] = symbol
            turnDone = True
    elif box == "b2": # Center
        if row2[1] == "X" or row2[1] == "O":
            print("Box is already taken!")
        else:
            row2[1] = symbol
            turnDone = True
    elif box == "b3": # Middle right
        if row2[2] == "X" or row2[2] == "O":
            print("Box is already taken!")
        else:
            row2[2] = symbol
            turnDone = True
    elif box == "c1": # Bottom left
        if row3[0] == "X" or row3[0] == "O":
            print("Box is already taken!")
        else:
            row3[0] = symbol
            turnDone = True
    elif box == "c2": # Bottom middle
        if row3[1] == "X" or row3[1] == "O":
            print("Box is already taken!")
        else:
            row3[1] = symbol
            turnDone = True
    elif box == "c3":
        if row3[2] == "X" or row3[2] == "O":
            print("Box is already taken!")
        else:
            row3[2] = symbol
            turnDone = True
    else:
        print("Please choose a valid box!")
    
    if turnDone == True: # If a valid move was made, the turn is over, and "True" is returned back to the main code
        print(str(row1) + "\n" + str(row2) + "\n" + str(row3))
        return True

def checkWin(): # Checks for all possible scenarios for a win
    if row1[0] == "X" and row1[1] == "X" and row1[2] == "X":
        return True
    elif row2[0] == "X" and row2[1] == "X" and row2[2] == "X":
        return True
    elif row3[0] == "X" and row3[1] == "X" and row3[2] == "X":
        return True
    elif row1[0] == "X" and row2[0] == "X" and row3[0] == "X":
        return True
    elif row1[1] == "X" and row2[1] == "X" and row3[1] == "X":
        return True
    elif row1[2] == "X" and row2[2] == "X" and row3[2] == "X":
        return True
    elif row1[0] == "X" and row2[1] == "X" and row3[2] == "X":
        return True
    elif row3[0] == "X" and row2[1] == "X" and row1[2] == "X":
        return True
    elif row1[0] == "O" and row1[1] == "O" and row1[2] == "O":
        return True
    elif row2[0] == "O" and row2[1] == "O" and row2[2] == "O":
        return True
    elif row3[0] == "O" and row3[1] == "O" and row3[2] == "O":
        return True
    elif row1[0] == "O" and row2[0] == "O" and row3[0] == "O":
        return True
    elif row1[1] == "O" and row2[1] == "O" and row3[1] == "O":
        return True
    elif row1[2] == "O" and row2[2] == "O" and row3[2] == "O":
        return True
    elif row1[0] == "O" and row2[1] == "O" and row3[2] == "O":
        return True
    elif row3[0] == "O" and row2[1] == "O" and row1[2] == "O":
        return True
    else:
        return False
    
# Main Code
print("INSTRUCTIONS: Type the name of the box to put your symbol (X or O) in the box")
print(str(row1) + "\n" + str(row2) + "\n" + str(row3))

gameEnd = False
turn = 0

while gameEnd != True: # Loop breaks when the game is over, otherwise repeats over and over
    player1Finished = False
    while player1Finished != True: # Loop breaks when a "True" value is received from replaceRow()
        player1 = input("Player 1 (x), select your box:")
        player1Finished = replaceRow("X", player1)
    turn += 1
    
    gameEnd = checkWin() # Checks if Player 1 won, then ends the game
    if gameEnd == True:
        print("Player 1 wins!")
        break
    if turn == 9 and gameEnd == False: # Checks for a tie, then ends the game
        print("Tie!")
        break

    player2Finished = False
    while player2Finished != True: # Loop breaks when a "True" value is received from replaceRow()
        player2 = input("Player 2 (O), select your box:")
        player2Finished = replaceRow("O", player2)
    turn += 1

    gameEnd = checkWin() # Checks if Player 2 won, then ends the game
    if gameEnd == True:
        print("Player 2 wins!")
        break