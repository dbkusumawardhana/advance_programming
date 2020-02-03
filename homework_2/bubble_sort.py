# source of bubble sort and insertion sort algorithm
# https://www.tutorialspoint.com/python_data_structure/python_sorting_algorithms.htm

import csv
import array
import time
import os
import numpy as np

def main():
	filename = '../datasets/10integer.csv'
	list_unsorted = read_file(filename)
	list_to_sort = np.copy(list_unsorted)
	list_sorted = batch_sorting(list_to_sort)
	print('Unsorted List:\n', list_unsorted)
	print('Sorted List:\n', list_sorted)

def read_file(filename):
	parent_dir = os.getcwd()
	path = os.path.join(parent_dir, filename)
	with open(path) as csvfile:
		list_to_sort = list(csv.reader(csvfile))
	list_to_sort = np.array(list_to_sort)
	return (list_to_sort)

def batch_sorting(batch_unsorted):
	batch_sorted = []
	for i in range(0, 10):
		bubble_sorted = bubble_sort(batch_unsorted[i])
		batch_sorted.append(bubble_sorted)
	batch_sorted = np.array(batch_sorted)
	return(batch_sorted)

def bubble_sort(list):
	for iter_num in range(len(list)-1,0,-1):
		for idx in range(iter_num):
			if list[idx]>list[idx+1]:
				temp = list[idx]
				list[idx] = list[idx+1]
				list[idx+1] = temp
	return (list)

if __name__ == "__main__":
	main()