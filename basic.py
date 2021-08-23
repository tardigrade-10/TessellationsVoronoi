import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d

# plt.close('all')

x1 = 0
x2 = 1
y1 = 0
y2 = 1

xd = x2-x1
yd = y2-y1
area = xd * yd

lamb = 10

numbpoints = np.random.poisson(lamb * area)
x = xd * np.random.uniform(0,1, numbpoints) + x1
y = yd * np.random.uniform(0,1, numbpoints) + y1

xy = np.stack((x,y), axis = 1)
voronoi = Voronoi(xy)
vertex = voronoi.vertices
cell = voronoi.regions

voronoi_plot_2d(voronoi, show_points = False, show_vertices = False)

plt.scatter(x, y, edgecolor = 'b', facecolor='b')

for i in range(numbpoints):
    plt.text(x[i] + xd/50, y[i]+ yd/50, i)

plt.savefig('out.png')

# python basic.py
