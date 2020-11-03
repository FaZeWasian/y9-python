Decklist = [] # Here I have named the list.
print("We will make your deck list.") # Giving the user extra information.
for x in range(0, 10, 1):# This means the program will loop 10 times and the user will input 10 cards, in my actual program you would input 60.
    cardinput = str(input("Input Card Name... "))#This is where the user inputs the card name. Because it is tect the input has been defined as a string.
    Decklist.append(cardinput)#This line appends or puts the input into the list.
print("Your Deck List is...", Decklist)#This function prints the list on the screen.
    