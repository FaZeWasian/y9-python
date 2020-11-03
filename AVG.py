print("We will find your academic average.")#Giving extra information.
totalsum = 0.0#Setting variables to 0 and defining them as int and float values.
counter = 0
while counter <= 4:#While loop has been established
        gradeinput = float(input("Input Grade... "))#Where the user will input their grades.
        if 0 >= gradeinput:#A check to make sure the data that the user input can be used for this calculation.
            print("Your number must be positive and greater then 0.")
            continue#Resets the user back to the beginning of the while loop.
        elif 100 < gradeinput:#A check to make sure the data that the user input can be used for this calculation.
            print("Your number must be less than or equal to 100.")
            continue
        else:
            totalsum += gradeinput#This adds the value of gradeinput to the totalsum.
            counter += 1#Adds one to counter which brings us closer to the end of the while loop.
avg = totalsum/5#This line calculates the average of the grades.
print("Your Average is... ", avg )#This line prints the results.

    
    
    
 

