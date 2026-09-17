#If else conditional statements
a=int(input("Enter your age:"))
print("Your age is=", a)
#Conditional Operators: 
""">, <, >=, <=, ==, !=
print(a==18)
print(a!=18)
print(a>18)
print(a<18)
print(a<=18)"""
if(a>=18):
    print("You can drive")
    print("Yes")
else:
    print("You can't drive")
    print("No")
#If, elif and else.
"""Here if and else can be write only once but if we want many conditions to work then we can use elif,
 since it can be repeated multiple times with changing the condition."""
ApplePrice= 200
budget=int(input("Enter your budget:"))
#Method 1:
if(budget>ApplePrice):
    print("You can buy the apple.")
else:
    print("Sorry, You don't have the budget to buy apples.")
#Method 2:
if(budget-ApplePrice>300):
    print("You can buy 1kg apple.")
elif(budget-ApplePrice>=50):
    print("Now you have absolute chance to buy the apples.")
elif(budget-ApplePrice>=150):
    print("Buying Apples.")
else:
    print("You can't buy the apple.")
#Nested if statements:
"""We can run if,elif and else statements again inside the if elif statement:"""
num=int(input("Enter your num:"))
if(num==12):
    print("The value is 12.")
elif(num>12):
    print("The value is more then 12.")
    if(num<=12):
        print("The value is equal or lesser then 12.")
    elif(num>=12):
        print("The value is equal or greater then 12.")
    else:
        print("The value is not 12.")
else:
    print("The number is less then 12.")