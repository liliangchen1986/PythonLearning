#P94Exc3.5.py
for i in range(11):
    if i % 5 == 0:
        for j in range(11):
            if j % 5 == 0:
                print("+ ",end="")
            else:
                print("- ",end="")
        print("\n")
    else:
        for j in range(11):
            if j % 5 == 0:
                print("| ",end="")
            else:
                print("  ",end="")
        print("\n")