import numpy as np
import matplotlib.pyplot as plt

def kinematics_p2(alpha, b1, b2, l1, l2, l3):
    """
    l2 is length of first arm segment, l3 is length of second
    b1 is angle of first link to base, b2 is second link to first link
    alpha is the 3D rotation, like overhead, the angle of the base

    b1 and b2 are along the y axis
    alpha is along the z axis

    returns a 3D homogenous transform that takes the coordinate system of the
    second arm to the system of the base
    """
    t01 = np.array([
        [np.cos(alpha), -np.sin(alpha), 0, 0],
        [np.sin(alpha), np.cos(alpha), 0, 0],
        [0, 0, 1, l1],
        [0, 0, 0, 1]
    ])
    t12 = np.array([
        [np.cos(b1), 0, -np.sin(b1), 0],
        [0, 1, 0, 0],
        [np.sin(b1), 0, np.cos(b1), 0],
        [0, 0, 0, 1]
    ])

    t02 = t01 @ t12

    t23 = np.array([
        [np.cos(b2), 0, -np.sin(b2), l2],
        [0, 1, 0, 0],
        [np.sin(b2), 0, np.cos(b2), 0],
        [0, 0, 0, 1]
    ])

    t03 = t02 @ t23

    return (t01, t12, t23)

def composite_tfs(transforms):
    res = np.identity(4)
    for tf in transforms:
        res = res @ tf
    return res

"""
Challenge part 1 testing
"""
# l1 = 0
# l2 = 1
# l3 = 1

# tfs = kinematics_p2(0, 0, 0, l1, l2, l3)
# for tf in tfs:
#     print(tf, "\n")

# t03 = composite_tfs(tfs)
# print(t03)
# print(t03 @ np.array([l3, 0, 0, 1]).T)

"""
Challenge part 2
"""
l1 = 2
l2 = 1
l3 = 1
alpha_range = np.linspace(-np.pi/2, np.pi/2, 32)
b1_range = np.linspace(0, np.pi/2, 32)
b2_range = np.linspace(-np.pi/2, np.pi/2, 32)

end_effector_points = []
for alpha in alpha_range:
    for b1 in b1_range:
        for b2 in b2_range:
            end_effector_points.append(
                (composite_tfs(kinematics_p2(alpha, b1, b2, l1, l2, l3)) @ (np.array([l3, 0, 0, 1]).T))[:3]
            )

end_effector_points = np.array(end_effector_points)
# print(end_effector_points)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(*end_effector_points.T)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
plt.tight_layout()
# plt.show()

"""
Example cases for discussion post
"""
print((composite_tfs(kinematics_p2(np.pi/2, 0, np.pi/2, l1, l2, l3)) @ (np.array([l3, 0, 0, 1]).T))[:3])
print((composite_tfs(kinematics_p2(0, np.pi/2, 0, l1, l2, l3)) @ (np.array([l3, 0, 0, 1]).T))[:3])

print((composite_tfs(kinematics_p2(-np.pi/4, np.radians(-10), np.radians(20), 0.5, 1.5, 0.8)) @ (np.array([0.8, 0, 0, 1]).T))[:3])
print((composite_tfs(kinematics_p2(np.radians(-30), np.radians(-30), np.radians(10), 0.5, 1.5, 0.8)) @ (np.array([0.8, 0, 0, 1]).T))[:3])
