# source of bubble sort and insertion sort algorithm
# https://www.tutorialspoint.com/python_data_structure/python_sorting_algorithms.htm

import csv
import array
import time
import os
import numpy as np

def main():
	filename = '10integer.csv'
	list_to_sort = read_file(filename)
	print('list length = %d' %len(list_to_sort))
	#print(list_to_sort)
	
	list_to_bubble = np.copy(list_to_sort)
	bubble_start = time.time()
	bubble_sorted = bubblesort(list_to_bubble)
	bubble_end = time.time()
	print('bubble elapsed: %f' %(bubble_end - bubble_start))
	#print(bubble_sorted)
	
	list_to_insertion = np.copy(list_to_sort)
	insertion_start = time.time()
	insertion_sorted = bubblesort(list_to_insertion)
	insertion_end = time.time()
	print('insertion elapsed: %f' %(insertion_end - insertion_start))
	#print(insertion_sorted)

def read_file(filename):
	parent_dir = os.getcwd()
	path = os.path.join(parent_dir, filename)
	with open(path) as csvfile:
		list_to_sort = list(csv.reader(csvfile))
	list_to_sort = np.hstack(list_to_sort)
	return (list_to_sort)

def bubblesort(list):
# Swap the elements to arrange in order
	for iter_num in range(len(list)-1,0,-1):
		for idx in range(iter_num):
			if list[idx]>list[idx+1]:
				temp = list[idx]
				list[idx] = list[idx+1]
				list[idx+1] = temp
	return (list)

def insertion_sort(InputList):
	for i in range(1, len(InputList)):
		j = i-1
		nxt_element = InputList[i]
		# Compare the current element with next one
		
		while (InputList[j] > nxt_element) and (j >= 0):
			InputList[j+1] = InputList[j]
			j=j-1
		InputList[j+1] = nxt_element
	return (InputList)

if __name__ == "__main__":
	main()