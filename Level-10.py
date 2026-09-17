#String Methods
a="!!!Manish!! !! Manish" #Strings are immutable
print(len(a))
print(a.lower())
print(a.upper())
print(a.rstrip("!"))#It only strip or remove the things are main word like Manish
print(a.replace("Manish", "Harry"))#It replace all the first character with the second character.
print(a.split(" "))#It split the string according to the condition like space between them
blogheading="introduction of capitAlize"
print(blogheading.capitalize())
str1="Welcome to the Console!!!"
print(len(str1))
print(len(str1.center(50)))#It align the string to the center by adding 25 spaces before the start of the string. 
print(str1.center(50))
print(str1.center(50, "."))
print(a.count("Manish"))
print(str1.endswith("!!!"))#It helps to show if the string end with the following character. If yes then it will print True or else false.
print(str1.endswith("to", 4, 10))#Here i am asking them if the word "to" end with in the character slicing of 4 to 10 or not.
print(str1.startswith("!!!"))#It helps to show if the string starts with the following character. If yes then it will print True or else false.
print(str1.find("is"))
print(str1.find("to"))
#print(str1.index("is"))#Index is used if we are sure the follwing word is there in the string and you want it.
print(str1.isalnum())#It shows if the following string is alphanumeric or not? It should not contain any space or any other character.
str2="Welcometotheconsole47"
str3="Welcometotheconsole"
str4="9594533992"
print(str2.isalnum())
print(str3.isalpha())#Only alphabeths should be there.
print(str3.islower())#Only lower case then True
print(str3.isupper())#Only upper case then True
print(str4.isnumeric())#Only numbers should be there.
print(str2.isprintable())#If printable or not. Like\n is not printable.
str1="       "#Using space
print(str1.isspace())
str2="      "#Using tab
print(str2.isspace())
str1="World Health Organisation"
print(str1.istitle())#If the first letter of each word of the string is in upper case or not.
print(str1.swapcase())#Swap the lower case character to upper case and vice versa.
str2="Hello guys, how are you?"
print(str2.title())#Uppercase all the first letter of the words in the given string.