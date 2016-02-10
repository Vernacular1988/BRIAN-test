# An example of I&F Neurongroups of Brian
# Illustrate membrane potential of random connected neuron
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
              
M=StateMonitor(G,'V', record = 0)

G.V=Vr+rand(40)*(Vt-Vr)

run(0.5*second)




#voltageplotting
plot(M.times / ms, M[0] / mV)
xlabel('Time (in ms)')
ylabel('Membrane potential (in mV)')
title('Membrane potential for neuron 0')
show()