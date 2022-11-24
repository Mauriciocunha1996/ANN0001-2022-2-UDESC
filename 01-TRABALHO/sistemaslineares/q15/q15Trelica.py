import math
import numpy as np


np.set_printoptions(precision=16)
A = np.array([[-math.cos(math.radians(48)),0,math.cos(math.radians(33)),0,0,0],
[-math.sin(math.radians(48)),0,-math.sin(math.radians(33)),0,0,0],
[math.cos(math.radians(48)),1,0,1,0,0],
[math.sin(math.radians(48)),0,0,0,1,0],
[0,-1,-math.cos(math.radians(33)),0,0,0],
[0,0,math.sin(math.radians(33)),0,0,1]])


B = np.array([0,1971,0,-1971,0,-1971])



x = np.linalg.solve(A,B)
print(x)