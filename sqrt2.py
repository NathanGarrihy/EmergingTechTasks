def sqrt(x):
    """
    A function to calculate the square root of a number x.
    """
    # Initial guess for the square root (z)
    z = x / 2
    # Loop until accuracy is sufficiant
    while abs(x - (z * z)) > 0.0000001:
        # Calculate a better guess for square root
        z -= (z*z - x) / (2*z)
    # Return the approx square root of x
    return z

# Print square root of 2
print(sqrt(2))