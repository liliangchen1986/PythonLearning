#e4.3TextPrgressBar.py
import time
scale = 50
print("执行开始".center(scale//2,"-"))
t = time.clock()
for i in range(scale):
    a = '*' * i
    b = '.' * (scale - i)
    c = (i/scale) * 100
    t -= time.clock()
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,-t),end='')
    time.sleep(.05)
print("\n"+"执行结束".center(scale//2,'-'))