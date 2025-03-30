a = 10
b = 12

c = a&b
print("Result of AND:",c, "Binary:", bin(c) )

c = a|b
print("Result of OR: ",c, "Binary:", bin(c) )

c = a^b
print("Result of XOR: ",c, "Binary:", bin(c) )

c= ~a
print("Result of COMPLEMENT: ",c, "Binary:", bin(c) )

c=a<<b
print("Result of LEFT SHIFT: ",c, "Binary:", bin(c) )

c=a>>b
print("Result of RIGHT SHIFT: ",c, "Binary:", bin(c) )
