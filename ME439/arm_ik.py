import numpy as np
import matplotlib.pyplot as plt

def ik(l_1, l_2, l_3, x_0, y_0, z_0):
    delta_z = z_0 - l_1
    delta_R = np.linalg.norm(np.array([x_0, y_0]))

    alpha = np.arctan2(y_0, x_0)

    # delta is like the elbow angle on the inside
    # delta could give solutions - we probably want the elbow up option, where delta > 180 deg (?)
    delta = np.arccos((delta_z**2 + delta_R**2 - l_2**2 - l_3**2)/(-2*l_2*l_3))
    
    # solve for Beta_2 from delta
    Beta_2 = np.pi-delta

    # solve for angle Psi
    Psi = np.arctan2(delta_z, delta_R)

    # solve for angle Phi
    k_1 = l_2 + (l_3*np.cos(Beta_2))
    k_2 = l_3 * np.sin(Beta_2)
    Phi = np.arctan2(k_2, k_1)
    # Phi = np.degrees(np.arctan(k_2/k_1)) # alternative way to do it per notes

    # solve for Beta_1 from Psi and Phi
    Beta_1 = Psi - Phi # could be plus or minus, need to make sure signs make sense

    # find Beta_3 - link 4 needs to keep the pen vertical
    # b1 + b2 + b3 = 0
    # Beta_3 = -(Beta_1 + Beta_2)

    return (np.degrees(alpha), np.degrees(Beta_1), np.degrees(Beta_2))

# # our actual robot parameters
# l_1 = 0.1026
# l_2 = 0.1180
# l_3 = 0.1335
# l_4 = 0.0290

# x_0 = 0.17
# y_0 = 0.1
# z_0 = 0

# print(ik(l_1, l_2, l_3, l_4, x_0 -0.008, y_0 + 0.35, z_0))

# x_0 = 0.15
# y_0 = 0.08
# z_0 = 0
# print(ik(l_1, l_2, l_3, l_4, x_0 -0.008, y_0 + 0.35, z_0))


# x_0 = -0.2
# y_0 = 0.1
# z_0 = 0
# print(ik(l_1, l_2, l_3, l_4, x_0 -0.008, y_0 + 0.35, z_0))

# x_0 = 0.3
# y_0 = 0
# z_0 = 0
# print(ik(l_1, l_2, l_3, l_4, x_0 -0.008, y_0 + 0.35, z_0))

print(ik(0.5, 1.5, 0.8, 1.8719, 0.3301, 1.7378))

x = 0.16
y = 0.16
z = 0.0045
c = 0.015

xy_vec = np.array([x, y, 0])
xy_vec_u = xy_vec / np.linalg.norm(xy_vec)
change = xy_vec_u * -c
print(change)
print(ik(0.04, 0.118, 0.118, x + change[0], y + change[1], z + change[2]))