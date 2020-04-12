from car import Car, ElectricCar, PetrolCar, DieselCar, HybridCar
import csv
import random
import string
import numpy as np

#test_car = PetrolCar('black', 'peugeot', 3000, 1.4, 'in stock', '07LH1559', 5)

class Dealership(object):

    def __init__(self):
        self.electric_cars = []
        self.petrol_cars = []
        self.diesel_cars = []
        self.hybrid_cars = []
        self.rented_electric_cars = []
        self.rented_petrol_cars = []
        self.rented_diesel_cars = []
        self.rented_hybrid_cars = []

    def create_current_stock(self):
        colours = ['blue', 'white', 'red', 'black', 'orange'] * 8
        makes = ['jaguar', 'lamborghini', 'ferrari', 'mustang', 'maserati'] * 8
        engine_sizes = [3, 3.5, 4, 4.5, 4.7] * 8
        reg_numbers = [''.join(random.choices(string.ascii_uppercase + string.digits, k=8)) for i in range(40)]
        number_cylinders = [6, 8] * 17

        for i in range(6):
           self.electric_cars.append(ElectricCar())
           self.electric_cars[i].setColour(colours.pop())
           self.electric_cars[i].setMake(makes.pop())
           self.electric_cars[i].setEngineSize(engine_sizes.pop())
           self.electric_cars[i].setRegNumber(reg_numbers.pop())
           
        for i in range(20):
           self.petrol_cars.append(PetrolCar())
           self.petrol_cars[i].setColour(colours.pop())
           self.petrol_cars[i].setMake(makes.pop())
           self.petrol_cars[i].setEngineSize(engine_sizes.pop())
           self.petrol_cars[i].setRegNumber(reg_numbers.pop())
           self.petrol_cars[i].setNumberCylinders(number_cylinders.pop())

        for i in range(10):
           self.diesel_cars.append(DieselCar())
           self.diesel_cars[i].setColour(colours.pop())
           self.diesel_cars[i].setMake(makes.pop())
           self.diesel_cars[i].setEngineSize(engine_sizes.pop())
           self.diesel_cars[i].setRegNumber(reg_numbers.pop())
           self.diesel_cars[i].setNumberCylinders(number_cylinders.pop())

        for i in range(4):
           self.hybrid_cars.append(HybridCar())
           self.hybrid_cars[i].setColour(colours.pop())
           self.hybrid_cars[i].setMake(makes.pop())
           self.hybrid_cars[i].setEngineSize(engine_sizes.pop())
           self.hybrid_cars[i].setRegNumber(reg_numbers.pop())
           self.hybrid_cars[i].setNumberCylinders(number_cylinders.pop())

    def in_stock(self, car_list):
        cars_in_stock = [car for car in car_list if car.getStatus() == 'in stock']
        return cars_in_stock
    
    def rented_cars(self, car_list):
        rented_cars = [car for car in car_list if car.getStatus() == 'rented']
        return len(rented_cars)

    def get_data(self, car_list):      
        data = []
#        header = []
#        keys = [value for value in car_list[0].__dict__.keys()]
#        header.append(keys)
        print(car_list[0].__dict__.values())
        for car in car_list:
            values = [str(value) for value in car.__dict__.values()]
            values.insert(0, str(car_list.index(car)))
            data.append(values)
        data = np.array(data)
        data = data[np.argsort(data[:, 1])]
        return data
        
    def display_data(self, car_list):
        data = self.get_data(car_list)
        if car_list == self.electric_cars:
            print('{:<10s} {:<15s} {:<10s} {:<10s} {:<15s} {:<15s} {:<15s} {:<15s}'.format('Index', 'Make', 'Colour', 'mileage', 
                  'Engine_size', 'Status', 'Reg_number', 'Fuel_cells'))
            
            for i in data:
                print('{:<10s} {:<15s} {:<10s} {:<10s} {:<15s} {:<15s} {:<15s} {:<15s}'.format(i[0], i[1], i[2], i[3],
                          i[4], i[5], i[6], i[7]))
        
        elif car_list == self.petrol_cars or car_list == self.diesel_cars:
            print('{:<10s} {:<15s} {:<10s} {:<10s} {:<15s} {:<15s} {:<15s} {:<15s}'.format('Index', 'Make', 'Colour', 'mileage', 
                  'Engine_size', 'Status', 'Reg_number', 'Cylinders'))
            
            for i in data:
                print('{:<10s} {:<15s} {:<10s} {:<10s} {:<15s} {:<15s} {:<15s} {:<15s}'.format(i[0], i[1], i[2], i[3],
                          i[4], i[5], i[6], i[7]))
                
        elif car_list == self.hybrid_cars:
            print('{:<10s} {:<15s} {:<10s} {:<10s} {:<15s} {:<15s} {:<15s} {:<15s} {:<15s}'.format('Index', 'Make', 'Colour', 
                  'mileage', 'Engine_size', 'Status', 'Reg_number', 'Fuel_cells', 'Cylinders'))
                
            for i in data:
                print('{:<10s} {:<15s} {:<10s} {:<10s} {:<15s} {:<15s} {:<15s} {:<15s} {:<15s}'.format(i[0], i[1], i[2], i[3],
                      i[4], i[5], i[6], i[7], i[8]))
    
    def change_status(self, car_list, status):
        answer = eval(input('Enter the index of the car you want to rent: '))
        car_list[answer].setStatus(status)
        
    def chose_car_list(self):
#        answer = input('would you like to rent "r" or return "b" a car? r/b ')
        car_type = input('what type would you like to rent? p/e/d/h ')

        if car_type == 'e':
            return self.electric_cars
        
        elif car_type == 'p':
            return self.petrol_cars
        
        elif car_type == 'd':
            return self.diesel_cars
        
        else:
            return self.hybrid_cars 

    def main():
        dealership = Dealership()
        answer = input('Do you want start from scratch "1", or load previously saved data "2"? ')
        if answer == '1':
            dealership.create_current_stock()
        else:
            pass
        proceed = 'y'
        while proceed == 'y':
            answer = input('would you like to rent "r" or return "b" a car? r/b ')
            if answer == 'r':
                status = 'rented'
            else:
                status = 'in stock'
            car_list = dealership.chose_car_list()
            dealership.display_data(car_list)
            dealership.change_status(car_list, status)
            proceed = input('continue? y/n ')
            
        data = dealership.get_data(car_list)
        answer = input('would you like to save changes made? y/n ')
        if answer == 'y':
            with open("output.csv", "w", newline="",  encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerows(data)
                f.close()

if __name__ == '__main__':
   Dealership.main()