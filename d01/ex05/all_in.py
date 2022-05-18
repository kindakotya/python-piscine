import sys
states = {
		"Oregon" : "OR",
		"Alabama" : "AL",
		"New Jersey": "NJ",
		"Colorado" : "CO"
		}
capital_cities = {
				"OR": "Salem",
				"AL": "Montgomery",
				"NJ": "Trenton",
				"CO": "Denver"
				}


def printMagic(string):
	capital = capital_cities.get(states.get(sys.argv[1]))
	if capital != None:
		print(capital)
	else:
		print("Unknown state")


def makeMagic(inputString):
	inputListLower = list(map(str.strip, str.lower(inputString).split(',')))
	statesLower = { str.lower(state): ab for (state, ab) in states.items() }
	capital_citiesLover = { capital: str.lower(ab) for (capital, ab) in capital_cities.items() }
	for element in inputListLower:
		kek = statesLower.get(element)
		if kek != None:
			print(kek)
	print()
	#for element in inputList:
		

if __name__ == '__main__':
	#if len(sys.argv) == 2:
		makeMagic("Meow, mem, Oregon, DdFtVV")#sys.argv[1])