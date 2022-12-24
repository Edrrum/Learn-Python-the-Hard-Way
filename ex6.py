x = "There are %d types of people." % 10 #Defining x using format string (%d = 10)
binary = "binary" #Defining binary
do_not = "don't" #Defining do_not
y = "Those who know %s and those who %s." % (binary, do_not) #defining y using format string (%s, %s = binary, do_not )

print(x) #prints x
print(y) #prints x 

print("I said: %r" % x) #prints a string using %r to use x inside the string 
print("I also said: '%s'." % y) #prints using %s to use y inside the string
hilarious = False #defines hilarious
joke_evaluation = "Isn't that joke so funny?! %s" #define joke_evaluation with a unused format character inside

print(joke_evaluation % hilarious) # prints joke_evaluation while using hilarious as the format string

w = "This is the left side of..." #defines w
e = 'a string with a right side.' #defines e

print(w + e) #additions w and e to make one string