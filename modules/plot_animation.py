#Animación de la epidemia a través de agentes. 

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches
#from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes, mark_inset
import os


colores = ['blue','red', 'green']
archivo = "data/animacion.txt"

# build_animation
def build_animation(np_steps, tpause=0.01):

	N = 1024
	L = 100

	fig, ax = plt.subplots()

	for i in range(0, np_steps, 2000):
		if(i % 100==0):
			print(i)

		x = np.loadtxt(archivo, usecols=0, skiprows=N * i, max_rows=N)
		y = np.loadtxt(archivo, usecols=1, skiprows=N * i, max_rows=N)

		estado = np.loadtxt(archivo, usecols=3, skiprows=N * i, max_rows=N, dtype=int)
				
		plt.cla()

		#plt.title("Agents system") 
		plt.xlabel("L") 
		plt.ylabel("L")

		plt.axis('square')
		#plt.grid()
		plt.xlim(-1, L + 1)
		plt.ylim(-1, L+1)


		for j in range(N):
			circ = patches.Circle((x[j],y[j]), 1, alpha=0.7, fc= colores[estado[j]])
			ax.add_patch(circ)
		
		#save figure
		plt.savefig("video/pic%.4i.png" %(i), dpi=300)
		#plt.pause(tpause)

build_animation(500000)




####################################################################
####################################################################

