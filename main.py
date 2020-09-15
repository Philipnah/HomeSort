# This file will be used to select which algorithm you want to run

defaultList = [1, 9, 3, 5, 2, 7, 6, 4, 8]
print("This will sort the default list.\nEdit the code to select another list.\n")

def start():

	Algo = Algorithms()

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
					Algo.BubbleSort(defaultList)
				elif n == 1:
					#Algo.Bucket(defaultList)
					break
				else:
					print("Error, could not find your function to run.")

			n += 1
	else:
		print("Your choice is not available.")

class Algorithms:

	def BubbleSort(self, inputList):
		n = 0
		while n < len(inputList) - 1:
			i = 0
			while i < len(inputList) - n - 1:
				j = i + 1

				a = inputList[i]
				b = inputList[j]

				if a > b:
					inputList[i] = b
					inputList[j] = a
					print("swapped " + str(i) + " & " + str(j))
				else:
					pass

				i += 1
			n += 1
		print(inputList)
		




	def Bucket(self, inputList):
		pass


start()
