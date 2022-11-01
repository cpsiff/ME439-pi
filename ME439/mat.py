import numpy as np

#q3, 4
mat = np.array([
    [np.cos(np.pi/4), -np.sin(np.pi/4)],
    [np.sin(np.pi/4), np.cos(np.pi/4)]
])
pt = mat @ np.array([2, 1]).T
print(pt)

#q5, 6
tf01 = np.array([
    [np.cos(np.radians(30)), -np.sin(np.radians(30)), 3],
    [np.sin(np.radians(30)), np.cos(np.radians(30)), 4],
    [0, 0, 1]
])
tf12 = np.array([
    [np.cos(np.radians(15)), -np.sin(np.radians(15)), 4],
    [np.sin(np.radians(15)), np.cos(np.radians(15)), 3],
    [0, 0, 1]
])
print(tf01 @ tf12 @ np.array([3, 2, 1]))

#q7, 8, 9
