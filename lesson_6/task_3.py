class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = income
        
class Position(Worker):
    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)
        
    def get_full_name(self):
        return (self.name + " " + self.surname) 
    
    def get_total_income(self):
        return (self.income["wage"] + self.income["bonus"])
    
    
print(Position("John", "Smith", "asd", {"wage": 123, "bonus": 15}).get_full_name())
print(Position("John", "Smith", "asd", {"wage": 123, "bonus": 15}).get_total_income())