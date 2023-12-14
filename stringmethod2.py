
str1 = "WelcomeToTheConsole"
print(str1.isalnum())    #method returns True only if the entire string only consists of A-Z, a-z, 0-9

str1 = "Welcome"
print(str1.isalpha())   #method returns True only if the entire string only consists of A-Z, a-z.

str1 = "hello world"
print(str1.islower())  #method returns True if all the characters in the string are lower case, else it returns False.

str1 = "World Health Organization" 
print(str1.istitle())   #istitile() returns True only if the first letter of each word of the string is capitalized, else it returns Fa

str1 = "WORLD HEALTH ORGANIZATION" 
print(str1.isupper())  #method returns True if all the characters in the string are upper case, else it returns False.