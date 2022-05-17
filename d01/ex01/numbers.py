from asyncore import read


numbersFile = open("numbers.txt", "r")
numbersList = numbersFile.read().split(',')
for element in numbersList:
	print(element)