import csv
import array
import math
import time
import os
import numpy as np
#import matplotlib.pyplot as plt
from bubble_sort import read_file, bubble_sort, batch_sorting

list_length = [10, 50, 100, 500, 1000]#, 5000, 10000]
csv_directory = ['10integer.csv', '50integer.csv', '100integer.csv', '500integer.csv', '1000integer.csv']#, '5000integer.csv', '10000integer.csv']

def main():
	time_sort = []
	for csv_file in csv_directory:
		filename = '../datasets/' + csv_file
		list_unsorted = read_file(filename)
		list_to_sort = np.copy(list_unsorted)
		list_sorted, time = batch_sorting(list_to_sort)
		time_sort.append(time)
		print('Execution Time: %f' %time)
	#print('Commulative time: \n', time_sort)
	plot_graph(list_length, time_sort)

def plot_graph(list_length, time_sort):
	list_length_log = []
	time_sort_usec = []
	for length in list_length:
		log_length = math.log10(length)
		list_length_log.append(log_length)
	for time in time_sort:
		time_usec = time * 1000000
		time_sort_usec.append(time_usec)
	print('Length of element: \n', list_length_log)
	print('Execution time: \n', time_sort_usec)

	#plt.plot(list_length_log, time_sort_usec)
	#plt.ylabel('Number of Elements')
	#plt.ylabel('Execution Time')
	#plt.show()

if __name__ == "__main__":
	main()