#Cicso Final Project
# play tic-tac-toe Game
print("=== play tic-tac-toe Game===")

board=[1,2,3,4,5,6,7,8,9]
def display_board(board):
    print(board[0],"|",board[1],"|",board[2])
    print("----------") 
    print(board[3],"|",board[4],"|",board[5])
    print("----------")
    print(board[6],"|",board[7],"|",board[8])
display_board(board)

#User move
def enter_move():
    print("===User Chance===")
    move=int(input("Enter your position 1-9 :"))
    
    if board[move-1]!="X" and board[move-1]!="O":
        board[move-1]="O"
    else:
        print("Position already Occupied!")
    
    display_board(board)
enter_move()

#Computer move
def computer_move():
    print("===Computer Chance===")
    import random
    move = random.randint(1,9)

    free_position=[]
    for i in range(9):
        if board[i]!="X" and board[i]!="O":
            free_position.append(i)
    move=random.choice(free_position)
    board[move]="X"
    display_board(board)
computer_move()

#Check Winner
#Computer win
def computer_win():
    if board[0]==board[1]==board[2]=="X":
        print("**Computer WIN**")
        return True
    elif board[3]==board[4]==board[5]=="X":
        print("**Computer WIN**")
        return True
    elif board[6]==board[7]==board[8]=="X":
        print("**Computer WIN**")
        return True
    elif board[0]==board[3]==board[6]=="X":
        print("**Computer WIN**")
        return True
    elif board[1]==board[4]==board[7]=="X":
        print("**Computer WIN**")
        return True
    elif board[2]==board[5]==board[8]=="X":
        print("**Computer WIN**")
        return True
    elif board[0]==board[4]==board[8]=="X":
        print("**Computer WIN**")
        return True
    elif board[2]==board[4]==board[6]=="X":
        print("**Computer WIN**")
        return True
    return False
computer_win()    

#User Win

#Game Loop
def user_win():
    if board[0]==board[1]==board[2]=="O":
        print("**You WIN**")
        return True
    elif board[3]==board[4]==board[5]=="O":
        print("**You WIN**")
        return True
    elif board[6]==board[7]==board[8]=="O":
        print("**You WIN**")
        return True
    elif board[0]==board[3]==board[6]=="O":
        print("**You WIN**")
        return True
    elif board[1]==board[4]==board[7]=="O":
        print("**You WIN**")
        return True
    elif board[2]==board[5]==board[8]=="O":
        print("**You WIN**")
        return True
    elif board[0]==board[4]==board[8]=="O":
        print("**You WIN**")
        return True
    elif board[2]==board[4]==board[6]=="O":
        print("**You WIN**")
        return True
    return False
user_win()
    
#Final structure    
while True:
    enter_move()
    
    if user_win():
        break
    
    computer_move()
    
    if computer_win():
        break
    
    #Match Draw
    free_position=[]
    
    for i in range(9):
        if board[i]!="O" and board[i]!="X":
            free_position.append(i)
            
    if len(free_position)==0:
        print("====Match Draw====")        
        break 