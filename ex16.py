from sys import argv
script,filename = argv

print("We're going to erase %r." % filename)
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")
input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")

print("Now i'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")
print("Now i'm going to write these to the file")

target.write("%s\n%s\n%s\n" % (line1, line2, line3))


print("And finally, we close it.")
target.close()

txt = input("Type the filename again: ")
daFile = open(txt)
print(daFile.read())
daFile.close()