import numpy as np
import os

#=========================================================================#
# FUNCTIONS
#=========================================================================#
def get_subdirectories(path: str) -> list[str]:
    subdirectories = []
    for entry in os.scandir(path):
        if entry.is_dir():
            subdirectories.append(entry.path)
            subdirectories.extend(get_subdirectories(entry.path))
    return subdirectories

def merge_data(path_first: str, path_second: str, merge_path: str)-> None:
	data_first = np.loadtxt(path_first, dtype=int)
	data_second = np.loadtxt(path_second, dtype=int)	
	appended_data = np.concatenate((data_first, data_second))
	np.savetxt(merge_path, appended_data, fmt='%d')


for L in [80, 100, 120, 140, 160, 180, 200, 220]:
	path_first = f"data/N=1k, v=0.1/batch 1/epidemia_0.100000_{L}.txt"
	path_second = f"data/N=1k, v=0.1/batch 2/epidemia_0.100000_{L}.txt"
	merge_path = f"data/N=1k, v=0.1/merge/epidemia_0.100000_{L}.txt"

	merge_data(path_first, path_second, merge_path)

current_directory = os.getcwd()

