# This file will be used to select which algorithm you want to run

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
			print("You have selected " + algorithms[n])
		n += 1
else:
	print("Your choice is not available.")