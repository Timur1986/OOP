class airplane:
    def __init__ (self, make, model, year, max_speed, odometer):
        self.make = make
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.odometer = odometer
        self.is_flying = False
    
    def take_off (self):
        self.is_flying = True
        
    def land (self):
        self.is_flying = False
        
    def fly (self, km):
        self.odometer = self.odometer + km
        print('Полет проходит в штатном режиме. За бортом - 20 градусов')
        
air_plane = airplane ('Airbus', 'A320', 2015, '2000 km', 150000)
print(f'{air_plane.make} {air_plane.model} {air_plane.year} {air_plane.max_speed}')
air_plane.take_off()
print(air_plane.is_flying)
air_plane.land()
print(air_plane.is_flying)
air_plane.fly(30000)
print(air_plane.odometer)

