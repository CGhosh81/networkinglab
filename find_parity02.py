def getParity( n ):
    parity = 0
    while n:
        parity = ~parity
        n = n & (n - 1)
    return parity
 

n=int(input("Initialize n:"))
print (( "Odd parity" if getParity(n) else "Even parity"))