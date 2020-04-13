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

# create original stock when using the application for the first time
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

# get the car attribute values of a list of cars + the header
    def get_data(self, car_list):      
        if car_list == self.electric_cars:
            data = [['Index', 'Make', 'Colour', 'Mileage', 'Engine_size', 'Status', 'Reg_number', 'Fuel_cells', 'Car_type']]
        
        elif car_list == self.petrol_cars or car_list == self.diesel_cars:
            data = [['Index', 'Make', 'Colour', 'Mileage', 'Engine_size', 'Status', 'Reg_number', 'Cylinders', 'Car_type']]
        
        elif car_list == self.hybrid_cars:
            data = [['Index', 'Make', 'Colour', 'Mileage', 'Engine_size', 'Status', 'Reg_number', 'Fuel_cells', 'Cylinders', 
                    'Car_type']]
            
        for car in car_list:
            values = [str(value) for value in car.__dict__.values()]
            values.insert(0, str(car_list.index(car)))
            data.append(values)
            
        return data

# Get the data attributes of a car list in the correct shape and display it to the screen        
    def display_data(self, car_list):
        data = self.get_data(car_list)

        if car_list == self.electric_cars:
            for i in data:
                print('{:<10s} {:<15s} {:<10s} {:<10s} {:<15s} {:<15s} {:<15s} {:<15s} {:<15s}'.format(i[0], i[1], i[2], i[3],
                          i[4], i[5], i[6], i[7], i[8]))
        
        elif car_list == self.petrol_cars or car_list == self.diesel_cars:
            for i in data:
                print('{:<10s} {:<15s} {:<10s} {:<10s} {:<15s} {:<15s} {:<15s} {:<15s} {:<15s}'.format(i[0], i[1], i[2], i[3],
                          i[4], i[5], i[6], i[7], i[8]))
                
        elif car_list == self.hybrid_cars:
            for i in data:
                print('{:<10s} {:<15s} {:<10s} {:<10s} {:<15s} {:<15s} {:<15s} {:<15s} {:<15s} {:<15s}'.format(i[0], i[1], i[2], 
                      i[3], i[4], i[5], i[6], i[7], i[8], i[9]))
    
# Change the status of a car. A car is either 'rented' or 'in stock' 
    def change_status(self, car_list, status, index): 
        if car_list[index].getStatus() == status:
            print('\nSorry the car is already either Rented or In Stock')
        else:
            car_list[index].setStatus(status)

#  Change the mileage of a car        
    def change_mileage(self, car_list, mileage, index):
        car_list[index].setMileage(mileage)

# Based on user input return the correct list of cars         
    def chose_car_list(self, car_type):
        if car_type == 'e':
            return self.electric_cars
        
        elif car_type == 'p':
            return self.petrol_cars
        
        elif car_type == 'd':
            return self.diesel_cars
        
        else:
            return self.hybrid_cars

# Save the original data when the app is launched for the first time.
# The user needes to select option '1' when launching the app for the first time.    
    def save_original_data(self):
            file_names = ['electric_cars', 'petrol_cars', 'diesel_cars', 'hybrid_cars']
            index = 0
            data_electric = self.get_data(self.electric_cars)
            data_petrol = self.get_data(self.petrol_cars)
            data_diesel = self.get_data(self.diesel_cars)
            data_hybrid = self.get_data(self.hybrid_cars)
            for i in (data_electric, data_petrol, data_diesel, data_hybrid):
                data = [item[1:] for item in i]
                file_name = file_names[index] + '.csv'
                index += 1
                with open(file_name, "w", newline="",  encoding='utf-8') as f:
                    writer = csv.writer(f)
                    writer.writerows(data)
                    f.close()

# Load data if the app has been used at least once in the past     
    def load_data(self):
            file_names = ['electric_cars', 'petrol_cars', 'diesel_cars', 'hybrid_cars']
            index = 0
            for i in file_names: 
                file_name = file_names[index] + '.csv'
                index += 1
                with open(file_name, newline='') as f:
                    reader = csv.reader(f)
                    next(reader, None)  # Skip the header.
                    # Unpack the row directly in the head of the for loop.           
                    if file_name == 'electric_cars.csv':
                        for Make, Colour, Mileage, Engine_size, Status, Reg_number, Fuel_cells, Car_type in reader:
                            # Now create the car instance and append it to the list.
                            car = ElectricCar()
                            car.setMake(Make)
                            car.setColour(Colour)
                            car.setMileage(Mileage)
                            car.setEngineSize(Engine_size)
                            car.setStatus(Status)
                            car.setRegNumber(Reg_number)
                            car.setNumberFuelCells(Fuel_cells)
                            car.setCarType(Car_type)
                            self.electric_cars.append(car)
                            
                    elif file_name in ('petrol_cars.csv', 'diesel_cars.csv'):
                        for Make, Colour, Mileage, Engine_size, Status, Reg_number, Cylinders, Car_type in reader:
                            if file_name == 'petrol_cars.csv':
                                car = PetrolCar()
                                
                            elif file_name == 'diesel_cars.csv':
                                car = DieselCar()
                            
                            car.setMake(Make)
                            car.setColour(Colour)
                            car.setMileage(Mileage)
                            car.setEngineSize(Engine_size)
                            car.setStatus(Status)
                            car.setRegNumber(Reg_number)
                            car.setNumberCylinders(Cylinders)
                            car.setCarType(Car_type)
                            
                            if file_name == 'petrol_cars.csv':
                                self.petrol_cars.append(car)
                                
                            elif file_name == 'diesel_cars.csv':
                                self.diesel_cars.append(car)
                    
                    elif file_name in ('hybrid_cars.csv'):
                        for Make, Colour, Mileage, Engine_size, Status, Reg_number, Fuel_cells, Cylinders, Car_type in reader:
                            car = HybridCar()
                            car.setMake(Make)
                            car.setColour(Colour)
                            car.setMileage(Mileage)
                            car.setEngineSize(Engine_size)
                            car.setStatus(Status)
                            car.setRegNumber(Reg_number)
                            car.setNumberFuelCells(Fuel_cells)
                            car.setNumberCylinders(Cylinders)
                            car.setCarType(Car_type)
                            self.hybrid_cars.append(car)
                            
    def main():
        dealership = Dealership()
        answer = input('\nDo you want to start from scratch "1", or load previously saved data "2"? ')                    
        if answer == '1':
            dealership.create_current_stock()
            dealership.save_original_data()
        
        else:
            dealership.load_data()
            
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
            
            elif answer == 'b':
                status = 'in stock'
                car_type = input('\nWhat type would you like to return? p/e/d/h ')
                car_list = dealership.chose_car_list(car_type)
                dealership.display_data(car_list)
                index = eval(input('\nEnter the index of the car you want to return: '))
                dealership.change_status(car_list, status, index)
                mileage = eval(input('\nWhat is the mileage of the car on return? '))
                dealership.change_mileage(car_list, mileage, index) 
            
            answer = input('\nWould you like to save changes made? y/n ')
            if answer == 'y':
                data = dealership.get_data(car_list)
                data = [item[1:] for item in data]
                file_name = car_list[0].getCarType() + '_cars.csv'
                with open(file_name, "w", newline="",  encoding='utf-8') as f:
                    writer = csv.writer(f)
                    writer.writerows(data)
                    f.close()
            
            proceed = input('\nWould you like to continue y/n? ')
                           
if __name__ == '__main__':
   Dealership.main()