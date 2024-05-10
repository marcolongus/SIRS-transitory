import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

y_grid_size = 1

data = np.load('heat_grid.npy')

time_step = 1
data_new = data[:4200:time_step].astype(int).T

mask = np.array(data_new, dtype=bool)
mask = np.logical_not(mask)
print(mask)

#ax = sns.heatmap(data_new, mask=mask, linewidths=0.002, annot=False, fmt="d", square=False)
ax = sns.heatmap(data_new, mask=mask, 
	linewidths=0.002, annot=False, 
	fmt="d", square=False, 
	cmap="rocket_r", vmin=0)
ax.invert_yaxis()

# Calculate the number of time steps and set the x-tick positions and labels
num_time_steps = data_new.shape[1]
x_tick_positions = np.arange(0, num_time_steps, 500)
x_tick_labels = x_tick_positions * time_step

# Set the x-ticks on the heatmap
plt.xticks(x_tick_positions, x_tick_labels)

# Set the x-ticks on the heatmap
plt.xticks(x_tick_positions, x_tick_labels)

# Calculate the y-axis tick positions and labels
y_tick_positions = np.arange(0, data_new.shape[0], 20)
y_tick_labels = y_tick_positions * y_grid_size / 1000

# Set the y-ticks on the heatmap
plt.yticks(y_tick_positions, y_tick_labels)

solution = np.load('rk4_ball_0.05.npy')
infected = solution[::time_step * 20, 1] * 1000
plt.plot(infected, 
	color='black', 
	linewidth=2.5, 
	label='meanfield ballistic')

solution = np.load('rk4_diff_0.05.npy')
infected = solution[::time_step*20, 1] * 1000
plt.plot(infected, 
	color='black',
	linestyle='dotted',
	linewidth=2.5,
	label='meanfield diffusive')

solution = np.load('rk4_beta_0.0054.npy')
infected = solution[::time_step*20, 1] * 1000
plt.plot(infected,
 	color='black',
	linestyle='dashed',
	linewidth=2.5,
	label='meanfield best-fit')

plt.xlabel("TIME", fontsize=15)
plt.ylabel(r'$\rho_i$', fontsize=20)

plt.tight_layout()
plt.legend(fontsize=14)

plt.savefig("heatmap.png")
plt.show()


#x_ticks = [time_step*i for i in range(1000) if time_step*i<6800]
#y_ticks = [i*y_grid_size for i in range(100) if i*y_grid_size < 120]

# #ax = sns.heatmap(data_new, linewidths=0.002, annot=False, fmt="d", square=False, xticklabels=x_ticks, yticklabels=y_ticks)
# solution = np.load('rk4_diff_0.05.npy')
# infected = solution[::time_step*20, 1]*1000
# plt.plot(infected, color='orange', linestyle='dashed', label='meanfield-diffusive')


