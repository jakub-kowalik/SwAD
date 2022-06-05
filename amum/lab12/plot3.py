# >> UZUPEŁNIJ <<
import matplotlib.animation
import matplotlib.pyplot as plt
import numpy as np

my_fig = np.array([[1, 0] ,[0, 1], [-1, 0], [0, -1]])
my_fig


# >> UZUPEŁNIJ <<

def rotate_by(angle):
    return np.array([[np.cos(np.deg2rad(angle)), -np.sin(np.deg2rad(angle))],
                     [np.sin(np.deg2rad(angle)), np.cos(np.deg2rad(angle))]])


def stretch_by(k, k2=None, axis='x'):
    if axis == 'x':
        return np.array([[k, 0], [0, 1]])
    elif axis == 'y':
        return np.array([[1, 0], [0, k]])
    elif axis == 'both':
        return np.array([[k, 0], [0, k2]])
    else:
        raise ValueError


def lean_by(k, axis='x'):
    if axis == 'x':
        return np.array([[1, k], [0, 1]])
    elif axis == 'y':
        return np.array([[1, 0], [k, 1]])
    else:
        raise ValueError


# rotated = my_fig @ lean_by(1, 'x')

fig, ax = plt.subplots(figsize=(10, 7))


def animate(i):
    lin = np.sin(np.deg2rad(i))
    ax.cla()
    ax.set_xlim((-2, 2))
    ax.set_ylim((-2, 2))
    rotated = my_fig @ lean_by(lin, 'y')
    ax.fill(rotated[:, 0], rotated[:, 1])
    plt.draw()


ani = matplotlib.animation.FuncAnimation(fig, animate, frames=360, interval=1, repeat=True)

plt.show()
