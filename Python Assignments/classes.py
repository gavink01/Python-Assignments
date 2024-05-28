class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"Car(Make: {self.make}, Model: {self.model}, Year: {self.year})"

    def getMake(self):
        return self.make
    
    def getModel(self):
        return self.model
    
    def getYear(self):
        return self.year
    
    def setMake(self, make):
        self.make = make

    def setModel(self, model):
        self.model = model
    
    def setYear(self, year):
        self.year = year

car = Car("Ford","Ranger","1998")
print(car)
print(car.getMake())
car.setMake("Chevy")
print(car.getMake())