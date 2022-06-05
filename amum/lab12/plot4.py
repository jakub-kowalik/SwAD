# >> UZUPEŁNIJ <<
import matplotlib.animation
import matplotlib.pyplot as plt
import numpy as np

my_fig = np.array([[1, 0] ,[0, 1], [-1, 0]])
my_fig = np.c_[my_fig, np.ones(my_fig.shape[0])]


# >> UZUPEŁNIJ <<

def affine_transformation(kx, ky, theta):
    return np.array([[np.cos(np.deg2rad(theta)), -np.sin(np.deg2rad(theta)), kx],
                     [np.sin(np.deg2rad(theta)), np.cos(np.deg2rad(theta)), ky],
                     [0, 0, 1]])


# rotated = my_fig @ lean_by(1, 'x')

fig, ax = plt.subplots(figsize=(10, 7))


def animate(i):
    syn = np.sin(np.deg2rad(i))
    cosyn = np.cos(np.deg2rad(i))
    ax.cla()
    ax.set_xlim((-5, 5))
    ax.set_ylim((-5, 5))
    rotated = my_fig @ affine_transformation(syn * 2, cosyn * 2, -i * (1/2)).T
    ax.fill(rotated[:, 0], rotated[:, 1])
    plt.draw()


ani = matplotlib.animation.FuncAnimation(fig, animate, frames=720, interval=0.001, repeat=True)

plt.show()
