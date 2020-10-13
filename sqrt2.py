SQRTNUM = 2
def guessSqrt2():
    """
    A function to calculate the approx square root of a number x.
    """
    # Initial guess for the square root (z)
    z = SQRTNUM * .5
    # Loop until accuracy is sufficiant
    while abs(SQRTNUM - (z * z)) > 0.000000000000001: # maximum accuracy
        # Calculate a better guess for square root
        z -= (z*z - SQRTNUM) / (SQRTNUM*z)
    # Return the approx square root of x
    # 52 decimal places is max for now
    return "{0:.100f}".format(z)
    
def sqrt2():
    """
    A function that returns the accurate square root of a number to 100 decimal places
    """
    r = SQRTNUM
    x = SQRTNUM
    
    precision = 10 ** (-10)
    
    while abs(x - r * r) > precision:
        r = (r + x / r) / 2
        
    return "{0:.52f}".format(r)
    
    
    
# Print square root of 2
print(guessSqrt2())
print(sqrt2())
