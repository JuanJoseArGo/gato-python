from random import randrange
llenos=[]
ganar=[]
valor=1

board =[[1 for r in range(3)] for f in range(3)]
for i in range(3):
    for j in range(3):
        board[i][j]=valor
        valor+=1

def Tie(board):
    contador=0
    for i in range(3):
        for i in range(3):
            if board[i][j]=='X' or board[i][j]=='O':
                contador+=1
            else:
                continue
    return contador

def DisplayBoard(board):
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   ",board[0][0]," |   ",board[0][1]," | ",board[0][2],"   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   ",board[1][0]," |   ",board[1][1]," | ",board[1][2],"   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   ",board[2][0]," |   ",board[2][1]," | ",board[2][2],"   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("\n\n")

def EnterMove(board):
    num = int(input("Dame la celda que eliges"))
    for i in range(3):
        for j in range(3):
            if board[i][j]==num:
                board[i][j]='X'
                llenos.append(num)
            else:
                continue

def VictoryFor(board, sign='X'):
    bandera=True
    vertical=0
    vertical2=0
    vertical3=0
    diagonal1=0
    diagonal2=0
    horizontal1=0
    horizontal2=0
    horizontal3=0
    for i in range(3):
        if board[0][i]==sign:
            horizontal1+=1
        if board[1][i]==sign:
            horizontal2+=1
        if board[2][i]==sign:
            horizontal3+=1
        if board[i][0]==sign:
            vertical+=1
        if board[i][1]==sign:
            vertical2+=1
        if board[i][2]==sign:
            vertical3+=1
        if board[i][2-i]==sign:
            diagonal2+=1
        if i==0 or i==1 or i==2:
                if board[i][i]==sign:
                    diagonal1+=1
    ganar.append(horizontal1)
    ganar.append(horizontal2)
    ganar.append(horizontal3)
    ganar.append(vertical)
    ganar.append(vertical2)
    ganar.append(vertical3)
    ganar.append(diagonal1)
    ganar.append(diagonal2)

    termina = max(ganar)
    if termina ==3:
        bandera = False
    else:
        bandera = True
    return bandera

def DrawMove(board):
    bandera=True
    while bandera:
        valNew=randrange(9)
        if valNew not in board:
            valNew=randrange(9)
        for i in range(3):
            for j in range(3):
                if valNew==board[i][j]:
                    board[i][j]='O'
                    bandera=False
                else:
                    continue

aux=True
while aux:
    DisplayBoard(board)
    EnterMove(board)
    aux1 = VictoryFor(board,'X')
    if aux1==False:
        print("Ganaste buapo uwu")
        aux=False
        break
    if Tie(board)==9:
        print("Es EMPATE chiale")
        break
    DisplayBoard(board)
    DrawMove(board)
    aux2 = VictoryFor(board,'O')
    if aux2==False:
        DisplayBoard(board)
        print("Te ganaron papu uwu")
        aux = False
        break
    ganar.clear()
    