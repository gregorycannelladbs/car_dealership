from car import Car, ElectricCar, PetrolCar, DieselCar, HybridCar
import csv
import random
import string

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
        colours = ['blue', 'white', 'red', 'black', 'green'] * 8
        makes = ['Jaguar', 'lamborghini', 'Ferrari', 'mustang'] * 8
        engine_sizes = [3, 3.5, 4, 4.5, 4.7] * 8
        reg_numbers = [''.join(random.choices(string.ascii_uppercase + string.digits, k=8)) for i in range(40)]
        numer_cylinders = [6, 8] * 9

        for i in range(6):
           self.electric_cars.append(ElectricCar())
           self.electric_cars[i].setColour(colours.pop())
           self.electric_cars[i].setMake(makes.pop())
           self.electric_cars[i].setMake(engine_sizes.pop())
           self.electric_cars[i].setRegNumber(reg_numbers.pop())
           #print(self.electric_cars[i].__dict__)
           
        for i in range(20):
           self.petrol_cars.append(PetrolCar())
           self.petrol_cars[i].setColour(colours.pop())
           self.petrol_cars[i].setMake(makes.pop())
           self.petrol_cars[i].setMake(engine_sizes.pop())
           self.petrol_cars[i].setRegNumber(reg_numbers.pop())

        for i in range(10):
           self.diesel_cars.append(DieselCar())
        for i in range(4):
           self.hybrid_cars.append(HybridCar())
            
    def stock_count(self):
        print('petrol cars in stock '+ str(len(self.petrol_cars)))
        print('electric cars in stock ' + str(len(self.electric_cars)))
        print('Diesel cars in stock ' + str(len(self.diesel_cars)))
        print('Hybrid cars in stock ' + str(len(self.hybrid_cars)))
        print('rented petrol cars ' + str(len(self.rented_petrol_cars)))
        print('rented electric cars ' + str(len(self.rented_electric_cars)))
        print('rented diesel cars ' + str(len(self.rented_diesel_cars)))
        print('rented hybrid cars ' + str(len(self.rented_hybrid_cars)))

    def rent(self, from_car_list, to_car_list, number):
        if len(from_car_list) < number:
            print('\nNot enough cars in stock ! Try again.')
            return
        total = 0
        while total < number:
           total = total + 1
           to_car_list.append(from_car_list.pop())
     
    def return_car(self, from_car_list, to_car_list, number):
        if len(from_car_list) < number:
            print('\nToo many car returned ! Try again.')
            return
        total = 0
        while total < number:
           total = total + 1
           to_car_list.append(from_car_list.pop())
           
    def process_rental(self):
        answer = input('would you like to rent "r" or return "b" a car? r/b ')
        if answer == 'r':
            answer = input('what type would you like to rent? p/e/d/h ')
            number = int(input('how many would you like to rent? '))
            if answer == 'p':
                self.rent(self.petrol_cars, self.rented_petrol_cars, number)
            elif answer == 'e':
                self.rent(self.electric_cars, self.rented_electric_cars, number)
            elif answer == 'd':
                self.rent(self.diesel_cars, self.rented_diesel_cars, number)
            else:
                self.rent(self.hybrid_cars, self.rented_hybrid_cars, number)
        
        else:
            answer = input('what type would you like to return ? p/e/d/h ')
            number = int(input('how many would you like to return? '))
            if answer == 'p':
                self.return_car(self.rented_petrol_cars, self.petrol_cars, number)
            elif answer == 'e':
                self.return_car(self.rented_electric_cars, self.electric_cars, number)
            elif answer == 'd':
                self.return_car(self.rented_diesel_cars, self.diesel_cars, number)
            else:
                self.return_car(self.rented_hybrid_cars, self.hybrid_cars, number)
        
        print("")
        self.stock_count()
        
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