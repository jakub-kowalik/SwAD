import matplotlib.image
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.offsetbox import AnnotationBbox, OffsetImage


def hover(event):
    if event.inaxes:
        # print(event.ind)
        print(event.xdata)
        # event.artist.set_visible(True)
        pass


def main():
    with open('animals.npz', 'rb') as f:
        animals = np.load(f)['animals']
    print(animals)

    fig, ax = plt.subplots()

    weight = []
    height = []
    samples = []

    for element in animals:
        weight.append(float(element[2]))
        height.append(int(element[3]))
        samples.append([float(element[2]), int(element[3])])

    sc = plt.scatter(weight, height)

    # for a in animals[:3]:
    #     imagebox = OffsetImage(matplotlib.image.imread(a[4]), zoom=0.2)
    #     imagebox.image.axes = ax
    #     annot = AnnotationBbox(imagebox, (float(a[2]), float(a[3])),
    #                            xybox=(120, -80),
    #                            xycoords='data',
    #                            boxcoords="offset points",
    #                            pad=0.5
    #                            )
    #     ax.add_artist(annot)
    #     annot.set_visible(False)

    imagebox = OffsetImage(matplotlib.image.imread(animals[0][4]), zoom=0.2)
    imagebox.image.axes = ax
    annot = AnnotationBbox(imagebox, (0, 0),
                           xybox=(120, -80),
                           xycoords='data',
                           boxcoords="offset points",
                           pad=0.5
                           )
    ax.add_artist(annot)
    annot.set_visible(False)


    def hover(event):
        if sc.contains(event)[0]:
            ind, = sc.contains(event)[1]["ind"]
            w, h = fig.get_size_inches() * fig.dpi
            ws = (event.x > w / 2.) * -1 + (event.x <= w / 2.)
            hs = (event.y > h / 2.) * -1 + (event.y <= h / 2.)
            annot.xybox = (ws, hs)
            annot.set_visible(True)
            annot.xy = (weight[ind], height[ind])
            imagebox.set_data(matplotlib.image.imread(animals[ind][4]))
        else:
            annot.set_visible(False)
        fig.canvas.draw_idle()

    fig.canvas.mpl_connect('motion_notify_event', hover)
    plt.show()


if __name__ == '__main__':
    main()

# ab =
#
# ax.add_artist(ab)
#
# # Fix the display limits to see everything
# ax.set_xlim(0, 1)
# ax.set_ylim(0, 1)
#
# plt.show()
