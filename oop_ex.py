class patient:
    def __init__(self):
        self.name = ''
        self.age = ''
        self.year = ''
        self.diagnosis = ''
        self.health = True

    def unit (self, owner):
        self.name = self.name + owner
        print ('Hello, dear patient!')

    def doctor (self, x, y):
        self.age = self.age + x
        self.year = self.year + y
        print('Pleas ask, your age and year, ' + self.name)

    def status (self, ill):
        self.diagnosis = self.diagnosis + ill
        print ('I have your result test, and you ill:')

    def check (self):
        self.health = False
        print ('You should take tablet!')

person = patient()
person.unit ('Anton')
print (person.name)
person.doctor ('40', '1978')
print (person.age, person.year)
person.status ('itchy feet')
print (person.diagnosis)
person.check ()
print(person.health)
