#e3.2DyaDayUp363.py
import math
dayup = math.pow((1.0+0.005),365)
daydown = math.pow((1.0-0.005),365)
print("UP:{:.2f},DOWN:{:.2f}".format(dayup,daydown))