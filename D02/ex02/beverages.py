class Hotbeverage:

    def _init__(self, price=0.30, name="hot beverage", description="Just some hot water in a cup."):
        self.price = price
        self.name = name
        
    def __str__(self):
        str = "desc = name : " + self.name + \
              "\nprice : " + "%.2f" % self.price + \
              "\ndesciption : " + self.description
        return str

class Coffee(Hotbeverage):
    def __init__(self):
        Hotbeverage.__init__(self, 0.40, "coffee", "A coffee, to stay awake.")

class Tea(Hotbeverage):
    def __init__(self):
        super.__init__(self, 0.30, "tee", "Just some hot water in a cup.")

class Chocolate(Hotbeverage):
    def __init__(self):
        super.__init__(self, 0.50, "chocolate", "Chocolate, sweet chocolate...")

class Capuccino(Hotbeverage):
    def __init__(self):
        super.__init__(self, 0.45, "capuccino", "Un po’ di Italia nella sua tazza!")
        
if __name__ == "__main__":
    hotbeverage = Hotbeverage()
    coffe = Coffee()
    tea = Tea()
    chocolate = Chocolate()
    capuccino = Cappucino()
    print(hotbeverage)
