class player:
    def __init__(self, name, health=100):
        self.name=name
        self.__health=health
    
    def take_damage(self,amount):
        if amount < 0:
            raise ValueError ("Negative not allowed")
        self.__health -=amount
        
        if self.__health<0:
            self.__health=0
        print(f"{self.name} took {amount} damage. Health now is {self.__health}")

    def heal(self, amount):
        if amount < 0:
            raise ValueError ("Negative not allowed")
        self.__health += amount

        if self.__health>100:
            self.__health=100
        print(f"{self.name} healed by {amount} points. Health now is {self.__health}")

    def get_health(self):
        self.__health

p=player("john")
p.take_damage(30)
p.heal(40)
p.take_damage(150)
print(p.get_health())

