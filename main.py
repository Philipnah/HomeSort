# This file will be used to select which algorithm you want to run


def start():
	algorithms = [
		"bubble sort",
		"bucket"
	]

	i = 1
	for items in algorithms:
		print(str(i) + ". " + items)
		i += 1


	choice = input("\nSelect which algorithm you want to run: ")

	if choice in algorithms:
		n = 0
		while(n <= len(algorithms) - 1):
			if choice == algorithms[n]:
				print("You have selected " + algorithms[n] + "\n")
				
				# Try to make these following if-statements shorter, perhaps by using another method.
				if n == 0:
					print("0")
					Algorithms.BubbleSort(SortThis)
				elif n == 1:
					Algorithms.Bucket(SortThis)
				else:
					print("Error, could not find your function to run.")

			n += 1
	else:
		print("Your choice is not available.")

class Algorithms:
	#def swap(self, a, b):
	#	c = a


	def BubbleSort(self):
		i = 0
		j = i + 1
		
		n = 0
		while n < len(SortThis):
			while i < len(SortThis) - n:

				a = SortThis[i]
				b = SortThis[j]

				if a > b:
					c = a
					a = b
					b = c
					print(SortThis)

					#swap(a, b)
				else:
					pass

				i += 1
			n += 1



	def Bucket(self):
		pass

SortThis = [1, 9, 3, 5, 2, 7, 6, 4, 8]
print("This will sort the default list.\nEdit the code to select another list.\n")

start()
