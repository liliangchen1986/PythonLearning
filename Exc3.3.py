#Exc3.3.py
ability = 1
circle = eval(input("请输入周期数："))
for i in range(365):
    if i % circle in [0,1,2]:
        ability = ability
    else:
        ability = ability * 1.01
print("经过365天的努力，能力变为最初的{:^.3f}倍".format(ability))