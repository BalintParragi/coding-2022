date = "2022-01-17"

def compute_tomorrow(date):
    year = date[:4]
    month = date[5:7]
    day = int(date[-2:])
    return year + '-' + month +'-'+ str(day+1)


#_problem: cant use outside things defined inside the function
print("Next class is on",compute_tomorrow(date))

#exit(): 
def add_two(number):
    return number + 2
    
# end of function

def greet():
    print("Hello world")
    print("Second line")

#if I press print(greet())--> there will be a last line: none

def non_returning_computation(number):
    (number + 7)*13



print(non_returning_computation(21)) #again, none: we did not use return

def returning_computation(number):
    return (number + 7)*13
    
def feet_to_meter(feet):
    return feet*0.3048 #pr print(feet*0.3048)






