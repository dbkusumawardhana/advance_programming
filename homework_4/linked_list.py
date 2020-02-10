'''
Objective:
	importing data from csv, 
	formatting imported data,
	create linked list without sorting,
	create linked list with sorting
'''

import csv
import array
import time
import os
import numpy as np

class SLinkedList:
	def __init__(self):
		self.headval = None

	# Function to add new node
	def AtEnd(self, nis, name):
		NewNode = Node(nis, name)
		if self.headval is None:
			self.headval = NewNode
			return
		laste = self.headval
		while(laste.nextval):
			laste = laste.nextval
		laste.nextval = NewNode

	# Print the linked list
	def listprint(self):
		printval = self.headval
		while printval is not None:
			print(printval.nis, printval.name)
			printval = printval.nextval
		print("\n")

	# Function to add new sorted node
	def appendSorted(self, nis, name):
		node = Node(nis, name)
		curr = self.headval
		prev = None

		while curr is not None and curr.nis < nis:
			prev = curr
			curr = curr.next
		if prev == None:
			self.headval = node
		else:
			prev.next = node
		node.next = curr

	#print the list sorted
	def printList(self):
		curr = self.headval
		while curr != None:
			print(curr.nis, curr.name)
			curr = curr.next
		print("\n")

class Node:
	def __init__(self, nis=None, name=None):
		self.nis = nis
		self.name = name
		self.nextval = None

def main():
	filename = 'sepakbola-exported.csv'	
	list_of_players = read_file(filename)

	# Create linked list with unsorted condition
	list1 = SLinkedList()
	for player in list_of_players:
		list1.AtEnd(int(player[0]), str(player[1]))
	print("Unsorted linked list:")
	list1.listprint()

	# Create linked list with sorted condition
	list2 = SLinkedList()
	for player in list_of_players:
		list2.appendSorted(int(player[0]), str(player[1]))
	print("Sorted linked list:")
	list2.printList()

def read_file(filename):

	# Import data from csv
	parent_dir = os.getcwd()
	path = os.path.join(parent_dir, filename)
	with open(path, mode='r', encoding='utf-8-sig') as csvfile:
		list_unseparated = list(csv.reader(csvfile))

	# Format the data
	list_separated = []
	for element in list_unseparated:
		player = element[0].split(';')
		player[0] = int(player[0])
		list_separated.append(player)

	return(list_separated)

if __name__ == "__main__":
	main()

























