#Exc3.13
dayup = 1.0
for j in range (11):
    for i in range (365):
        if i % 7 in [6,0]:
            dayup = dayup
        else:
            dayup = dayup * (1+0.001*j)
    print("The impovement factor of the project is {:.3f}".format(0.001*j))
    print("The improve of the project is {:.3f}".format(dayup))
    print("\n")