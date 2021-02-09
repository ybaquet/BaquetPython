import sys

def capital_city(city):
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
    notfound = True
    for key1, value1 in capital_cities.items():
        if city == value1:
            for key2, value2 in states.items():
                if key1 == value2:
                    print(key2)
                    notfound = False  
    if notfound:
        print("Unknown capital city")

if __name__ == "__main__":
    if 2 == len(sys.argv):
        capital_city(sys.argv[1])