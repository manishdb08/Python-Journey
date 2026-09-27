#Match Case Statement
x=(int(input("Enter the value of x:"))) 
"""x is the variable to match"""
match x:
    case 0:#If x is 0
        print("x is zero")
    case 4:# case with if-else condition
        print("x is 4")
    case _:
        print("x is", int(x),  "which is not 4")