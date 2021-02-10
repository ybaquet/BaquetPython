from beverages import *
import random

class CoffeeMachine:
    
    def __init__(self):
        self.count = 0
        
    class EmptyCup(Hotbeverage):
        description = "An empty cup?! Gimme my money back!"

        def __init__(self):
            Hotbeverage.__init__(self, 0.90, "empty cup")

    class BrokenMachineException(Exception):
        def __init__(self, msg= "This coffee machine has to be repaired."):
            Exception.__init__(self, msg)
    
    def repair(self):
        self.count = 0

    def serve(self, Boisson):
        if self.count >= 10:
            raise CoffeeMachine.BrokenMachineException()
        self.count += 1
        if 1 == random.randint(0, 1):
            return self.EmptyCup()
        else:
            return Boisson()
             
if __name__ == '__main__':
    coffeeMachine = CoffeeMachine()
    i = 0
    while i < 5:
        i += 1
        try:
            coffeeMachine.repair()
            print("1")
            print(coffeeMachine.serve(Tea))
            print("------------- \n2.")
            print(coffeeMachine.serve(Coffee))
            print("------------- \n3.")
            print(coffeeMachine.serve(Chocolate))
            print("------------- \n4.")
            print(coffeeMachine.serve(Capuccino))
            print("------------- \n5.")
            print(coffeeMachine.serve(Tea))
            print("------------- \n6.")
            print(coffeeMachine.serve(Tea))
            print("------------- \n7.")
            print(coffeeMachine.serve(Coffee))
            print("------------- \n8.")
            print(coffeeMachine.serve(Coffee))
            print("------------- \n9.")
            print(coffeeMachine.serve(Chocolate))
            print("------------- \n10.")
            print(coffeeMachine.serve(Chocolate))
            print("------------- \n11.")
            print(coffeeMachine.serve(Chocolate))
            print("------------- \n12.")
            print(coffeeMachine.serve(Tea))
            print("------------- \n13.")
            print(coffeeMachine.serve(Tea))
            print("------------- \n14.")
            print(coffeeMachine.serve(Tea))
            print("------------- \n15.")
            print(coffeeMachine.serve(Tea))
            print("------------- \n16.")
            print(coffeeMachine.serve(Tea))
            print("------------- \n17.")
            print(coffeeMachine.serve(Tea))
        except coffeeMachine.BrokenMachineException as e:
            print(e)
