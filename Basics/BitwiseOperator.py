a = 10
b = 4

# bin(c): This function converts the integer c to its binary string representation (e.g., '0b11110101'). 
c = a&b
print("Result of AND:",c, "Binary:", bin(c) )

c = a|b
print("Result of OR: ",c, "Binary:", bin(c) )

c = a^b
print("Result of XOR: ",c, "Binary:", bin(c) )

c= ~a # just Reverse the bits
print("Result of COMPLEMENT: ",c, "Binary:", bin(c) )

c=a<<b # 10*2^4 =10*16=160 
print("Result of LEFT SHIFT: ",c, "Binary:", bin(c) )

c=a>>b # 10÷2^4 =10÷16=0 ->Since 10 is less than 16, it shifts out completely, resulting in 0
print("Result of RIGHT SHIFT: ",c, "Binary:", bin(c) )

d=20
print("a", bin(a), "b:", bin(b), "d:", bin(d))
