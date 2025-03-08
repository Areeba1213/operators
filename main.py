#                  PYTHON OPERATOR

# 1.Arithmetic Operator
# a.Addition
x=3
y=4
print(x+y)
# b.Subtraction
a=5
b=10
print(b-a)
# c.Multiplication
x=21
y=2
print(x*y)
# d.Division
a=23
b=4
print(a/b)
# e.Modulus
x=20
y=5
print(x%y)
# f.Exponentiation
a=10
b=5
print(a**b)
# g.Floor Division
x=30
y=2
print(x//y)
# ASSAIGNMENT OPERATOR
# a.=
x=10
print(x)
# +=
x = 10
x += 5
print(x)
# -=
x=5
x -=10
print(x)
# *=
x=12
x *=6
print(x)
# /=
x=5
x /=4
print(x)
# %=
x=2
x %=5
print(x)
# //=
x=3
x //=4
print(x)
# **=
x=4
x **=8
print(x)
# &=
x=6
x &=12
print(x)
# |=
x=4
x |=6
print(x)
# ^=
x=5
x ^=15
print(x)
# >>=
x=7
x >>=3
print(x)
# <<=
x=3
x <<=4
print(x)
# :=
print(x :=5)
# Comparision Operator
# == equal
x=3
y=5
print(x ==y)
# != not equal
x=4
b=4
print(x!=b)
# > greater than
x=7
y=5
print(x>y)
# < less then
x=4
y=5
print(x<y)
# >=
x=5
y=3
print(x>=y)
# <=
x=5
y=10
print(x <= y)
# Logical Operators
# and 	Returns True if both statements are true
x=4
print(x > 5 and x < 10)
# or 	Returns True if both statements are true
x=5
print(x > 3 or x < 4)
# not Reverse the result, returns False if the result is true
x=5
print(not(x > 3 and x < 10))
# Identity Opperator 
# Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location
# is 	Returns True if both variables are the same object
x= ["apple" ,"guava"]
y = ["apple" ,"guava"]
z=x
print(x is z)
print(x is y)
print(x == y)
# is not 	Returns True if both variables are not the same object
x= ["apple" ,"guava"]
y = ["apple" ,"guava"]
z=x
print(x is not z)
print(x  is not y)
print(x != y)

# Membership Operators
# in 	Returns True if a sequence with the specified value is present in the objec
x = ["orange","banana"]
print("banana" in x)
# not in  Returns True if a sequence with the specified value is not present in the object
x = ["banana","orange"]
print("banana" not in x)

# Bitwise Operator
# & AND
a = 5      # Binary:  0101
b = 3      # Binary:  0011
result = a & b  
print(result)  # Output: 1  (Binary: 0001)
# | OR
a = 5      # Binary:  0101
b = 3      # Binary:  0011
result = a | b  
print(result)  # Output: 7  (Binary: 0111)
# XOR (^)
a = 5      # Binary:  0101
b = 3      # Binary:  0011
result = a ^ b  
print(result)  # Output: 6  (Binary: 0110)
# NOT (~)
a = 5      # Binary:  0101
result = ~a  
print(result)  # Output: -6  (Binary: 1010 in Two's Complement)
# Left Shift (<<)
a = 5      # Binary:  0101
result = a << 1  
print(result)  # Output: 10  (Binary: 1010)
# Right Shift (>>)
a = 5      # Binary:  0101
result = a >> 1  
print(result)  # Output: 2  (Binary: 0010)










