
x=[["_","_","_"],
["_","_","_"],
["_","_","_"]]
while True:
    for i in range(len(x)):
        print()
        for k in range(len(x[i])):
            print(x[i][k], end=" ")
    placement1= int(input("\n\nWhich x coordinate?\n\n"))
    placement2= int(input("\n\nWhich y coordinate?\n\n"))
    x[placement1][placement2]= ("x")
    for i in range(len(x)):
        print()
        for k in range(len(x[i])):
            print(x[i][k], end=" ")
    placement1= int(input("\n\nWhich x coordinate?\n\n"))
    placement2= int(input("\n\nWhich y coordinate?\n\n"))
    x[placement1][placement2]= ("o")
    