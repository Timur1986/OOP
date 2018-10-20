class car:
    def __init__(self,owner, model, make, year):
        self.owner = owner
        self.model = model
        self.make = make
        self.year = year
        self.odometer = 0
        self.is_going = False
    def go(self, km):
        self.odometer = self.odometer + km
        self.is_going = True
        print('Woooon')
    def stop(self):
        self.is_going = False
   
new_car = car('Timur', 'X6', 'BMW', 2012)
print(f'{new_car.owner} {new_car.model}')
print(new_car.odometer, new_car.is_going)
new_car.go(250)
print(new_car.odometer, new_car.is_going)
new_car.stop()
print(new_car.is_going)

