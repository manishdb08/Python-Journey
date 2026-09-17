#Typecasting in Python
# a=10
a="10"
# b=20
b="20"
print("The sum of a and b is:", int(a)+int(b))#Typecasting string to integer
print(type(a))
print(type(b))
print(type(a+b))
"""It is Explicit typecasting because we are explicitly converting the string to integer."""
c=10.9
d=20
print("The sum of c and d is:",c+d)#Typecasting integer to float
print(type(c))
print(type(d))
print(type(c+d))
"""It is Implicit typecasting because we are not explicitly converting the integer to float.
It is automatically converted to float. It is built-in feature of python."""
