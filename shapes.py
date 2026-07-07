while True:
    size= input("\nsize?\n")
    for i in range(int(size)):
        print("")
        for s in range(int(size)-i):
            print("  ", end="")
        for k in range(i):
            print("_ _ ", end="")
    for l in range(int(size)):
        print("")
        for d in range(l):
            print("  ", end="")
        for o in range(int(size)-l):
            print("_ _ ", end="")

        