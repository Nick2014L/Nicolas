from time import sleep
while True:
    shape= input("\nWhich shape?\n")
    if shape== ("Square"):
        hollow= input("1. Hollow 2. Not hollow?\n")
        if hollow== ("1"):
            size= input("\nsize?\n")
            for i in range(int(size)):
                print("")
                for k in range(int(size)):
                    if i== 0 or i== int(size)-1 or k== 0 or k== int(size)-1:
                        print("x ",end="")
                    else:
                        print("  ", end="")
        elif hollow== ("2"):
            size= input("\nsize?\n")
            for i in range(int(size)):
                print("")
                for k in range(int(size)):
                    print("x ", end="")
        else:
            print("There is a problem with your compter:(")
    elif shape== ("Diamond"):
        hollow= input("1. Hollow 2. Not hollow?\n")
        if hollow== ("2"):
            size= input("\nsize?\n")
            for i in range(int(size)):
                print("")
                for s in range(int(size)-i):
                    print("  ", end="",flush=True)
                for k in range(i):
                    print("x x ", end="",flush=True)
                    sleep (0.01)
            for l in range(int(size)):
                print("")
                for d in range(l):
                    print("  ", end="", flush=True)
                for o in range(int(size)-l):
                    print("x x ", end="", flush=True)
                    sleep (0.01)
        elif hollow== ("1"):
            size= input("\nsize?\n")
            for i in range(int(size)):
                print("")
                for s in range(int(size)-i):
                    print("  ", end="",flush=True)
                for k in range(i):
                    if k== (0) or k== (i-1):
                        print("x   ", end="", flush=True)
                        sleep (0.01)
                    else:
                        print("    ", end="", flush=True)
            for l in range(int(size)):
                print("")
                for d in range(l):
                    print("  ", end="", flush=True)
                for o in range(int(size)-l):
                    if o== (0) or o== (int(size)-l-1):
                        print("x   ", end="", flush=True)
                        sleep (0.01)
                    else:
                        print("    ", end="", flush=True)


