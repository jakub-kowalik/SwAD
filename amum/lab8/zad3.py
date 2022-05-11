import matplotlib.pyplot as plt
import numpy as np
import mpl_toolkits.mplot3d.axes3d as p3


def f(x, y):
    return 0.5 * np.sin(x ** 3) + 0.25 * np.sin((y + np.pi) ** 2)


def main():
    n = 100
    x = np.linspace(-np.pi / 2, np.pi / 2, n)
    y = np.linspace(-np.pi, np.pi / 2, n)

    res = np.array([[f(xx, yy) for xx in x] for yy in y])

    X, Y = np.meshgrid(x, y)

    fig, ax = plt.subplots(figsize=(10, 7))

    ax = p3.Axes3D(fig)
    # ax.set_xlim3d([-np.pi / 2, np.pi / 2])
    # ax.set_ylim3d([0, np.pi * 1.5])
    # ax.contourf(X, Y, res, cmap='jet')
    ax.plot_surface(X, Y, res, cmap='gist_ncar')
    # ax.contour(X, Y, res, linestyle='auto')

    plt.show()
    pass


if __name__ == "__main__":
    main()
