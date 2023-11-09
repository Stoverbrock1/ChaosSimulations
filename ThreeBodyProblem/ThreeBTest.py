import numpy as np
import matplotlib.pyplot as plt
from ThreeBody import *

coord0 = [5, 0]
coord1 = [-5, 0]
m1 = 10
m2 = 10

realF = m1*m2/(100)

realD = 10

print("Real Distance: ", realD)
print("Calculated Distance: ", distEq(coord0, coord1))
print("Real Force: ", realF)
print("Calculated Force: ", forceEq(m1, m2, coord0, coord1))
