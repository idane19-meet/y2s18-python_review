class SuperHero:
    def __init__(self,name,superpower,strength):
        self.name = name
        self.superpower = superpower
        self.strength = strength
    
    def print_me(self):
        print("My name is " + self.name + " ,And my super power is " + self.  superpower)
    def save_civilian(self):
        work = int(input("Enter a number:"))
        if self.strength - work < 0:
            print("Superhero is not strong enough! :(")
        else:
            self.strength -= work
a = SuperHero("superman","laser",10)
a.save_civilian()