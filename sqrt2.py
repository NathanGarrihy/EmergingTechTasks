SQRTNUM = 2
def Sqrt2():
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
    
# Print square root of 2
print(Sqrt2())

