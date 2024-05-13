import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# =====================================#
# PARAMETERS
# =====================================#
# time_step = 1250
# time_step = 30 * 1250
x_grid_size = 20
y_grid_size = 20

# =====================================#
# FUNCTION
# =====================================#
def save_grid(L: int) -> np.array:
	try:
		1/0
		data = np.load(f"data/N=1k, v=0.1/merge/epidemia_0.100000_{L}.npy")
	except Exception as e:
		print("Saving Exception", e)
		data = np.loadtxt(f"data/N=1k, v=0.1/merge/epidemia_0.100000_{L}.txt")
		np.save(f"data/N=1k, v=0.1/merge/epidemia_0.100000_{L}.npy", data)

	time = data[:, 3]
	infected = data[:, 1]

	x_grids = int((time.max())) // x_grid_size + 1
	y_grids = int((infected.max())) // y_grid_size + 5

	print("x_grids: ", x_grids)
	print("y_grids: ", y_grids)

	heat_grid = np.zeros(shape=(x_grids, y_grids))
	for i in range(0, time.size):
		x_id = int(time[i]) // x_grid_size
		y_id = int(infected[i]) // y_grid_size
		heat_grid[x_id, y_id] += 1

	np.save(f"grid_data/heat_grid_{L}", heat_grid)
	np.savetxt(f"grid_data/heat_grid_{L}.txt", heat_grid, fmt="%i")
	return heat_grid

def load_grid(L: int):
	return np.load(f"grid_data/heat_grid_{L}.npy")


def build_heatmap(L: int):
	print(f"\n L={L}.")
	try:
		1/0
		print("\t Loading grid.")
		heatmap = load_grid(L)
	except Exception as e:
		print("\t Saving grid:", e)
		heatmap = save_grid(L)

	mask = np.array(heatmap, dtype=bool)
	mask = np.logical_not(mask)
	ax = sns.heatmap(
		heatmap.T,
		mask=mask.T,
		linewidths=0.002,
		annot=False,
		square=False,
		cmap="rocket_r",
		vmin=0,
	)
	ax.invert_yaxis()

	# Calculate the y-axis tick positions and labels
	print(heatmap.shape)
	y_tick_positions = np.linspace(0, heatmap.shape[1], 5) 
	y_tick_labels = y_tick_positions * y_grid_size 
	y_tick_labels_formated = ["{:d}".format(int(y)) for y in y_tick_labels]
	plt.yticks(y_tick_positions, y_tick_labels_formated, fontsize=15)

	# Calculate the y-axis tick positions and labels
	x_tick_positions = np.linspace(0, heatmap.shape[0], 5)
	x_tick_labels = x_tick_positions * x_grid_size
	x_tick_labels_formated = [f"{int(x): d}" for x in x_tick_labels]
	plt.xticks(x_tick_positions, x_tick_labels_formated, fontsize=15)

	# plt.show()

	# Rungekutta
	solution = np.load(f"ballistic, v=0.1/rk4_ballistic_0.1_{L}.npy")
	time = np.load("ballistic, v=0.1/time.npy")
	infected = solution[:, 1] * 1024
	plt.plot(
		time[0:25000] / x_grid_size,
		infected[0:25000] / y_grid_size,
		color="black",
		linewidth=3,
		label=f"meanfield ballistic-{L}",
	)
	plt.legend()
	plt.tight_layout()
	#plt.axis("square")

L_list = [100, 120, 140, 160, 180, 200]
for L in L_list:
	build_heatmap(L)
	#plt.savefig("figures/heatmap_L.eps")
	plt.savefig(f"figures/heatmap_{L}.pdf")
	plt.savefig(f"figures/heatmap_{L}.png")
	plt.show()
