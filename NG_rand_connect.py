# An example of I&F Neurongroups of Brian
# Spike count and Raster plot of of random connected neuron
# library can be downloaded from http://briansimulator.org/

from  brian import *

tau = 20 * msecond        # membrane time constant
Vt = -50 * mvolt          # spike threshold
Vr = -60 * mvolt          # reset value
El = -49 * mvolt          # resting potential (same as the reset)
psp = 0.5 * mvolt

G = NeuronGroup(N=40, model='dV/dt = -(V-El)/tau : volt', threshold=Vt, reset=Vr)

#Connect Neuron randomly with sparsness 0.1
C=Connection(G,G,sparseness=0.1, weight=psp)
              
M=SpikeMonitor(G)

G.V=Vr+rand(40)*(Vt-Vr)

run(1*second)

print M.nspikes

#rasterplotting
raster_plot()
show()