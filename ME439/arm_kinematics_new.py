import numpy as np
import matplotlib.pyplot as plt

def set_axes_equal(ax):
    '''Make axes of 3D plot have equal scale so that spheres appear as spheres,
    cubes as cubes, etc..  This is one possible solution to Matplotlib's
    ax.set_aspect('equal') and ax.axis('equal') not working for 3D.

    Input
      ax: a matplotlib axis, e.g., as output from plt.gca().
      https://stackoverflow.com/questions/13685386/matplotlib-equal-unit-length-with-equal-aspect-ratio-z-axis-is-not-equal-to
    '''

    x_limits = ax.get_xlim3d()
    y_limits = ax.get_ylim3d()
    z_limits = ax.get_zlim3d()

    x_range = abs(x_limits[1] - x_limits[0])
    x_middle = np.mean(x_limits)
    y_range = abs(y_limits[1] - y_limits[0])
    y_middle = np.mean(y_limits)
    z_range = abs(z_limits[1] - z_limits[0])
    z_middle = np.mean(z_limits)

    # The plot bounding box is a sphere in the sense of the infinity
    # norm, hence I call half the max range the plot radius.
    plot_radius = 0.5*max([x_range, y_range, z_range])

    ax.set_xlim3d([x_middle - plot_radius, x_middle + plot_radius])
    ax.set_ylim3d([y_middle - plot_radius, y_middle + plot_radius])
    ax.set_zlim3d([z_middle - plot_radius, z_middle + plot_radius])

def kinematics_p2(alpha, b1, b2, b3, l1, l2, l3):
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

    t34 = np.array([
        [np.cos(b2), 0, -np.sin(b2), l3],
        [0, 1, 0, 0],
        [np.sin(b2), 0, np.cos(b2), 0],
        [0, 0, 0, 1]        
    ])

    return (t01, t12, t23, t34)

def composite_tfs(transforms):
    res = np.identity(4)
    for tf in transforms:
        res = res @ tf
    return res

l1 = 0.1026
l2 = 0.1180
l3 = 0.1335
l4 = 0.0290

pen_x = 0.008
pen_y = -0.035

print(
    (composite_tfs(kinematics_p2(np.pi/2, 0, np.pi/2, np.pi/4, l1, l2, l3)) @ (np.array([l4 + pen_x, pen_y, 0, 1]).T))[:3]
)

print(
    (composite_tfs(kinematics_p2(70.20112364547508, -72.88326197340162, 89.90634617915083, -17.023084205749214, l1, l2, l3)) @ (np.array([0, 0, 0, 1]).T))[:3]
)



# plot the pen's reachable workspace on the ground
# alpha_range = np.linspace(-np.pi, np.pi, 64)
# b1_range = np.linspace(-np.pi, np.pi, 64)
# b2_range = np.linspace(-np.pi, np.pi, 32)
# b3_range = np.linspace(-np.pi, np.pi, 32)

# alpha_range = np.linspace(np.radians(-88), np.radians(100), 32)
# b1_range = np.linspace(np.radians(-134), np.radians(-19), 32)
# b2_range = np.linspace(np.radians(61), np.radians(151), 32)
# b3_range = np.linspace(-np.radians(-81), np.radians(84), 32)

# end_effector_points = []
# for alpha in alpha_range:
#     for b1 in b1_range:
#         for b2 in b2_range:
#             pt = (composite_tfs(kinematics_p2(alpha, b1, b2, -(b2+b1), l1, l2, l3)) @ (np.array([l3, 0, 0, 1]).T))[:3]
#             if(pt[2] > -0.01 and pt[2] < 0.01):
#                 end_effector_points.append(pt)
#     print(alpha)

# end_effector_points = np.array(end_effector_points)
# # print(end_effector_points)

# fig = plt.figure()
# ax = fig.add_subplot(projection='3d')
# ax.scatter(*end_effector_points.T)
# ax.set_xlabel("x")
# ax.set_ylabel("y")
# ax.set_zlabel("z")
# set_axes_equal(ax)
# plt.tight_layout()
# plt.show()