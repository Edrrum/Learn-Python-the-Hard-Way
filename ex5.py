name = 'Zed A. Shaw'
age = 35 #not a lie 
height = 74 #inches
weight = 180 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print("let's talk about %s." % name)
print("He's %d centimeters tall." % (height * 2.54))
print("He's %d kilograms heavy." % (weight * 0.45359237))
print("Actually that's not too heavy")
print("He's got %s eyes and %s hair." %(eyes, hair))
print("His teeth are usually %s depending on the coffee." % teeth)

# this line is tricky, try to get it exactly right
print("If i add %d, %d and %d I get %d." %(age, height, weight, age + height + weight))