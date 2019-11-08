#Exc3.1TheCalucateOfWeight.py
import time
year = 2019
EarthWeight = 100
MoonWeight = 0
for i in range(11):
    year += 1
    EarthWeight += 0.5
    MoonWeight = EarthWeight * 0.165
    print("{:4d}年，您的体重是{:3.1f}kg，月球上折合的体重是{:^3.2f}kg".format(year,EarthWeight, MoonWeight))