# Your code here
import math
import random

def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v




factors = {}
# for x in range(2,15):
#     for y in range(3,7):
#         v = math.pow(x, y)
#         num = math.factorial(v)
#         num //=(x+y)
#         num %= 982451653
        
#         factors[(x,y)] = num
        
        
        


    


def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    if (x,y) in factors:
        value = factors[(x,y)]
    else: 
        value = slowfun_too_slow(x, y)
        factors[(x,y)] = value
    return value
    


# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
