#main
player1 = input ("Player 1, please enter a name: ")
player2 = input ("Player 2, please enter a name: ")

players = [player1, player2]
players.sort()

for i in players:
    print (players[0]+", you are X!")
    print (players[1]+", you are O!")
    break

row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]

board = [row1, row2, row3]
rows = 3

def turn_x():
    row = int(input (players[0]+", pick a row: "))
    column = int(input (players[0]+", please pick a column: ")) -1
    if row == 1 and row1[column] != "X" and row1[column] != "O":
        row1[column] = row1[column].replace(" ", "X")

    elif row == 2 and row2[column] != "X" and row2[column] != "O":
        row2[column] = row2[column].replace(" ", "X")
    
    elif row == 3 and row3[column] != "X" and row3[column] != "O":
        row3[column] = row3[column].replace(" ", "X")

    else:
        print ("Sorry, try again.")
        turn_x()

    return

def turn_o():
    row = int(input (players[1]+", pick a row: "))
    column = int(input (players[1]+", please pick a column: ")) - 1
    if row == 1 and row1[column] != "X" and row1[column] != "O":
        row1[column] = row1[column].replace(" ", "O")
        
    elif row == 2 and row2[column] != "X" and row2[column] != "O":
        row2[column] = row2[column].replace(" ", "O")
    
    elif row == 3 and row3[column] != "X" and row3[column] != "O":
        row3[column] = row3[column].replace(" ", "O")

    else:
        print ("Sorry, try again.")
        turn_o()

    return

def wingame():
    w = 0
    if row1[0] == row1[1] == row1[2]:
        if row1[0] != " ":
            w = w + 1
    elif row2[0] == row2[1] == row2[2]:
        if row2[0] != " ":
            w = w + 1
    elif row3[0] == row3[1] == row3[2]:
        if row3[0] != " ":
            w = w + 1
    elif row1[0] == row2[0] == row3[0]:
        if row1[0] != " ":
            w = w + 1
    elif row1[1] == row2[1] == row3[1]:
        if row1[1] != " ":
            w = w + 1
    elif row1[2] == row2[2] == row3[2]:
        if row1[2] != " ":
            w = w + 1
    elif row1[0] == row2[1] == row3[2]:
        if row1[0] != " ":
            w = w + 1
    elif row1[2] == row2[1] == row3[0]:
        if row1[2] != " ":
            w = w + 1
            
    return w

def show_board():
    print (row1)
    print (row2)
    print (row3)

    return

def game():
    while wingame() == 0:
        turn_x()
        show_board()
        if wingame() == 1:
            print (players[0]+" won the game!")
            break
        else:
            turn_o()
            show_board()
            if wingame() == 1:
                print (players[1]+" won the game!")
                break

    return

game()

