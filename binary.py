import sys

a = int(raw_input("enter a number ")) 
a = bin(a)[2:]
a = a[::-1]
print int(a,2)


