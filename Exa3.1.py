#e3.1DayDayUp365.py
import math
dayup = math.pow((1.0+0.001),365) #提高0.001
daydown = math.pow((1.0-0.001),365) #降低0.001
print("UP:{:.2f},DOWN:{:.2f}".format(dayup,daydown))
