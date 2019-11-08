#Exc3.4回文数判断.py
str = input("请输入您要进行判断的数字:")
p = 0
if len(str)%2 == 0:
    for i in range(int(len(str)/2)):
        if str[i] != str[-(i+1)]:
            p += 1
        else:
            p += 0
else:
    for i in range(int((len(str)+1)/2)):
        if str[i] != str[-(i+1)]:
            p +=1
        else:
            p += 0
if p == 0:
    print("您输入的数字是{},是回文数".format(str))
else:
    print("您输入的数字是{},不是回文数".format(str))
