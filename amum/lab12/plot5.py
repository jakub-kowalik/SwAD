# >> UZUPEŁNIJ <<
import matplotlib.animation
import matplotlib.pyplot as plt
import numpy as np

my3dfig = np.array([[0, 0, 0], [1, 0, 0], [1, 1, 1], [0, 1, 1],
                    [0, 0, 1], [0, 1, 0], [1, 1, 0],[0, 0, 0]
                    ]) * 2


def affine_transformation(kx, ky, theta):
    return np.array([[np.cos(np.deg2rad(theta)), -np.sin(np.deg2rad(theta)), kx],
                     [np.sin(np.deg2rad(theta)), np.cos(np.deg2rad(theta)), ky],
                     [0, 0, 1]])


fig = plt.figure()
ax = fig.add_subplot(projection='3d')

def animate(i):
    lin = np.sin(np.deg2rad(i))
    ax.cla()
    ax.set_xlim3d(-2, 2)
    ax.set_ylim3d(-2, 2)
    ax.set_zlim3d(-2, 2)
    points = my3dfig @ affine_transformation(0, 0, i * 3)
    ax.scatter(points[:, 0], points[:, 1], points[:, 2], c='r', marker='o')
    ax.plot(points[:, 0], points[:, 1], points[:, 2], c='r', linewidth=2)
    plt.draw()


ani = matplotlib.animation.FuncAnimation(fig, animate, frames=360, interval=1, repeat=True)

plt.show()
