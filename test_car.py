import unittest

from car import Car, ElectricCar, PetrolCar, DieselCar, HybridCar
#
# test the car functionality
class TestCar(unittest.TestCase):

    def setUp(self):
        self.car = Car()

    def test_car_mileage(self):
        self.assertEqual(0, self.car.getMileage())
        self.car.move(15)
        self.assertEqual(15, self.car.getMileage())

    def test_car_make(self):
        self.assertEqual('', self.car.getMake())
        self.car.setMake('Ferrari')
        self.assertEqual('Ferrari', self.car.getMake())

    def test_car_colour(self):
        self.assertEqual('', self.car.getColour())
        self.car.setColour('blue')
        self.assertEqual('blue', self.car.getColour())
        self.car.paint('red')
        self.assertEqual('red', self.car.getColour())
    
    def test_engine_size(self):
        self.assertEqual(0, self.car.getEngineSize())
        self.car.setEngineSize(3)
        self.assertEqual(3, self.car.getEngineSize())
        
    def test_get_status(self):
        self.assertEqual('in stock', self.car.getStatus())
        self.car.setStatus('rented')
        self.assertEqual('rented', self.car.getStatus())
        
    def test_get_reg_number(self):
        self.assertEqual('', self.car.getRegNumber())
        self.car.setRegNumber('68BXXSTD')
        self.assertEqual('68BXXSTD', self.car.getRegNumber())
    
class TestElectricCar(unittest.TestCase):
    
    def setUp(self):
        self.electric_car = ElectricCar()
    
    def test_number_fuel_cells(self):
        self.assertEqual(1, self.electric_car.getNumberFuelCells())
        self.electric_car.setNumberFuelCells(2)
        self.assertEqual(2, self.electric_car.getNumberFuelCells())
        
    def test_car_type(self):
        self.assertEqual('electric', self.electric_car.getCarType())
        self.electric_car.setCarType('petrol')
        self.assertEqual('petrol', self.electric_car.getCarType())
        
class TestPetrolCar(unittest.TestCase):
    
    def setUp(self):
        self.petrol_car = PetrolCar()
    
    def test_number_cylinders(self):
        self.assertEqual(1, self.petrol_car.getNumberCylinders())
        self.petrol_car.setNumberCylinders(2)
        self.assertEqual(2, self.petrol_car.getNumberCylinders())
        
    def test_car_type(self):
        self.assertEqual('petrol', self.petrol_car.getCarType())
        self.petrol_car.setCarType('diesel')
        self.assertEqual('diesel', self.petrol_car.getCarType())

class TestDieselCar(unittest.TestCase):
    
    def setUp(self):
        self.diesel_car = DieselCar()
    
    def test_number_cylinders(self):
        self.assertEqual(1, self.diesel_car.getNumberCylinders())
        self.diesel_car.setNumberCylinders(2)
        self.assertEqual(2, self.diesel_car.getNumberCylinders())
        
    def test_car_type(self):
        self.assertEqual('diesel', self.diesel_car.getCarType())
        self.diesel_car.setCarType('petrol')
        self.assertEqual('petrol', self.diesel_car.getCarType())
        
class TestHybridCar(unittest.TestCase):
    
    def setUp(self):
        self.hybrid_car = HybridCar()
        
    def test_number_fuel_cells(self):
        self.assertEqual(1, self.hybrid_car.getNumberFuelCells())
        self.hybrid_car.setNumberFuelCells(2)
        self.assertEqual(2, self.hybrid_car.getNumberFuelCells())
    
    def test_number_cylinders(self):
        self.assertEqual(1, self.hybrid_car.getNumberCylinders())
        self.hybrid_car.setNumberCylinders(2)
        self.assertEqual(2, self.hybrid_car.getNumberCylinders())
        
    def test_car_type(self):
        self.assertEqual('hybrid', self.hybrid_car.getCarType())
        self.hybrid_car.setCarType('petrol')
        self.assertEqual('petrol', self.hybrid_car.getCarType())
        
if __name__ == '__main__':
    unittest.main()
