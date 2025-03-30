a=10 
b=5

c= a+b
print("Addition of",a,"+",b,":",c)

c=a-b
print("Subtraction of",a,"-",b,":",c)

c=a*b
print("Multiplication of",a,"*",b,":",c)

c=a/b
print("Addition of",a,"/",b,":",c)

c=a%b
print("Mod of",a,"%",b,":",c)

c=a**b # Exponent value, also known as the power, indicates how many times a base number is multiplied by itself. For example, in 2**3 -> 3 is the exponent, meaning 2 is multiplied by itself three times (2 x 2 x 2 = 8)
print("Exponent of",a,"**",b,":",c)

c=a//b #The Floor value of 11 divided by 4 (11//4) is 2. 
# Here's why:
# Division: 11 divided by 4 is 2.75. 
# Floor Function: The floor function rounds a number down to the nearest integer. 
# Result: Rounding 2.75 down to the nearest integer gives you 2
print("Floor value of",a,"//",b,":",c) 

a=-11; b=9
c=a//b
print("Floor value of one negative value is always negative: ",a,"//",b,":",c)