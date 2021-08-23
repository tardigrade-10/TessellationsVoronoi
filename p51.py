# Voronoi Tessellations diagram animation
import numpy as np
import matplotlib.pyplot as plt

plt.setp(plt.gca(), autoscale_on=False)

X=np.array(plt.ginput(-1, timeout=-1))
Y=[i for i in range (len(X))]

Grid=np.zeros((100,100))-1
x_grid = np.linspace(0,1,100)
y_grid = np.linspace(0,1,100)

for r in range(0,int(100*(2)**0.5)):
    for i in range(len(Y)):
        for x in range(0,100):
            for y in range(0,100):
                if Grid[y][x]==-1:
                   if (x/100-X[i][0])**2+(y/100-X[i][1])**2<(r/100+0.01)**2 and (x/100-X[i][0])**2+(y/100-X[i][1])**2>(r/100-0.01)**2:
                       Grid[y][x]=Y[i]
    plt.title('Voronoi Tessellations Diagram r='+str(r/100))
    plt.pcolormesh(x_grid,y_grid,Grid, shading='auto')
    plt.scatter(X[:,0],X[:,1],color="red",marker ="x")
    plt.pause(0.005)
    if np.any(Grid==-1)!=True:
        break
    plt.cla()

print(X)
print(Y)
print(Grid)
    