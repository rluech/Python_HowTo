
import math

s = [1,6,8]

[x+1 for x in s]

def fun(a, b):
    x = a ** b
    y = math.sqrt(x)
    z = x % b
    z += b
    return(z)

fun(3, 4)


