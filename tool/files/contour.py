# Utilize the data after collecting the svg points
# Input: txt_file Points.txt (file input)
# Output: nx2 np.array of points

import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


class ContourReader():
    def readFile(self):
        filename = "Points.txt"
        Points = []
        with open(filename, "r") as f:
            for line in f:
                Points.append([float(n) for n in line.strip().split(',')])
        f.close()
        print(len(Points))
        self.points = np.array(Points)

    def show(self):
        _, ax = plt.subplots()
        ax.scatter(self.points[0:1546, 0],
                   self.points[0:1546, 1], s=1, alpha=0.5)
        plt.xlim(0, 500)
        plt.ylim(0, 500)
        ax = plt.gca()
        ax.set_aspect('equal', adjustable='box')
        plt.draw()
        plt.show()
