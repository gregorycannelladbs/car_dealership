# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 15:16:20 2020

@author: Greg
"""
import unittest
from dealership import Dealership
from car import Car

class TestDealership(unittest.TestCase):

    def setUp(self):
        self.dealership = Dealership()
        self.car = Car()
        self.dealership.create_current_stock()

    def test_create_current_stock(self):
        self.assertEqual(6, len(self.dealership.electric_cars))    
        self.assertEqual(20, len(self.dealership.petrol_cars))
        self.assertEqual(10, len(self.dealership.diesel_cars))
        self.assertEqual(4, len(self.dealership.hybrid_cars))
    
    def test_get_data(self):
        for sublist in self.dealership.get_data(self.dealership.electric_cars):
            self.assertTrue(len(sublist), 6)
        
        for sublist in self.dealership.get_data(self.dealership.petrol_cars):
            self.assertTrue(len(sublist), 20)
            
        for sublist in self.dealership.get_data(self.dealership.diesel_cars):
            self.assertTrue(len(sublist), 9)
        
        for sublist in self.dealership.get_data(self.dealership.hybrid_cars):
            self.assertTrue(len(sublist), 4)
    
    def test_change_status(self):
        self.dealership.change_status(self.dealership.electric_cars, 'rented', 0)
        self.assertEqual('rented', self.dealership.electric_cars[0].getStatus())
    
    def test_change_mileage(self):
        self.dealership.change_mileage(self.dealership.petrol_cars, 5000, 0)
        self.assertEqual(5000, self.dealership.petrol_cars[0].getMileage())
        
    def test_chose_car_list(self):
        self.assertEqual(self.dealership.electric_cars, self.dealership.chose_car_list('e'))
        self.assertEqual(self.dealership.petrol_cars, self.dealership.chose_car_list('p'))
        self.assertEqual(self.dealership.diesel_cars, self.dealership.chose_car_list('d'))
        self.assertEqual(self.dealership.hybrid_cars, self.dealership.chose_car_list('h'))

if __name__ == '__main__':
    unittest.main()