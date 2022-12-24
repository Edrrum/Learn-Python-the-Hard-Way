from random import randint
def cheese_and_crackers(cheese_count, boxes_of_crackers): #defines the function cheese_and_crackers with the cheese_count and boxes_of_crackers as arguments
    print("You have %d cheeses!" % cheese_count) #prints a string that gives us the number of cheese
    print("You have %d boxes of crackers" % boxes_of_crackers) #prints a string that gives us the number of crackers
    print("Man that's enough for a party!") #just prints a string 
    print("Get a blanket. \n")#just prints a string and makes a new line

print("We can just give the function numbers directly") #prints a string
cheese_and_crackers(20,30) #runs the function cheese_and crackers with 20 as the cheese_count arguments and 30 as the boxes_of crackers argument

print("OR, we can use variables from our script") #prints a string
amount_of_cheese = 10 #creates a variable that stores an int 10
amount_of_crackers = 50#creates a variable that stores an int 10

#runs the function cheese_and crackers with the variableas amount_of cheese as the cheese_count argument and amount_of_crackers as the boxes_of crackers argument
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:") # prints a string
cheese_and_crackers(10+20, 5+6) #runs the function cheese_and crackers with 20+10 as the cheese_count arguments and 5+6 as the boxes_of crackers argument

print("And we can combine the two, variables and math:") # prints a string
#runs the function cheese_and_crackers with amount_of_cheese + 100 as the cheese_count arguments and amount_of_crackers + 1000 as the boxes_of crackers argument
cheese_and_crackers(amount_of_cheese+ 100, amount_of_crackers + 1000) 

def pastaAndSauce(pastaAmount, sauceAmount):
    print("you have %d grams of pasta" % pastaAmount)
    print("you have %d liters of sauce" % sauceAmount)
    print("That's a ton of sauce or pasta i don't know xDD")

pastaAndSauce(1000, 1)
Pasta_count = 500
Sauce_count = 0.5

pastaAndSauce(Pasta_count, Sauce_count)
pastaAndSauce(50 + 10, 0.1 + 0.2)
pastaAndSauce(Pasta_count+ 10, Sauce_count + 5)
Pasta = int(input("Grams of pasta: "))
Sauce = int(input("Liters of sauce: "))
pastaAndSauce(Pasta_count + Pasta, Sauce_count + Sauce)
pastaAndSauce(Pasta + 10, Sauce + 1)
pastaAndSauce(Pasta * 2, Sauce * 2)
pastaAndSauce(Pasta_count * 2, Sauce_count * 2)
pastaAndSauce(randint(1, 10000), randint(1, 100))
pastaAndSauce(randint(1, 100) + 100, randint(1, 10) + 50)
pastaAndSauce(randint(1,100) + Pasta, randint(1,10) + Sauce)
