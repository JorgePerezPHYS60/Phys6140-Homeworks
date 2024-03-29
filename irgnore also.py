# -*- coding: utf-8 -*-
"""PHYS 6040 HW_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19lYJH9OJazj1p-XM8OnR-OKPkjFzdpm5
"""

import math
import numpy as np
import random
from matplotlib import pyplot

reps=int(10e6) #repeat experiment reps times
tries=[] #number of tries to see all six outcomes

for num in range(reps):
  count=0 #counts number of dice rolled
  rolls=[1,2,3,4,5,6] #possible outcomes
  while not not rolls:
    roll=random.randint(1,6)
    if roll in rolls:
      rolls.remove(roll)
      count+=1
    else:
      count+=1
  tries.append(count)

mean=sum(tries)/len(tries)
print(mean)
