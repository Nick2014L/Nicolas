import os
b= [["⚪","⚪","⚪","⚪","⚪","⚪","⚪"],
    ["⚪","⚪","⚪","⚪","⚪","⚪","⚪"],
    ["⚪","⚪","⚪","⚪","⚪","⚪","⚪"],
    ["⚪","⚪","⚪","⚪","⚪","⚪","⚪"],
    ["⚪","⚪","⚪","⚪","⚪","⚪","⚪"],
    ["⚪","⚪","⚪","⚪","⚪","⚪","⚪"]]
def horizontal():
    for i in range(6):
        for k in range(4):
            if b[i][k]== "🔴" and b[i][k+1]== "🔴" and b[i][k+2]== "🔴" and b[i][k+3]== "🔴":
                return 1
            if b[i][k]== "🟡" and b[i][k+1]== "🟡" and b[i][k+2]== "🟡" and b[i][k+3]== "🟡":
                return 2
def vertical():
    for i in range(3):
        for k in range(7):
            if b[i][k]== "🔴" and b[i+1][k]== "🔴" and b[i+2][k]== "🔴" and b[i+3][k]== "🔴":
                return 1
            if b[i][k]== "🟡" and b[i+1][k]== "🟡" and b[i+2][k]== "🟡" and b[i+3][k]== "🟡":
                return 2
def checkWins():
    if horizontal()== 1 or vertical()== 1:
        print("Player1 is the WINNER!!!")
    elif horizontal()== 2 or vertical== 2:
        print("Player2 is the WINNER!!!")
def printb():
    os.system("cls")
    print("      CONNECT 4\n\n\n")
    checkWins()
    print("\n\n\n 0  1  2  3  4  5  6 ", end= "")
    for i in range(len(b)):
        print()
        for k in range(len(b[i])):
            print(b[i][k], end=" ")
def place(p,emoji):
    for s in range(5,-1,-1):
        if b[s][p]== ("⚪"):
            b[s][p]= (emoji)
            break
while True:
    p=-1
    while (p<0) or (p>6):
        printb()
        p= int(input("\n\nPlayer1, where do you want to place your piece?\n\n"))
    place(p,"🔴")
    p=-1
    while (p<0) or (p>6):
        printb()
        p= int(input("\n\nPlayer2, where do you want to place your piece?\n\n"))
    place(p,"🟡")  
