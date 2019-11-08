#e3.3DayDayUp365.py
import math
dayfactor=0.01
dayup = math.pow((1.0+dayfactor),365)
daydown = math.pow((1.0-dayfactor),365)
print("UP:{:.2f},DOWN：{:.2f}".format(dayup,daydown))