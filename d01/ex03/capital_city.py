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

def printCapital(state):
	capital = capital_cities.get(states.get(sys.argv[1]))
	if capital != None:
		print(capital)
	else:
		print("Unknown state")


if __name__ == '__main__':
	if len(sys.argv) == 2:
		printCapital(sys.argv[1])