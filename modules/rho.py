import numpy as np
from math import sqrt

# Old Densities
N=1024
L=60
L_list = [L + d for d in range(20, 200, 20)]
rho = [N / s**2 for s in L_list]

#New values
print()
N_new = 65536
N_new = 8182
L_new = [int(sqrt(N_new / densidad)) for densidad in rho]

print("L_new")
print(L_new)
rho_new = [N_new / s**2 for s in L_new]
print()
print(rho_new)
print()
print(np.diff(L_new	))

for l, l_old, d, d_old in zip(L_new, rho_new, L_list, rho):
	print(round(l, 1), round(d, 4), round(l_old, 1), round(d_old, 4))