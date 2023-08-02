winner=None
state=[ [' ',' ',' '],[' ',' ',' '],[' ',' ',' ']] #initialise empty board in global list state

def display_board():
    print("\n\n***************")
    print("*  {} | {} | {}  *".format(state[0][0], state[0][1], state[0][2]))
    print("*-------------*")
    print("*  {} | {} | {}  *".format(state[1][0], state[1][1], state[1][2]))
    print("*-------------*")
    print("*  {} | {} | {}  *".format(state[2][0], state[2][1], state[2][2]))
    print("***************")


def check_win():
    pass


def player_input(player):
    print(f"Player {player}'s turn")

    success=False
    while success==False:
        row=int(input("Enter row: "))
        col=int(input("Enter column: "))

        if state[row][col]==" ":
            state[row][col]=player
            success=True
        else:
            print("Enter empty row and column please \n")


def check_win():
    win=False
    # check row
    for i in range(3):
        if state[i][0]==state[i][1]==state[i][2]!=" ":
            winner=state[i][0]
            return winner
        
    # check columns
    for j in range(3):
        if state[0][j]==state[1][j]==state[2][j]!=" ":
            winner=state[0][j]
            return winner

    # check diagonals
    if state[0][0]==state[1][1]==state[2][2]!=" ":
        winner=state[1][1]
        return winner
    
    if state[0][2]==state[1][1]==state[2][0]!=" ":
        winner=state[1][1]
        return winner

    return win


def check_board_full():
    full=True
    for i in range(3):
        for j in range(3):
            if state[i][j]==" ":
                full=False
    return full




def play():
    print("Welcome to Tic Tac Toe!")
    display_board() #display initial board

    players=['X','O']
    while True:
        for player in players:
           #Player input
           player_input(player) 

           #display board
           display_board() 
            
            #check if player won
           winning_player=check_win()
           if winning_player!=False:
               print(f"Player {winning_player} won!")
               exit()
            
            #check if board is full
           if check_board_full()==True:
             print("Board is full. Game over")
             exit()


play()

