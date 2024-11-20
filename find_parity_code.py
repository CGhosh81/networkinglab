
def getParity(n):
    binary_str = bin(n)[2:]
    count=binary_str.count('1')
    if(count%2)==0:
        return "Even"
    else:
        return "Odd"
n=int(input("Initialize n:"))
print(f"This number is {getParity(n)} Parity")  
