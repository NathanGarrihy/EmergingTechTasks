def Sqrt2():
    # This constant is not fully required but can be changed
    # in order to find the square root of a different number
    SQRTNUM = 2;
    # googol = 10 to the power of 100
    # a = google value of 2 * googol. This moves
    # numbers to the left side of the decimal place
    a = SQRTNUM *(10**(200))
    b = 0
    googol = 1
    
    # Loop until accuracy is sufficiant
    while googol != b:
        # Set b to googol
        b = googol
        # Get the floor division + Bit shift num 1 place to the right
        # Keeps running until b == googol
        googol = (b+(a//b)) >> 1
    # Returns numbers to the right of decimal place
    finalVal = googol-(10**100)
    return "1.%d"%finalVal
    
# Print square root of 2
print(Sqrt2())