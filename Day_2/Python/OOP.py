#Basic OOP

class Animal():
    animal = "mammal"
    def __init__(self,name,color,country,number) -> None:
        self.color = color
        self.name = name 
        self.country = country
        self.number = number
    def __repr__(self) -> str:
        return f'Name:{self.name},Color:{self.color},Country:{self.country}'
    def __len__(self):
        return self.number
    
    
cow = Animal('meow',"red","India",65)
print(cow.country)
print(len(cow))