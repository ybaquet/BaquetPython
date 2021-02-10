class Intern:

    def __init__(self, name="My name? I’m nobody, an intern, I have no name."):
        self.Name = name

    def __str__(self):
        return self.Name
    
    def work(self):
        raise Exception("I’m just an intern, I can’t do that...")
    
    class Coffee:
        def __str__(self):
            return "This is the worst coffee you ever tasted."

    def make_coffee(self):
        return self.Coffee()
        
if __name__ == "__main__":
    mark = Intern("Mark")
    print(mark)
    noname = Intern()
    print(noname)
    cafe = mark.make_coffee()
    print(cafe)
    try:
        mark.work()
    except Exception as e:
        print("Error: " + str(e))