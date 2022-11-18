import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from pklshop.rally import *


def animate(i):
    # erase previous plot
    ax.cla()

    plot_court()
    fig.set_facecolor("lightblue")

    # draw point's trajectory
    ax.plot(
        position[: i + 1, 0],
        position[: i + 1, 1],
        linestyle="-",
        color="black",
        alpha=0.2,
    )

    # draw point's current position
    ax.plot(
        position[i, 0],
        position[i, 1],
        marker="o",
        markerfacecolor="yellow",
        markeredgecolor="yellow",
    )

    # fix axes limits
    ax.set_xlim(-2.5, 22.5)
    ax.set_ylim(-25, 25)


if __name__ == "__main__":

    r = Rally("R1009")
    # position array generation
    N = 100
    speed_fac = 3

    xposinterp = np.array(
        [
            np.linspace(r.xcoords[i], r.xcoords[i + 1], int(N / speed_fac))
            for i in range(len(r.xcoords) - 1)
        ]
    ).flatten()
    yposinterp = np.array(
        [
            np.linspace(
                r.ycoords_flipped[i], r.ycoords_flipped[i + 1], int(N / speed_fac)
            )
            for i in range(len(r.ycoords_flipped) - 1)
        ]
    ).flatten()
    position = np.array([xposinterp, yposinterp]).T

    # generate figure and axis
    fig, ax = plt.subplots(figsize=(5, 5))

    n_frames = len(xposinterp)
    # define the animation
    ani = FuncAnimation(fig=fig, func=animate, interval=20, frames=n_frames)

    # show the animation
    # plt.show()
    ani.save("../figures/rally.gif", writer="pillow")
