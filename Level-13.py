#For Loops
name= "Manish"
for i in name:
    print(i)
    print(i, end=", ")
    if(i=="s"):
        print("This is something special.")
colors = ["Red", "Orange", "White", "Black", "Yellow"]
for color in colors:
    print(color)
    for i in color:
        print(i)
for k in range(5):
    print(k)#It will start from 0 to 4
    print(k+1)#It will start from 1 to 4
for k in range(1,9):#It will start from 1 to 8 only it will not include the last number which was 9.
    print(k)
for k in range(1,10,2): 
    print(k)
"""Here the range will be 1 to 9 but it will show the 2nd digit since the 3rd number is 2.
So here x and y is the range where y is y-1 and the z is the gap."""