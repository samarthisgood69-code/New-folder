print("full pyramid pattern of stars(*): " )
s = int(input("enter the number of rows "))
for v in range(s):
    for w in range(v+1):
        print( "*", end="")
    print()