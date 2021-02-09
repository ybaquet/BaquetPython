import sys

def capital_city(state):
    states = {
    "Oregon" : "OR",
    "Alabama" : "AL", "New Jersey": "NJ",
    "Colorado" : "CO"
    }
    capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
    }
    if state not in states:
        print("Unknown state")
    else:
        print(capital_cities[states[state]])

if __name__ == "__main__":
    if 2 == len(sys.argv):
        capital_city(sys.argv[1])