def Tree():
    row = int((input("How large should the tree be? ")))
    for x in range(row):
        x+=1
        spaces = row-x
        print(" "*spaces,"\033[0;32m*\033[00m "*x)
    print(" "*(row-3),"* "*3)
    print(" "*(row-3),"* "*3)