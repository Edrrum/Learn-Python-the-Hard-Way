formatter = "%r %r %r %r" #defines formatter
print (formatter % (1, 2, 3, 4))#prints formatter using (1,2,3,4) as the string formats
print (formatter % ("one", "two", "three", "four"))#prints formatter using ("one", "two", "three", "four") as the string formats
print(formatter % (True, False, False, True))#prints formatter using(True,False,False,True) as the string formats
print (formatter % (formatter, formatter, formatter, formatter))  #prints formatter using (formatter, formatter, formatter, formatter) as the string formats 
print (formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So i said goodnight"
)) # prints formatter using different strings as the string formats