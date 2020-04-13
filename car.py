# Define a class for my car

class Car(object):
    # implement the car object.#
    
    def __init__(self):
        self.__make = ''
        self.__colour = ''
        self.__mileage = 0
        self.__engineSize = 0
        self.__status = 'in stock'
        self.__reg_number = ''

    def getMake(self):
        return self.__make
    
    def getColour(self):
        return self.__colour

    def getMileage(self):
        return self.__mileage
    
    def getEngineSize(self):
        return self.__engineSize
    
    def getStatus(self):
        return self.__status

    def getRegNumber(self):
        return self.__reg_number

    def setMake(self, make):
        self.__make = make
        
    def setColour(self, colour):
        self.__colour = colour

    def setMileage(self, mileage):
        self.__mileage = mileage
        
    def setEngineSize(self, engineSize):
        self.__engineSize = engineSize
        
    def setStatus(self, status):
        self.__status = status

    def setRegNumber(self, reg_number):
        self.__reg_number = reg_number
        
    def paint(self, colour):
        self.__colour = colour
        return self.__colour

    def move(self, distance):
        self.__mileage = self.__mileage + distance
        return self.__mileage

class ElectricCar(Car):
    
    def __init__(self):
        Car.__init__(self)
        self.__numberFuelCells = 1
        self.__car_type = 'electric'

    def getNumberFuelCells(self):
        return self.__numberFuelCells
    
    def getCarType(self):
        return self.__car_type

    def setNumberFuelCells(self, value):
        self.__numberFuelCells = value
    
    def setCarType(self, value):
        self.__car_type = value


class PetrolCar(Car):

    def __init__(self):
        Car.__init__(self)
        self.__numberCylinders = 1
        self.__car_type = 'petrol'

    def getNumberCylinders(self):
        return self.__numberCylinders
    
    def getCarType(self):
        return self.__car_type

    def setNumberCylinders(self, value):
        self.__numberCylinders = value
    
    def setCarType(self, value):
        self.__car_type = value

class DieselCar(Car):

    def __init__(self):
        Car.__init__(self)
        self.__numberCylinders = 1
        self.__car_type = 'diesel'

    def getNumberCylinders(self):
        return self.__numberCylinders

    def getCarType(self):
        return self.__car_type

    def setNumberCylinders(self, value):
        self.__numberCylinders = value
    
    def setCarType(self, value):
        self.__car_type = value
        
class HybridCar(Car):
    
    def __init__(self):
        Car.__init__(self)
        self.__numberFuelCells = 1
        self.__numberCylinders = 1
        self.__car_type = 'hybrid'

    def getNumberFuelCells(self):
        return self.__numberFuelCells

    def getNumberCylinders(self):
        return self.__numberCylinders

    def getCarType(self):
        return self.__car_type
    
    def setNumberFuelCells(self, value):
        self.__numberFuelCells = value

    def setNumberCylinders(self, value):
        self.__numberCylinders = value
    
    def setCarType(self, value):
        self.__car_type = value
