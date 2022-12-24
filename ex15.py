from sys import argv #imports argv from the library sys
script, filename = argv #Empties argv(arguments) in script and filename
txt = open(filename) #opens the file with the filename
print("Here's your file %r:" % filename) #prints out a string with filename as a format string
print(txt.read()) #read the file with filename and prints it's content
print("Type the filename again:") #prints a string to prompt the user to type the filename again
file_again = input("> ") #seeks the user's input for the file's name
txt_again = open(file_again) #opens and empties the files content in the variable
print(txt_again.read()) #prints what's in the file using read()
txt.close()
txt_again.close()