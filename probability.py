print("This program will determine the porbability of drawing a certain coloured marble from a bag.")#Extra information for the user.
green = int(input("How many green marbles are in the bag? "))#The user inputs how many of each coloured marble are in the bag.
blue = int(input("How many blue marbles are in the bag? "))
red = int(input("How many red marbles are in the bag? "))    
purple = int(input("How many purple marbles are in the bag? "))
total = 0#Defining variables as integers.
prob1 = 0
prob3 = 0
prob4 = 0
total += blue + red + purple + green
prob1 = (green/total)*100#Probability calculations.
prob2 = (blue/total)*100
prob3 = (red/total)*100
prob4 = (purple/total)*100

print("Would you like to know the probability of picking a...")
print ("1. a green marble")
print ("2. a blue marble")
print ("3. a red marble")
print ("4. a purple marble")

colourselect = int(input("Which colour would you like to know the probability of picking? Specify by using the associating number. (1 = green, 2 = blue etc.)"))

if colourselect == 1:#Using if statements as a menu selection tool.
    print("The probability of choosing a green marble is ", prob1, "percent.")#This function prints your results.
elif colourselect == 2:
    print("The probability of choosing a blue marble is ", prob2, "percent.")
elif colourselect == 3:
    print("The probability of choosing a red marble is ", prob3, "percent.")
elif colourselect == 4:
    print("The probability of choosing a purple marble is ", prob4, "percent.")
else:
    print("Please input the number associating to the colour you want to choose next time.")#This is an error message explaining where you went wrong in the data input process.
    