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
           #print(self.electric_cars[i].__dict__)
           
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
    
#        stock_petrol_cars = [car for car in self.petrol_cars if car.getStatus() == 'in stock']
#        stock_diesel_cars = [car for car in self.diesel_cars if car.getStatus() == 'in stock']
#        stock_hybrid_cars = [car for car in self.hybrid_cars if car.getStatus() == 'in stock']
#        
#        print('electric cars in stock '+ str(len(stock_electric_cars)))
#        print('petrol cars in stock '+ str(len(stock_petrol_cars)))
#        print('diesel cars in stock '+ str(len(stock_diesel_cars)))
#        print('hybrid cars in stock '+ str(len(stock_hybrid_cars)))

#        print('make', 'colour', 'engine_size', 'number_of_cylinders', 'reg_number')
#        for car in stock_electric_cars:
#            print(car.getMake(), car.getColour(), car.getNumberFuelCells(), car.getEngineSize(), car.getRegNumber())
#            

        
        
#        print('petrol cars in stock '+ str(len(self.petrol_cars)))
#        print('electric cars in stock ' + str(len(self.electric_cars)))
#        print('Diesel cars in stock ' + str(len(self.diesel_cars)))
#        print('Hybrid cars in stock ' + str(len(self.hybrid_cars)))
#        print('rented petrol cars ' + str(len(self.rented_petrol_cars)))
#        print('rented electric cars ' + str(len(self.rented_electric_cars)))
#        print('rented diesel cars ' + str(len(self.rented_diesel_cars)))
#        print('rented hybrid cars ' + str(len(self.rented_hybrid_cars)))

    def rent(self, car_list):      
        data = []
        header = []
        keys = [value for value in car_list[0].__dict__.keys()]
        header.append(keys)
        for car in self.in_stock(car_list):
            values = [str(value) for value in car.__dict__.values()]
            values.insert(0, str(car_list.index(car)))
            data.append(values)
        data = np.array(data)
        data = data[np.argsort(data[:, 1])]

        if car_list == self.electric_cars:
            for i in header:
                print('{:<10s} {:<15s} {:<10s} {:<10s} {:<15s} {:<15s} {:<15s} {:<15s}'.format('Index', 'Make', 'Colour', 'mileage', 
                      'Engine_size', 'Status', 'Reg_number', 'Fuel_cells'))
            
            for i in data:
                print('{:<10s} {:<15s} {:<10s} {:<10s} {:<15s} {:<15s} {:<15s} {:<15s}'.format(i[0], i[1], i[2], i[3],
                          i[4], i[5], i[6], i[7]))
        
        elif car_list == self.petrol_cars or self.diesel_cars:
            for i in header:
                print('{:<10s} {:<15s} {:<10s} {:<10s} {:<15s} {:<15s} {:<15s} {:<15s}'.format('Index', 'Make', 'Colour', 'mileage', 
                      'Engine_size', 'Status', 'Reg_number', 'Cylinders'))
            
            for i in data:
                print('{:<10s} {:<15s} {:<10s} {:<10s} {:<15s} {:<15s} {:<15s} {:<15s}'.format(i[0], i[1], i[2], i[3],
                          i[4], i[5], i[6], i[7]))
                
        elif len(data[0]) == self.hybrid_cars:
            for i in header:
                print('{:<10s} {:<15s} {:<10s} {:<10s} {:<15s} {:<15s} {:<15s} {:<15s} {:<15s}'.format('Index', 'Make', 'Colour', 
                      'mileage', 'Engine_size', 'Status', 'Reg_number', 'Fuel_cells', 'Cylinders'))
                
            for i in data:
                print('{:<15s} {:<15s} {:<10s} {:<10s} {:<15s} {:<15s} {:<15s} {:<15s} {:<15s}'.format(i[0], i[1], i[2], i[3],
                      i[4], i[5], i[6], i[7], i[8]))
                
#            print('\n',  car_list.index(car), end=' ')
#            for value in car.__dict__.values():
#                print(value, end=' ')
#                    print(car_list.index(car), car.__dict__.values())
        answer = eval(input('Enter the index of the car you want to rent: '))
        car_list[answer].setStatus('rented')
        print(len(self.in_stock(car_list)))
#    else:
#        print('Only' + str(len(self.in_stock(car_list))) + 'in stock.')
     
    def return_car(self, car_list, number):
        data = []
        header = []
        keys = [value for value in car_list[0].__dict__.keys()]
        header.append(keys)
        for car in self.rented_cars(car_list):
            print(car_list.index(car), car.getMake(), 
                  car.getColour(), car.getNumberFuelCells(), car.getEngineSize(), car.getRegNumber())
        answer = eval(input('type the index of the car you want to return: '))
        car_list[answer].setStatus('in stock')
        print(len(self.rented_cars(car_list)))
#        else:
#            print('Too many car returned. Only' + str(len(self.in_stock(car_list))) + 'currently rented')
           
    def process_rental(self):
        answer = input('would you like to rent "r" or return "b" a car? r/b ')
        if answer == 'r':
            answer = input('what type would you like to rent? p/e/d/h ')
            if answer == 'e':
                self.rent(self.electric_cars)
            
            elif answer == 'p':
                self.rent(self.petrol_cars)
            
            elif answer == 'd':
                self.rent(self.diesel_cars)
            
            else:
                self.rent(self.hybrid_cars) 
        
        else:
            answer = input('what type would you like to return ? p/e/d/h ')
            if answer == 'e':
                self.return_car(self.rented_electric_cars)
            elif answer == 'p':
                self.return_car(self.rented_petrol_cars)
                
            elif answer == 'd':
                self.return_car(self.rented_diesel_cars)
            else:
                self.return_car(self.rented_hybrid_cars)
        
#        print("")
#        self.stock_count()
        
    def get_rental_status(self):
        rental_status = [
                ['electric_cars', len(self.electric_cars)],
                ['petrol_cars', len(self.petrol_cars)], 
                ['diesel_cars', len(self.diesel_cars)],
                ['hybrid_cars', len(self.hybrid_cars)], 
                ['rented_electric_cars', len(self.rented_electric_cars)], 
                ['rented_petrol_cars', len(self.rented_petrol_cars)],
                ['rented_diesel_cars', len(self.rented_diesel_cars)], 
                ['rented_hybrid_cars', len(self.rented_hybrid_cars)]
                ]
        return rental_status
        
    def main():
        dealership = Dealership()
        dealership.create_current_stock()
        proceed = 'y'
        while proceed == 'y':
            dealership.process_rental()
            proceed = input('continue? y/n ')
        data = dealership.get_rental_status()
        answer = input('would you like to save changes made? y/n ')
        if answer == 'y':
            with open("output.csv", "w", newline="",  encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerows(data)
                f.close()

if __name__ == '__main__':
   Dealership.main()