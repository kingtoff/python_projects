#parsing; reading through a file named fortune.txt

my_writeup = open( "fortune.txt", "r")

print(my_writeup.read()) #parsing through a whole text
print(my_writeup.readline()) #parsing through the text line by line

print(my_writeup.readlines()) #parsing through the whole text in index or arrays
print(my_writeup.readlines()[1]) #parsing through the text using the index position


my_writeup.close()