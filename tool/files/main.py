import numpy as np

from contour import ContourReader
from mst import MSTGenerator
from ftplot import FourierTransPlot
from path import PathGenerator

ct = ContourReader()
ct.readFile()
# show contour
# ct.show()

mst = MSTGenerator(ct.points)
g = mst.generateMST()
# show triangles
# mst.show(show_tri=False)

vals = [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5,
        5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10]
for val in vals:
    path = PathGenerator(ct.points, g)
    path.epsilon = val
    x = path.generatePath()
    # path.show()
    plot = FourierTransPlot(x)
    # show or save gif
    plot.plot(save_gif=True, filename=f'fft{int(val*10)}slow', speed=0.5)
    plot.plot(save_gif=True, filename=f'fft{int(val*10)}medium', speed=1.0)
    plot.plot(save_gif=True, filename=f'fft{int(val*10)}fast', speed=2.0)
