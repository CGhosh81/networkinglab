def FindIPClass(x):
    s=x.split(".")
    
    
    if(4==len(s)):
        temp=int(s[0])
        if(0>=temp and temp<=127):
          return "A"
        elif(128>=temp and temp<=191):
          return "B"
        elif(192>=temp and temp<=223):
          return "C"
        elif(224>=temp and temp<=239):
          return "D"
        elif(240>=temp and temp<=255):
          return "E"
        else:
          print("This is invalid ip address")
    else:
        print("This is invalid ip address")
   


x=str(input("Enter ip address:"))
print("The ip is",x)
print(f"This Ip address belong to Class {FindIPClass(x)}")