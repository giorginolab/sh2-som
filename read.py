import pandas as pd
import numpy as np

def read_traj_list(fname="SOM.neuron.classification.dat.xz"):
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


