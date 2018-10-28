# Task_1
import datetime

year = int(input('Укажите год своего рождения: '))
month = int(input('Укажите месяц своего рождения: '))
day = int(input('Укажите день своего рождения: '))

t1 = datetime.date(2018, 12, 31)
t2 = datetime.date(year, month, day)
t3 = (t1 - t2)//365
print('На 31/12/2018 Вам исполнится '+ str(t3))

# Task_2 
# Part_1

class Money:    
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency
    
    def __repr__(self):
        return f'It\'s money {self.amount} {self.currency}'
    
    def __str__(self):
        return f'On the note of {self.amount} {self.currency} depicted is Hiram Ulysses Grant'
    
    def __add__(self, currency_new):
        return self.currency + ', ' + currency_new.currency
    
    def __sub__(self, note_new):
        return self.amount - (note_new.amount//69)          

if __name__ == '__main__':
    
    note = Money(50, 'Dollar')
    print(note)
    note2 = Money(500, 'KGS')
    print(note + note2)
    print(note - note2)

# Part_2

class Money2:    
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency
        
    def __lt__(self, amount_new):
        res = self.amount < amount_new.amount
        return res
    
    def __le__(self, amount_new):
        res = self.amount <= amount_new.amount
        return res
    
    def __ne__(self, amount_new):
        res = self.amount != amount_new.amount
        return res
    
    def __gt__(self, amount_new):
        res  = self.amount > amount_new.amount
        return res
    
    def __ge__(self, amount_new):
        res = self.amount >= amount_new.amount
        return res

if __name__ == '__main__': 
    
    note1 = Money2(10, 'Dollar')
    note2 = Money2(50, 'Dollar')
    note3 = Money2(100, 'Dollar')
    note4 = Money2(50, 'Dollar')
    print(note1 < note2)
    print(note2 > note3)
    print(note1 < note3)
    print(note2 >= note4)
    print(note3 >= note4)
    print(note2 != note4)
    print(note4 != note1)
    print(note3 > note1)
    print(note1 > note4)
    print(note2 >= note4)
    print(note3 >= note1)
