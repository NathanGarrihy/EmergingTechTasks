def Sqrt2():
# Move numbers from left to right
    a = 2 *(10**(200))
    b = 0
    # set c to a googol(10^100)
    # googol is 10 to the power of 100 (100 decimal places)
    googol = 1 *(10**100)
    
    # Loop until accuracy is sufficiant
    while b != googol:
        # Set b to googol
        b = googol
        # Get the floor division + Bit shift num 1 place to the right
        googol = (b+(a//b)) >> 1
        # Keeps running until b == googol
    # Returns numbers to the right of decimal place
    return googol-(10**100)

# Print square root of 2
print("1.%d"%Sqrt2())