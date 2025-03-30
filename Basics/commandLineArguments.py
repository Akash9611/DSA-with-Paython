import sys
print("Argument length: ", len(sys.argv))
print("Argument list: ", str(sys.argv))

x = int(sys.argv[1])
y = int(sys.argv[2])
z=x+y

print("x= ",x, "y=", y, "addition of argv z= ", z)

# Run the following command on Terminal or cmd prompt

# E:\DSA_with_python\basics> python commandLineArguments.py 5 6
# Argument length:  3
# Argument list:  ['commandLineArguments.py', '5', '6']
# x=  5 y= 6 addition of argv z=  11