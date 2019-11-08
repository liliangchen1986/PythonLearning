#ex3.4DayDayUp365.py
dayup,dayfactor =1.0, 0.01
for i in range(365):
    if i % 7 in range(5):
        dayup = dayup * (1 + dayfactor)
        print(dayup)
    else:
        dayup = dayup * (1 - dayfactor)
        print(dayup)
print("UP5DOWN2:{:.2F}".format(dayup))