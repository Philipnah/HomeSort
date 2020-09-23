# This file will be used to select which algorithm you want to run
from random import randint
import time


randomList = []

i = 0
while i < 5000:
	randomList.append(randint(1, 5000))
	i += 1


preRandomList = [808, 406, 596, 725, 589, 115, 233, 797, 627, 982, 399, 729, 97, 677, 736, 338, 8, 53, 73, 278, 881, 573, 811, 996, 686, 48, 873, 190, 213, 971, 826, 46, 113, 861, 741, 593, 447, 268, 205, 908, 974, 392, 835, 447, 489, 277, 68, 19, 656, 293, 17, 319, 752, 298, 226, 284, 241, 444, 162, 350, 937, 478, 527, 5, 164, 25, 310, 818, 809, 944, 383, 81, 617, 914, 488, 848, 248, 857, 139, 703, 162, 797, 430, 389, 96, 60, 3, 443, 517, 693, 310, 884, 788, 487, 734, 621, 935, 639, 69, 499, 853, 6, 166, 570, 716, 351, 510, 721, 697, 
				513, 189, 279, 560, 734, 740, 811, 615, 978, 202, 280, 994, 401, 382, 879, 375, 494, 415, 42, 552, 257, 738, 758, 951, 735, 590, 898, 308, 808, 452, 793, 282, 658, 729, 516, 622, 732, 715, 437, 15, 935, 753, 387, 188, 364, 16, 871, 155, 933, 172, 469, 786, 624, 998, 315, 717, 789, 319, 792, 919, 227, 950, 960, 540, 985, 285, 225, 480, 880, 577, 794, 365, 632, 614, 90, 536, 773, 321, 488, 960, 266, 184, 255, 757, 473, 468, 181, 614, 486, 526, 857, 135, 977, 572, 764, 506, 438, 412, 735, 995, 705, 513, 703, 522, 900, 412, 433, 218, 177, 142, 154, 905, 114, 613, 3, 566, 402, 85, 929, 642, 428, 64, 131, 512, 750, 418, 420, 538, 494, 390, 395, 997, 626, 200, 158, 798, 125, 796, 387, 95, 759, 584, 899, 356, 246, 193, 464, 748, 363, 679, 766, 512, 770, 958, 687, 283, 451, 498, 547, 556, 889, 456, 327, 989, 195, 130, 507, 841, 46, 396, 559, 176, 704, 31, 772, 842, 857, 643, 679, 635, 705, 66, 162, 761, 276, 313, 640, 632, 465, 503, 177, 957, 353, 831, 887, 589, 253, 448, 503, 886, 889, 226, 160, 192, 163, 634, 607, 656, 24, 754, 967, 796, 788, 522, 804, 415, 213, 52, 605, 275, 663, 935, 685, 701, 942, 797, 969, 414, 144, 180, 318, 986, 204, 613, 344, 127, 83, 20, 406, 660, 676, 707, 662, 988, 283, 271, 834, 60, 842, 3, 488, 625, 543, 228, 42, 612, 548, 218, 251, 755, 896, 430, 9, 174, 20, 539, 829, 363, 662, 483, 203, 956, 800, 267, 848, 825, 11, 939, 729, 552, 562, 934, 883, 357, 862, 710, 652, 688, 600, 773, 251, 543, 671, 300, 375, 922, 889, 802, 85, 942, 476, 268, 112, 985, 771, 630, 447, 395, 575, 560, 5, 905, 436, 136, 99, 712, 518, 534, 264, 266, 797, 674, 779, 872, 369, 563, 878, 542, 822, 938, 379, 672, 626, 883, 385, 183, 108, 702, 731, 465, 619, 975, 496, 748, 411, 410, 181, 254, 983, 614, 355, 753, 908, 987, 715, 114, 59, 754, 421, 590, 112, 597, 275, 552, 800, 835, 762, 494, 472, 893, 759, 764, 800, 157, 314, 318, 829, 798, 317, 645, 463, 210, 487, 419, 803, 465, 647, 600, 446, 447, 63, 
				751, 244, 866, 743, 852, 700, 969, 75, 267, 738, 907, 48, 808, 787, 115, 721, 979, 495, 480, 35, 753, 344, 762, 343, 936, 271, 79, 679, 808, 874, 147, 751, 707, 253, 122, 648, 242, 470, 564, 6, 935, 321, 263, 959, 181, 992, 985, 981, 770, 591, 585, 986, 683, 885, 545, 137, 595, 34, 884, 975, 62, 593, 848, 255, 263, 608, 713, 201, 596, 522, 254, 138, 90, 945, 378, 768, 426, 528, 740, 382, 541, 19, 169, 154, 233, 384, 192, 464, 744, 424, 571, 649, 377, 744, 58, 787, 332, 21, 84, 718, 123, 493, 539, 35, 468, 217, 841, 197, 735, 5, 312, 328, 578, 825, 750, 224, 928, 592, 876, 333, 14, 25, 741, 822, 783, 919, 242, 515, 243, 465, 370, 975, 769, 370, 350, 498, 541, 61, 178, 882, 870, 945, 724, 336, 207, 366, 205, 398, 533, 467, 97, 711, 973, 964, 982, 926, 404, 336, 64, 371, 397, 409, 591, 932, 707, 444, 3, 518, 910, 764, 549, 652, 537, 337, 808, 609, 378, 648, 270, 413, 872, 183, 113, 130, 577, 719, 758, 802, 598, 120, 943, 853, 953, 471, 225, 252, 535, 335, 459, 199, 711, 374, 565, 323, 684, 167, 569, 203, 358, 560, 113, 436, 226, 16, 887, 140, 204, 823, 164, 60, 336, 862, 391, 71, 280, 309, 627, 313, 351, 315, 2, 888, 228, 581, 34, 797, 416, 547, 993, 133, 971, 160, 964, 239, 875, 643, 251, 635, 447, 860, 389, 779, 756, 716, 715, 252, 86, 942, 401, 288, 535, 739, 595, 897, 110, 605, 609, 392, 233, 201, 678, 591, 593, 946, 2, 326, 228, 664, 954, 512, 52, 756, 418, 31, 179, 656, 42, 
				54, 721, 245, 897, 593, 78, 842, 786, 150, 481, 934, 949, 596, 417, 43, 519, 644, 21, 468, 951, 440, 525, 717, 338, 79, 910, 648, 667, 593, 186, 101, 98, 818, 718, 868, 657, 930, 802, 141, 853, 20, 721, 504, 142, 456, 867, 580, 41, 866, 828, 47, 750, 262, 39, 87, 769, 92, 210, 906, 569, 703, 712, 237, 15, 103, 43, 48, 267, 857, 975, 971, 494, 818, 
				810, 133, 338, 734, 556, 630, 872, 139, 210, 968, 31, 939, 382, 319, 766, 18, 882, 414, 174, 131, 938, 357, 349, 597, 471, 382, 444, 449, 416, 955, 893, 584, 328, 478, 478, 340, 563, 736, 661, 223, 846, 251, 351, 998, 372, 753, 711, 117, 418, 199, 822, 204, 452, 441, 523, 978, 343, 879, 978, 854, 11, 352, 159, 928, 903, 317, 21, 958, 733, 436, 139, 584, 953, 629, 994, 389, 27, 173, 537, 982, 401, 432, 119, 329, 433, 90, 929, 33, 685, 847, 805, 805, 749, 7, 403, 133, 228, 203, 291, 978, 741, 730, 947, 8, 511, 28, 312, 617, 493, 478, 147, 113, 324, 15, 518, 819, 69, 364, 421, 568, 83, 655, 367, 440, 310, 224, 316, 279, 295, 61, 493, 856, 554, 125, 512, 873, 386, 779, 273, 628]

defaultList = [1, 9, 3, 5, 2, 7, 6, 4, 8]


whichList = int(input("What list do you want to use?\n1. Random list (5000)\n2. Predefined random list (1000)\n3. Default list (10)\n\n"))

if whichList == 1:
	usedList = randomList
elif whichList == 2:
	usedList = preRandomList
elif whichList == 3:
	usedList = defaultList
else:
	print("Your selection was not available.\n")


def start():

	Algo = Algorithms()

	algorithms = [
		"bubble",
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
					start_time = time.time()
					newList = Algo.Bubble(usedList)
					print(newList)
					print("--- %s seconds ---" % (time.time() - start_time))
				elif n == 1:
					start_time = time.time()
					Algo.Bucket(usedList)
					print("--- %s seconds ---" % (time.time() - start_time))
				else:
					print("Error, could not find your function to run.")

			n += 1
	else:
		print("Your choice is not available.")

class Algorithms:

	def Bubble(self, inputList):
		n = 0
		while n < len(inputList) - 1:
			print("Iteration " + str(n + 1))
			i = 0
			while i < len(inputList) - n - 1:
				j = i + 1

				a = inputList[i]
				b = inputList[j]

				if a > b:
					inputList[i] = b
					inputList[j] = a
				else:
					pass

				i += 1
			n += 1
		return inputList


	def Bucket(self, inputList):

		Algo = Algorithms()

		# can this be optimised?
		bucket1 = []
		bucket2 = []
		bucket3 = []
		bucket4 = []
		bucket5 = []
		bucket6 = []
		bucket7 = []
		bucket8 = []
		bucket9 = []
		bucket10 = []

		finalBucket = []

		interval = 100

		n = 0
		while n < len(inputList):

			# can this be optimised?
			if inputList[n] < interval and inputList[n] > interval - interval:
				bucket1.append(inputList[n])

			if inputList[n] < interval*2 and inputList[n] > interval*2 - interval:
				bucket2.append(inputList[n])

			if inputList[n] < interval*3 and inputList[n] > interval*3 - interval:
				bucket3.append(inputList[n])

			if inputList[n] < interval*4 and inputList[n] > interval*4 - interval:
				bucket4.append(inputList[n])

			if inputList[n] < interval*5 and inputList[n] > interval*5 - interval:
				bucket5.append(inputList[n])

			if inputList[n] < interval*6 and inputList[n] > interval*6 - interval:
				bucket6.append(inputList[n])
			
			if inputList[n] < interval*7 and inputList[n] > interval*7 - interval:
				bucket7.append(inputList[n])
			
			if inputList[n] < interval*8 and inputList[n] > interval*8 - interval:
				bucket8.append(inputList[n])
			
			if inputList[n] < interval*9 and inputList[n] > interval*9 - interval:
				bucket9.append(inputList[n])
			
			if inputList[n] < interval*10 and inputList[n] > interval*10 - interval:
				bucket10.append(inputList[n])
			
			n += 1

		finalBucket.append(Algo.Bubble(bucket1))
		finalBucket.append(Algo.Bubble(bucket2))
		finalBucket.append(Algo.Bubble(bucket3))
		finalBucket.append(Algo.Bubble(bucket4))
		finalBucket.append(Algo.Bubble(bucket5))
		finalBucket.append(Algo.Bubble(bucket6))
		finalBucket.append(Algo.Bubble(bucket7))
		finalBucket.append(Algo.Bubble(bucket8))
		finalBucket.append(Algo.Bubble(bucket9))
		finalBucket.append(Algo.Bubble(bucket10))

		print(finalBucket)
		


start()
