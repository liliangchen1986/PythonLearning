#Exc3.2DayDayUP.py\
ability = 1
for i in range(365):
    if i%7 in [0,1,2]:
        ability = ability
    else:
        ability = ability * 1.01
print("经过365天的努力，能力变为最初的{:^.3f}倍".format(ability))
