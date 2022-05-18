from asyncore import read

def printFile(): 
	numbersFile = open("numbers.txt", "r")
	numbersList = numbersFile.read().split(',')
	for element in numbersList:
		print(element)

if __name__ == '__main__':
	printFile()