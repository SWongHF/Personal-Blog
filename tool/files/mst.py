# Generate MST of selected points
# Using Delaunay triangulation and Kruskal
# Input: nx2 np.array of points
# Output: an adjacency list of MST

from scipy.spatial import Delaunay
import numpy as np
import math
import matplotlib.pyplot as plt


class MSTGenerator():
    def __init__(self, points: np.array):
        self.points = points
        self.triangles = Delaunay(self.points).simplices

    def __dist2(self, x: int, y: int):
        return math.sqrt((self.points[x, 0]-self.points[y, 0])**2 + (self.points[x, 1]-self.points[y, 1])**2)

    def show(self, show_tri=False):
        if show_tri:
            plt.subplot(1, 2, 1)
            plt.xlim(0, 500)
            plt.ylim(0, 500)
            ax = plt.gca()
            ax.set_aspect('equal', adjustable='box')
            self.__plotTriangles()
            plt.subplot(1, 2, 2)
        plt.xlim(0, 500)
        plt.ylim(0, 500)
        ax = plt.gca()
        ax.set_aspect('equal', adjustable='box')
        self.__plotMST()
        plt.show()

    def __plotTriangles(self):
        plt.triplot(self.points[:, 0], self.points[:, 1], self.triangles)

    def __plotMST(self):
        for u in range(len(self.g)):
            for v in self.g[u]:
                plt.plot((self.points[u, 0], self.points[v, 0]),
                         (self.points[u, 1], self.points[v, 1]))

    def generateMST(self) -> list:
        n = len(self.points)
        self.g = [[] for i in range(n)]
        edges = set()
        for tri in self.triangles:
            for i in range(3):
                u, v = tri[i-1], tri[i]
                edges |= {(u, v) if u < v else (v, u)}
        edges = list(edges)
        edges.sort(key=lambda e: self.__dist2(e[0], e[1]))
        fa = list(range(n))

        def find(x: int) -> int:
            if fa[x] == x:
                return x
            fa[x] = find(fa[x])
            return fa[x]

        def union(x: int, y: int):
            fa[find(x)] = find(y)

        for edge in edges:
            u, v = edge
            if find(u) == find(v):
                continue
            self.g[u].append(v)
            self.g[v].append(u)
            union(u, v)

        print("Done generating MST")
        return self.g
