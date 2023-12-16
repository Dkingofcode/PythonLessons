class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    
    def moves(self):
        print('Moves along..')
        
    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}.")    
        
my_car = Vehicle('Tesla', 'Model 3')


print(my_car.make)
print(my_car.model)
my_car.moves()        
my_car.get_make_model()

your_car = Vehicle('Cadillac', 'Escalade')
your_car.moves()
your_car.get_make_model()

class Airplane(Vehicle):
    def moves(self):
        print('Rumbles along..')
    
class Truck(Vehicle):
    def moves(self):
        print('Rumbles along..')    
        
        
class GolfCart(Vehicle):
    pass

cesna = Airplane('Cesna', 'Skyhawk', )
mack = Truck('Mackrewer', 'Goretrer')
golfwagon  = GolfCart('volkswagen', 'renault')
            
print('\n\n')

for v in (my_car, your_car, cesna, mack, golfwagon):
    v.get_make_model()
    v.moves()
            

