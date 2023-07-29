# Plot graph by Fourier Transform interpolation
# Using matplotlib.animation
# Input: nx2 np.array of points and a list of traverse points
# Output: gif animation

import numpy as np
from scipy.fftpack import fft
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
from matplotlib.patches import Circle


class FourierTransPlot():
    def __init__(self, x: np.array):
        x_max, x_min = x.max(), x.min()
        x = (x - x_min) / (x_max - x_min)
        self.X = fft(x[:, 0] + x[:, 1] * 1j)
        # let frame_number = circle_number
        #   such that it passes one point each frame
        self.number = len(self.X)
        self.__generatePos()

    def __generatePos(self):
        # circle i at different frame t
        # X[i][t] = self.X[i] * exp(2*pi*1j*t*i/n) / n
        X = []
        for i in range(self.number):
            X.append(self.X[i] * np.exp(
                2 * np.pi * 1j * i * np.arange(self.number) / self.number) /
                self.number)
        # pos[i][t] is the position of circle i's center at t frame
        # pos[i][t] = pos[i-1][t] + X[i][t]
        # len(pos) = t+1
        self.pos = [[0 for i in range(self.number)]]
        for i in range(self.number):
            self.pos.append(self.pos[-1] + X[i])

    def plot(self, save_gif=False, filename="", speed=1.0):
        fig, ax = plt.subplots(dpi=300, facecolor='#000000')
        ax.set(xlim=[0, 1], ylim=[0, 1])
        ax.axis('off')
        colorarr = ["#ff595e", "#ffca3a", "#8ac926", "#1982c4", "#6a4c93"]
        # initialize lines
        lines = [
            ax.plot([], [], alpha=0.5, color=colorarr[i % 5])[0]
            for i in range(self.number)
        ]
        # initialize circles
        circles = []
        for i in range(self.number):
            radius = np.abs(self.X[i] / self.number)
            # temporary place
            circle = Circle((0, 0), radius, alpha=0.5,
                            color=colorarr[i % 5], fill=False)
            circles.append(circle)
            ax.add_artist(circle)

        path = ax.plot([], [], 'w')[0]

        path_x = []
        path_y = []

        def render_frame(k: int):
            # render lines between two circles
            for i in range(self.number):
                u, v = self.pos[i][k], self.pos[i + 1][k]
                lines[i].set_data([u.real, v.real], [u.imag, v.imag])
            # render circles with new center
            for i in range(self.number):
                u = self.pos[i][k]
                circles[i].center = (u.real, u.imag)
            # add new point
            u = self.pos[-1][k]
            path_x.append(u.real)
            path_y.append(u.imag)
            path.set_data(path_x, path_y)

        animation = FuncAnimation(fig,
                                  render_frame,
                                  frames=self.number,
                                  interval=10,
                                  repeat_delay=2000)
        if save_gif:
            animation.save(f'{filename}.gif',
                           writer="imagemagick", fps=int(50/speed))
            print("Done saving gif")
        else:
            plt.show()
