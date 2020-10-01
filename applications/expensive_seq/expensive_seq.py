# Your code here

     
     
    
cache = {}
def expensive_seq(x, y, z):
    if x <= 0:
        if (y,z) in cache:
            num = cache[(y,z)]
        else:
            num = y + z
            cache[(y,z)] = num
    
    if x >  0: 
        if (x,y,z) in cache:
            num = cache[(x,y,z)]
        else:
            num = (expensive_seq(x-1,y+1,z) 
                + expensive_seq(x-2,y+2,z*2) + expensive_seq(x-3,y+3,z*3))
            cache[(x,y,z)] = num
    return num
if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

print(expensive_seq(150, 400, 800))
