class Hotbeverage:
    description ="Just some hot water in a cup."

    def __init__(self, price = 0.30, name = "hot beverage"):
        self.price = price
        self.name = name
        
    def __str__(self):
        str = "desc = name : " + self.name + \
              "\nprice : " + "%.2f" % self.price + \
              "\ndesciption : " + self.description
        return str

class Coffee(Hotbeverage):
    description = "Just some hot water in a cup."
    
    def __init__(self):
        Hotbeverage.__init__(self, 0.40, "coffee")

class Tea(Hotbeverage):
    description = "Just some hot water in a cup."
    
    def __init__(self):
        Hotbeverage.__init__(self, 0.30, "tea")

class Chocolate(Hotbeverage):
    description = "Chocolate, sweet chocolate..."
    
    def __init__(self):
        Hotbeverage.__init__(self, 0.50, "chocolate")

class Capuccino(Hotbeverage):
    description = "Un po' di Italia nella sua tazza!"
    
    def __init__(self):
        Hotbeverage.__init__(self, 0.45, "capuccino")