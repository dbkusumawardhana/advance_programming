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
		insertion_sorted = insertion_sort(batch_unsorted[i])
		batch_sorted.append(insertion_sorted)
	batch_sorted = np.array(batch_sorted)
	return(batch_sorted)

def insertion_sort(InputList):
	for i in range(1, len(InputList)):
		j = i-1
		nxt_element = InputList[i]
		while (InputList[j] > nxt_element) and (j >= 0):
			InputList[j+1] = InputList[j]
			j=j-1
		InputList[j+1] = nxt_element
	return (InputList)

if __name__ == "__main__":
	main()