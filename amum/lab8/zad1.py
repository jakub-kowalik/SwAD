import matplotlib.pyplot as plt
import numpy as np


def f(x, y):
    return 0.5 * np.sin(x ** 3) + 0.25 * np.sin((y + np.pi) ** 2)


def main():
    n = 100
    x = np.linspace(-np.pi / 2, np.pi / 2, n)
    y = np.linspace(-np.pi, np.pi / 2, n)

    res = [[f(xx, yy) for xx in x] for yy in y]

    X, Y = np.meshgrid(x, y)

    plt.contourf(X, Y, res, cmap='jet')
    plt.contour(X, Y, res, linestyle='auto')
    plt.show()
    pass


if __name__ == "__main__":
    main()
