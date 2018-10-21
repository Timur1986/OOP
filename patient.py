class patient:
    def __init__(self, name, age, born):
        self.name = name
        self.age = age
        self.born = born
        self.health = True # feel good
        self.diagnosis = 0
    
    def ill (self):
        self.health = False # feel bad
        print('You should take medicine')
        
    def status (self, check):
        self.diagnosis = self.diagnosis + check
            
    
new_person = patient('Anton', 38, 1980)
print(f'{new_person.name} {new_person.age} {new_person.born}')
new_person.ill()
print(new_person.health)
new_person.status('Diarrhea')
print(new_person.diagnosis)
