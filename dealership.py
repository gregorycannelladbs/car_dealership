from car import Car, ElectricCar, PetrolCar, DieselCar, HybridCar

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
        for i in range(6):
           self.electric_cars.append(ElectricCar())
        for i in range(20):
           self.petrol_cars.append(PetrolCar())
        for i in range(10):
           self.diesel_cars.append(DieselCar())
        for i in range(4):
           self.hybrid_cars.append(HybridCar())

    def stock_count(self):
        print('petrol cars in stock ' + str(len(self.petrol_cars)))
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

def main():
    dealership = Dealership()
    dealership.create_current_stock()
    proceed = 'y'
    while proceed == 'y':
        dealership.process_rental()
        proceed = input('continue? y/n')

if __name__ == '__main__':
    main()