# 10, 100, 500, 1000, dan 10000

# membuat array integer dan kemudian diacak urutannya
# membutuhkan python 3
# 
# n adalah jumlah elemen dari array yang akan kita buat

import array as arr
import random
import csv

def main():
	n = 2
	filename = str(n) + 'integer.csv'
	# simpan di berkas
	for i in range(0, 10):
		#print(i)
		if (i == 0):
			baris = create_array(n)
			baris = shuffle_array(baris, n)
			f =open(filename, 'w', newline='')
		# 'a' is for append
		else:
			baris = create_array(n)
			baris = shuffle_array(baris, n)
			f =open(filename, 'a', newline='')
		with f:
			writer = csv.writer(f)
			writer.writerows([baris])

def create_array(n):
	# buat array-nya
	baris = arr.array('i',[])
	for i in range(n):
		baris.append(i)
	#print(baris)
	return (baris)

def shuffle_array(baris, n):
	# kocok array m kali supaya isi array ditukar
	m = n
	for i in range(m):
		x = random.randint(0,n-1)
		y = random.randint(0,n-1)
		# swap baris(x,y)
		xi = baris[x]
		yi = baris[y]
		baris[y] = xi
		baris[x] = yi
	#print(baris)
	return (baris)

if __name__ == "__main__":
	main()
		