from random import randint

list1 = []

i = 0

while i < 1000:
	list1.append(randint(1, 1000))
	i += 1

print(list1)