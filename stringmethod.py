#Strings are immutable
str='kimtaehyung kimtaehyung  '
str1='jungkook !!,jimin!!'

print(str.upper())  #method convert the string into upper case 
print(str.lower())  #method convert the string into upper case 
print(str.count('kimtaehyung'))   #returns the number of times the given value has occurred within the given string.

str1='jungkook !!,jimin!!'
print(str1.rstrip('!'))   #removes any trailing characters
print(str1.split(" "))    #splits the given string at the specified instance and returns the separated strings as list items.
print(str1.replace("jungkook","kim namjoon"))   #replaces all occurences of a string with another string

blogheading='introduction to bts '
print(blogheading.capitalize())   #method turns only the first character of the string to uppercase and the rest other of the string are turned to lowercase

str2="Wellcome to bts!!"
print(len(str2))
print(str2.center(52))   #aligns the string to the center as per the parameters given by the user.
print(str2.endswith("!!"))   #checks if the string ends with a given value.

str2="he's ame is dan. he is an honest man."
print(str2.find("is"))   #searches for the first occurrence of the given value and returns the index where it is present.


