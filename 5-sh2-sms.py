# %% 

from htmd.ui import *
import numpy as np
from sklearn.cluster import * 
from glob import *
import matplotlib.pyplot as plt


# See 1-precompute-Metrics where it is done

contacts = MetricData(file="metrics/contacts.htmd")


for t in contacts.trajectories:
    p=t._projection
    p[p>12]=12


# %% 

ticaproj = TICA(data = contacts, lag = 50)
ticacontacts2 = ticaproj.project(ndim = 2)   # ndim = the number of TICA dimensions we want to project the data on

for i,d in enumerate(ticacontacts2.dat):
    plt.scatter(d[:,0], d[:,1], s=1, alpha=.1)
plt.show()

# %% 

ticaproj = TICA(data = contacts, lag = 50)
ticacontacts3 = ticaproj.project(ndim = 3)   # ndim = the number of TICA dimensions we want to project the data on

if False:
    fig = plt.figure(figsize = (10, 10))
    ax = plt.axes(projection ="3d")
    for i,d in enumerate(ticacontacts3.dat):
        ax.scatter3D(d[:,0], d[:,1], d[:,2], s=1, alpha=.1)
    plt.show()


# %% 

# https://stackoverflow.com/questions/43187484/matplotlib-slow-3d-scatter-rotation

import plotly.graph_objects as go

ff=go.Figure()
for i,d in enumerate(ticacontacts3.dat):
    s3 = go.Scatter3d(
        x=d[::10,0],
        y=d[::10,1], 
        z=d[::10,2],
        marker=go.scatter3d.Marker(size=2), 
         # opacity=0.5, 
        mode='markers'
    )
    ff.add_trace(s3)
ff.show("browser")


# %%

ticacontacts3.cluster(MiniBatchKMeans(n_clusters = 200), mergesmall = 5)

modello = Model(ticacontacts3)

# %%
modello.plotTimescales(lags = list(range(1, 800, 10)))

# %%

modello.markovModel(lag = 250, macronum = 6)
eqDist = modello.eqDistribution(plot = True)
print(eqDist)


# %%

modello.viewStates(protein = True)


# %%
