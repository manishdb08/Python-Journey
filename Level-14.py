#While Loops

i=int(input("Enter the value:"))
while(i<=6):
    print(i)
    i=i+1
print("Completed the loop")

# #Condition under the while loop.

i=int(input("Enter the value:"))
print(i)
while(i<=99):
    i=int(input("Enter the value:"))
    print(i)
print("Done with the loop")

#Decrementing the while loop

count=-12
while(count>=5):
    print(count)
    count=count-1
else:
    print("Over")

#Do-while loop
"""This while True will act as do-while loop where they will print statement
   before checking the condition."""
while True:
    password = input("Enter password: ")
    if password == "1234":
        print("Correct!")
        break
    