import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def hexagonal_grid(N, M):
    grid_centers = []
    for i in range(N):
        for j in range(M):
            x = j * np.sqrt(3) - (i % 2) * (np.sqrt(3) / 2)
            y = i * 1.5
            grid_centers.append((x, y))
    return np.array(grid_centers)



def state_plot(hgrid, clist, model=None):
    if model is not None:
        #cnew = np.zeros(hgrid.shape[0])
        cnew = np.full(hgrid.shape[0], np.nan)
        ss = model.state_symbols()
        for s, c in zip(ss,clist):
            # s is the state to plot
            cnew[s] = c
        clist = cnew

    plt.scatter(hgrid[:,0],hgrid[:,1],s=150,c=clist)
    for i, coord in enumerate(hgrid):
        plt.annotate(str(i+1), coord, fontsize=6, ha="center", va="center")  



# Given a vector lst and a value v, returns the index to the element closest to v
def index_of_closest(lst, v):
    return np.argmin((lst-v)**2)


# Return list of states traversed, as a trajectory list suitable for pyemma etc.
def read_traj_list(fname="data/SOM.neuron.classification.dat.xz"):
    d=pd.read_table(fname)
    d["RFrame"]=d.groupby(['Replica']).cumcount()
    d["State"]=d["Neuron.classif"]-1

    # Fix: RFrame is the replica's frame
    #      State is the 0-based neuron assignment

    # Split by replica. Make each replica's state list a list element.
    # traj_list is therefore a list of numpy arrays holding 0-based states

    dg=d.groupby("Replica")
    traj_list=[dg.get_group(x).State.to_numpy() for x in dg.groups]

    return traj_list





if __name__=="__main__":
    N = 5  # Number of hexagons along the x-axis
    M = 4  # Number of hexagons along the y-axis

    grid_centers = hexagonal_grid(N, M)

    # Plot the hexagonal grid
    plt.scatter(grid_centers[:, 0], grid_centers[:, 1], marker='o', c='blue')
    for i in range(N*M):
       plt.annotate(i, (grid_centers[i,0], grid_centers[i,1]))

    plt.gca().set_aspect('equal', adjustable='box')
    plt.title(f"2D Hexagonal Grid of size {N} x {M}")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()
