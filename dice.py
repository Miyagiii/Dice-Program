#made by TheSpaceCowboy
#date: 02/07/17
#imports
import random as rNumber#Imports the random python module

#main code

def interface():#Handles I/O for the program
    print("Welcome to my dice simulator.")
    print("How many sides on the dice would you like?")
    
    try:
        
        sides = int(input("> "))#Gets how many sides the user wants the dice to be
        
        if( sides <= 0):#Defencive programming for if the users input is less than or equal 0

            #Displays error message and restarts the program
            print("Please pick a number bigger than 0.\n\n")
            main()
            
        else:
            
            pass
        
    except ValueError:#Handles a value error if one occurs
        #Prints error message and resets program
        print("Please input a whole number, thank you.\n\n")
        main()
        
    print("Rolling the dice!")
    dice = diceRoll(sides)#Calls the diceRoll method
    print(dice)#Prints the output of the diceRoll method

    choice = input("Would you like to roll again? Y/N")#Asks the user if they want to play again

    if (choice.lower() == "y" or choice.lower() == "yes"):# if the answer is yes restart
        interface()
        
    else:#or it exits
        
        exit()
def diceRoll(sides):#Rolls the dice, requires the number of sides to run.
    dice = rNumber.randint(1,sides)#Picks a random number between 1 and the specified number
    return dice#Returns the number

interface()
