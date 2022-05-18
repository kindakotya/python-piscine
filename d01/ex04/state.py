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

def printState(capital):
	state = next((k for k in capital_cities if capital_cities[k] == capital), None)
	stateFullName = next((k for k in states if states[k] == state), None)
	if stateFullName != None:
		print(stateFullName)
	else:
		print("Unknown capital city")

if __name__ == '__main__':
	if len(sys.argv) == 2:
		printState(sys.argv[1])