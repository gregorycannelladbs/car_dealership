# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 15:16:20 2020

@author: Greg
"""
import unittest
from dealership import Dealership
from car import Car

class TestDealership(unittest.TestCase):
# Set up the test environement
    def setUp(self):
        self.dealership = Dealership()
        self.car = Car()
        self.dealership.create_current_stock()

# Check that the function creates the corect number of cars for each car type
    def test_create_current_stock(self):
        self.assertEqual(6, len(self.dealership.electric_cars))    
        self.assertEqual(20, len(self.dealership.petrol_cars))
        self.assertEqual(10, len(self.dealership.diesel_cars))
        self.assertEqual(4, len(self.dealership.hybrid_cars))

# Check the get_data() function returns the correct total number of cars + 1
# for each cart type. We add 1 because of the header 
    def test_get_data(self):
        self.assertEqual(7, len(self.dealership.get_data(self.dealership.electric_cars)))
        self.assertEqual(21, len(self.dealership.get_data(self.dealership.petrol_cars)))
        self.assertEqual(11, len(self.dealership.get_data(self.dealership.diesel_cars)))
        self.assertEqual(5, len(self.dealership.get_data(self.dealership.hybrid_cars)))

# Check that the function correctly updates the rental status of the car
# A status cannot be changed to a value that is equal to its current status
    def test_change_status(self):
        self.dealership.change_status(self.dealership.electric_cars, 'rented', 0)
        self.assertEqual('rented', self.dealership.electric_cars[0].getStatus())
        self.assertEqual(None, self.dealership.change_status(self.dealership.electric_cars, 'rented', 0))
        

# Check that the function correctly update the mileage of the car returned.
# We can only update the mileage of the car if the car is still in status 'rented'.
    def test_change_mileage(self):
        self.dealership.change_status(self.dealership.petrol_cars, 'rented', 0)
        self.dealership.change_mileage(self.dealership.petrol_cars, 5000, 0)
        self.assertEqual(5000, self.dealership.petrol_cars[0].getMileage())
        self.dealership.change_status(self.dealership.petrol_cars, 'in stock', 0)
        self.assertEqual(None, self.dealership.change_mileage(self.dealership.petrol_cars, 5000, 0))

# based on user input check that the correct list of cars is returned
    def test_chose_car_list(self):
        self.assertEqual(self.dealership.electric_cars, self.dealership.chose_car_list('e'))
        self.assertEqual(self.dealership.petrol_cars, self.dealership.chose_car_list('p'))
        self.assertEqual(self.dealership.diesel_cars, self.dealership.chose_car_list('d'))
        self.assertEqual(self.dealership.hybrid_cars, self.dealership.chose_car_list('h'))


if __name__ == '__main__':
    unittest.main()