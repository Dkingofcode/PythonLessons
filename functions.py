def hello():
    print("Hello world!")
    
hello()


def sum(num1=0, num2=0):
    if(type(num1) is not int or type(num2) is not int):
        return 0
    return num1 + num2
    
total = sum(7, 3)
print(total)
sum(1, 7)
sum(100, 3)

        
def multiple_items(*args):    
    print(args)
    print(type(args))
    
    
multiple_items("Dave", "John", "Sara")            

def mult_name_items(**kwargs):
    print(kwargs)
    print(type(kwargs))
    
mult_name_items(first = "Dave",  last = "Gray")    







