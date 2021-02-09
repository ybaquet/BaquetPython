import sys

def all_in(argument):
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
    for arg in argument.split(','):
        notfound = True
        key = arg.strip()
        if len(key):
            for key1, value1 in capital_cities.items():
                if key.casefold() == value1.casefold():
                    for key2, value2 in states.items():
                        if key1 == value2:
                            print(value1, "is the capital of", key2)
                            notfound = False
            if notfound:
                for key1, value1 in states.items():
                    if key.casefold() == key1.casefold():
                         print(capital_cities[value1], "is the capital of", key1)
                         notfound = False
            if notfound:
                print(key, "is neither a capital city nor a state")

if __name__ == "__main__":
    if 2 == len(sys.argv):
        all_in(sys.argv[1])
