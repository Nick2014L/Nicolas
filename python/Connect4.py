import os
b= [["⚪","⚪","⚪","⚪","⚪","⚪","⚪"],
    ["⚪","⚪","⚪","⚪","⚪","⚪","⚪"],
    ["⚪","⚪","⚪","⚪","⚪","⚪","⚪"],
    ["⚪","⚪","⚪","⚪","⚪","⚪","⚪"],
    ["⚪","⚪","⚪","⚪","⚪","⚪","⚪"],
    ["⚪","⚪","⚪","⚪","⚪","⚪","⚪"]]
def draw():
    for i in range(6):
         for k in range(7):
              if b[i][k]== "⚪":
                   return False
    return True
def diagonalR():
    for i in range(3):
         for k in range(4):
            if b[i][k]== "🔴" and b[i+1][k+1]== "🔴" and b[i+2][k+2]== "🔴" and b[i+3][k+3]== "🔴":
                        return 1
            if b[i][k]== "🟡" and b[i+1][k+1]== "🟡" and b[i+2][k+2]== "🟡" and b[i+3][k+3]== "🟡":
                        return 2
def diagonalL():
    for i in range(3):
         for k in range(3,7):
            if b[i][k]== "🔴" and b[i+1][k-1]== "🔴" and b[i+2][k-2]== "🔴" and b[i+3][k-3]== "🔴":
                        return 1
            if b[i][k]== "🟡" and b[i+1][k-1]== "🟡" and b[i+2][k-2]== "🟡" and b[i+3][k-3]== "🟡":
                        return 2
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
    if horizontal()== 1 or vertical()== 1 or diagonalL()== 1 or diagonalR()== 1:
        print("\n\nℙ𝕝𝕒𝕪𝕖𝕣𝟙 𝕚𝕤 𝕥𝕙𝕖 𝕎𝕀ℕℕ𝔼ℝ!!!\n\n")
        quit()
    elif horizontal()== 2 or vertical== 2 or diagonalL()== 2 or diagonalR()== 1:
        print("\n\nℙ𝕝𝕒𝕪𝕖𝕣𝟚 𝕚𝕤 𝕥𝕙𝕖 𝕎𝕀ℕℕ𝔼ℝ!!!\n\n")
        quit()
    elif draw():
         print("\n\n      Tie!!!")
def printb():
    os.system("cls")
    print("      \u001b[33m𝘾𝙤𝙣𝙣𝙚𝙘𝙩 4\u001b[0m\n")
    print("\n 𝟘  𝟙  𝟚  𝟛  𝟜  𝟝  𝟞\u001b[44m", end= "")
    for i in range(len(b)):
        print()
        for k in range(len(b[i])):
            print(b[i][k], end=" ")
    print("\u001b[0m")
def place(p,emoji):
    for s in range(5,-1,-1):
        if b[s][p]== ("⚪"):
            b[s][p]= (emoji)
            break
while True:
    p=-1
    while (p<0) or (p>6):
        printb()
        checkWins()
        p= int(input("\n\nℙ𝕝𝕒𝕪𝕖𝕣𝟙, 𝕨𝕙𝕖𝕣𝕖 𝕕𝕠 𝕪𝕠𝕦 𝕨𝕒𝕟𝕥 𝕥𝕠 𝕡𝕝𝕒𝕔𝕖 𝕪𝕠𝕦𝕣 𝕡𝕚𝕖𝕔𝕖?\n\n"))
    place(p,"🔴")
    p=-1
    while (p<0) or (p>6):
        printb()
        checkWins()
        p= int(input("\n\nℙ𝕝𝕒𝕪𝕖𝕣𝟚, 𝕨𝕙𝕖𝕣𝕖 𝕕𝕠 𝕪𝕠𝕦 𝕨𝕒𝕟𝕥 𝕥𝕠 𝕡𝕝𝕒𝕔𝕖 𝕪𝕠𝕦𝕣 𝕡𝕚𝕖𝕔𝕖?\n\n"))
    place(p,"🟡")  
