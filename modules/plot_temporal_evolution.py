import numpy as np
import matplotlib.pyplot as plt

import os
#==============================================#
# PARAMETERS
#==============================================#
cmap = plt.get_cmap('tab20')

current_dir = os.getcwd()


#==============================================#
# FUNCTIONS
#==============================================#
def temporal_evolution(N, L_min=100, L_max=270, L_step=20, folder="N=1k, vel=0.1"):
	t_max = []
	i_max = []
	L_s = []
	for idx, L in enumerate(range(L_min, L_max, L_step)):
		try:
			data = np.loadtxt(f"../data/{folder}/epidemia_0.100000_{L}.txt")
		except Exception as e:
			print(e)
			data = np.loadtxt(f"../data/epidemia_0.100000_{L}.txt")
		t = data[:,3]
		healthy = data[:,0]
		infected = data[:,1]
		refractary = data[:,2]
		# Plot results
		#plt.plot(t, healthy)
		#plt.plot(t, refractary)
		#plt.semilogy()
		plt.scatter(t, infected / N, color=cmap(idx), label=round(N / L**2, 3))
		plt.show()
	return None

#==============================================#
# MAIN
#==============================================#
folder = "N=1k, v=0.1/batch 1"
folder = ""

temporal_evolution(N=1024, L_min=180, L_max=181, L_step=20,  folder=folder)






