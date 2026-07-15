from random import randint
x= [4,1,68,34,2,4,6,43,6,4,6,3,6,6,3,3,5,6,76,4,3,3,5,6,43,6,6,3,66,4,6,45,7,4,6,8,4,6,3,2]
while True:
    x.append(randint(1,100))
    print(x)
    for k in range(len(x)):
        for i in range(len(x)-1):
            if x[i] > x[i+1]:
                t= x[i]
                x[i]= x[i+1]
                x[i+1]= t