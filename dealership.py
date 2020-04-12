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
        
    def get_electric_cars(self):
        return self.electric_cars
    
    def get_petrol_cars(self):
        return self.petrol_cars
    
    def get_diesel_cars(self):
        return self.diesel_cars
    
    def get_hybrid_cars(self):
        return self.hybrid_cars
    
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
            print('\n{:<10s} {:<15s} {:<10s} {:<10s} {:<15s} {:<15s} {:<15s} {:<15s} {:<15s}'.format('Index', 'Make', 'Colour', 
                  'mileage', 'Engine_size', 'Status', 'Reg_number', 'Fuel_cells', 'Car_type'))
            
            for i in data:
                print('{:<10s} {:<15s} {:<10s} {:<10s} {:<15s} {:<15s} {:<15s} {:<15s} {:<15s}'.format(i[0], i[1], i[2], i[3],
                          i[4], i[5], i[6], i[7], i[8]))
        
        elif car_list == self.petrol_cars or car_list == self.diesel_cars:
            print('\n{:<10s} {:<15s} {:<10s} {:<10s} {:<15s} {:<15s} {:<15s} {:<15s} {:<15s}'.format('Index', 'Make', 'Colour', 
                  'mileage', 'Engine_size', 'Status', 'Reg_number', 'Cylinders', 'Car_type'))
            
            for i in data:
                print('{:<10s} {:<15s} {:<10s} {:<10s} {:<15s} {:<15s} {:<15s} {:<15s} {:<15s}'.format(i[0], i[1], i[2], i[3],
                          i[4], i[5], i[6], i[7], i[8]))
                
        elif car_list == self.hybrid_cars:
            print('\n{:<10s} {:<15s} {:<10s} {:<10s} {:<15s} {:<15s} {:<15s} {:<15s} {:<15s} {:<15s}'.format('Index', 'Make', 
                  'Colour', 'mileage', 'Engine_size', 'Status', 'Reg_number', 'Fuel_cells', 'Cylinders', 'Car_type'))
                
            for i in data:
                print('{:<10s} {:<15s} {:<10s} {:<10s} {:<15s} {:<15s} {:<15s} {:<15s} {:<15s} {:<15s}'.format(i[0], i[1], i[2], 
                      i[3], i[4], i[5], i[6], i[7], i[8], i[9]))
    
    def change_status(self, car_list, status, index): 
        car_list[index].setStatus(status)
        
    def change_mileage(self, car_list, mileage, index):
        car_list[index].setMileage(mileage)
        
    def chose_car_list(self, car_type):
        if car_type == 'e':
            return self.electric_cars
        
        elif car_type == 'p':
            return self.petrol_cars
        
        elif car_type == 'd':
            return self.diesel_cars
        
        else:
            return self.hybrid_cars
    
#    def save_original_data(self):
#            self.create_current_stock()
#            file_names = ['electric_cars', 'petrol_cars', 'diesel_cars', 'hybrid_cars']
#            index = 0
#            for i in (self.get_data(self.electric_cars), self.get_data(self.petrol_cars),
#                      self.get_data(self.diesel_cars), self.get_data(self.hybrid_cars)):
#                file_name = file_names[index] + '.csv'
#                index += 1
#                with open(file_name, "w", newline="",  encoding='utf-8') as f:
#                    writer = csv.writer(f)
#                    writer.writerows(i)
#                    f.close()
    
#    def load_data(self):
#            file_names = ['electric_cars', 'petrol_cars', 'diesel_cars', 'hybrid_cars']
#            index = 0
#            for i in (self.get_data(self.electric_cars), self.get_data(self.petrol_cars),
#                      self.get_data(self.diesel_cars), self.get_data(self.hybrid_cars)):
#                file_name = file_names[index] + '.csv'
#                index += 1
#                with open(file_name, newline='') as f:
#                    reader = csv.reader(f)
#                    next(reader, None)  # Skip the header.
#                    # Unpack the row directly in the head of the for loop.
#                    for name, score1, score2, rank in reader:
#                        # Convert the numbers to floats.
#                        score1 = float(score1)
#                        score2 = float(score2)
#                        rank = float(rank)
#                        # Now create the Student instance and append it to the list.
#                        i.append(Student(name, (score1, score2), rank))

    def main():
        dealership = Dealership()
        answer = input('\nDo you want to start from scratch "1", or load previously saved data "2"? ')                    
        if answer == '1':
            dealership.create_current_stock()
            proceed = 'y'
            while proceed == 'y':
                answer = input('\nWould you like to rent "r" or return "b" a car? ')
                if answer == 'r':
                    status = 'rented'
                    car_type = input('\nWhat type would you like to rent? p/e/d/h ')
                    car_list = dealership.chose_car_list(car_type)
                    dealership.display_data(car_list)
                    index = eval(input('\nEnter the index of the car you want to rent: '))
                    dealership.change_status(car_list, status, index)
                
                else:
                    status = 'in stock'
                    mileage = eval(input('\nWhat is the mileage of the car on return? '))
                    car_list = dealership.chose_car_list()
                    dealership.display_data(car_list)
                    index = eval(input('\nEnter the index of the car you want to return: '))
                    dealership.change_status(car_list, status, index)
                    dealership.change_mileage(car_list, mileage, index) 
                
                answer = input('\nWould you like to save changes made? y/n ')
                if answer == 'y':
                    data = dealership.get_data(car_list)
                    file_name = car_list[0].getCarType() + '_cars.csv'
                    with open(file_name, "w", newline="",  encoding='utf-8') as f:
                        writer = csv.writer(f)
                        writer.writerows(data)
                        f.close()
            
                proceed = input('\nWould you like to continue y/n? ')
            
        else:
            print('\nSorry this feature is not available yet. I am working hard to make this feature available in a near future')
                
#            file_names = ['electric_cars', 'petrol_cars', 'diesel_cars', 'hybrid_cars']
#            for i in (dealership.get_data(dealership.electric_cars), dealership.get_data(dealership.petrol_cars),
#                      dealership.get_data(dealership.petrol_cars), dealership.get_data(dealership.hybrid_cars)):
#                with open(file_names[index], newline='') as f:
#                    reader = csv.reader(f)
#                    next(reader, None)  # Skip the header.
#                    # Unpack the row directly in the head of the for loop.
#                    for name, score1, score2, rank in reader:
#                        # Convert the numbers to floats.
#                        score1 = float(score1)
#                        score2 = float(score2)
#                        rank = float(rank)
#                        # Now create the Student instance and append it to the list.
#                        i.append(Student(name, (score1, score2), rank))
                    

            
if __name__ == '__main__':
   Dealership.main()