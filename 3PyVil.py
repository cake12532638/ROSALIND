#! /usr/bin/env python
# 60 69 115 123
sli = "36 46 53 60"
inStr = "5et7b4flyN8VOCIsfHYsakADy51CwmaSzNw6Gongylophisq3yxIaobsoletagF2P8IgmGJ0mMi6D6a5RjURe8VXopnnI3RmMBbfYeYnBiK0cM4RrvApBsXtnMLuPorW9nBKHcBdprASqcligtNwjXxjPW6LhG4iCu017vHwtUP2LB7pgIntpqzeEMyuyLuRGPsF4y."
a, b, c, d = sli.split()
hum = inStr[int(a) : int(b) + 1]

dum = inStr[int(c) : int(d) + 1]

print(hum, dum)
