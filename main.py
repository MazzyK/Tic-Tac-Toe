
# Function: display(mat)
#==========================================
#Purpose:
#   display current state of tic tac toe matrix
#Input Parameter(s):
#   takes in the current state of the matrix
#Returns:
#   no return value
#==========================================

def display(mat):
    for i in range (0,3):
        print(mat[i][0],end=' ')
        print(mat[i][1],end=' ')
        print(mat[i][2])

# Function: is winner(mat)
#==========================================
#Purpose:
#   to assess if it's a winning move
#Input Parameter(s):
#   takes in the current state of the matrix
#Returns:
#   win: a boolean value to determine if the move was a winning one
#Notes:
#   mat[i][0]!=0 condition set because unplayed positions are marked with a 0
#==========================================

def is_winner(mat):
    win = False
    for i in range(0, 3):
        if mat[i][0] == mat[i][1] and mat[i][1] == mat[i][2] and mat[i][0] != 0:
            win = True
            break
        elif mat[0][i] == mat[1][i] and mat[1][i] == mat[2][i] and mat[0][i] != 0:
            win = True
            break
        elif mat[0][0] == mat[1][1] and mat[1][1] == mat[2][2] and mat[0][0] != 0:
            win = True
            break
        else:
            pass
    return win

# Function: play_move(mat)
#==========================================
#Purpose:
#   main part of game + error handling
#Input Parameter(s):
#   takes in the current state of the matrix
#Returns:
#   mat: the updated matrix
#==========================================

def play_move(mat):
    loop = True
    last_played=''
    display(mat)
    while loop:
        row = int(input("Enter row you wish to play:"))
        pos = int(input("Enter position you wish to play:"))
        move = input("Enter x or o:")

        if move == last_played:
            print("you can't play {} again".format(move))
        else:
            last_played=move
            if mat[row][pos]!=0:
                print("That is not a valid move!")
                continue
            else:
                mat[row][pos] = move
                if is_winner(mat):
                    print("You win!")
                    display(mat)
                    break
                else:
                    pass
            display(mat)
    return mat


matrix=[[0,0,0],[0,0,0],[0,0,0]]

play_move(matrix)
