import matplotlib.pyplot as plt
import matplotlib.animation
import numpy as np


def f(x, y, t):
    return 0.5*np.sin(x**3) + 0.25*np.sin((y - t * 0.1)**2)


def main():
    n = 100
    x = np.linspace(-np.pi / 2, np.pi / 2, n)
    y = np.linspace(0, np.pi * 1.5, n)

    res = [[f(xx, yy, 0) for xx in x] for yy in y]

    X, Y = np.meshgrid(x, y)

    fig, ax = plt.subplots(figsize=(10, 7))

    ax.set_xlim(-np.pi / 2, np.pi / 2)
    ax.set_ylim(0, np.pi * 1.5)

    # uzupełnij (wyświetl obraz za pomocą `contourf` i `contour`).

    def animate(i):
        ax.clear()
        res = [[f(xx, yy, i) for xx in x] for yy in y]
        ax.contourf(X, Y, res, cmap='jet')
        ax.contour(X, Y, res)
        plt.draw()

    # uzupełnij

    ani = matplotlib.animation.FuncAnimation(fig, animate, frames=80, interval=100, repeat=False)
    ani.repeat = True
    plt.show()


if __name__ == '__main__':
    main()
