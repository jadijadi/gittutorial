import random

print("Machine suppose a Number between 1 to 10 ....")
machine_assumption = random.randint(1,10)
print("Now it is your turn to guess:")
print("You will have 5 chance to Win the game")

def run_game():
    tmp = 5
    while (tmp > 0):
        try:     
            user_guess = int(input("> Chance Number {}:  ".format(6-tmp)))
        except ValueError:
            print("Please enter valid data type:: Just numbers")
        else:
            if user_guess == machine_assumption:
                print("Congras! you Win")
                break
            elif user_guess < machine_assumption:
                print("Hint: Bigger")
                tmp -= 1
                print("Continue to Try :)")
            elif user_guess > machine_assumption:
                print("Hint: Smaller")
                tmp -= 1
                print("Continue to Try :)")
    else:
        print("Unfortunantly you Loose, have more lucky in next time ;)")
        print("The Assumed number was {}!".format(machine_assumption))
        if input("Do you want to play again? [Y/N] ").upper() == 'Y':
            run_game() 
        else:
            None

run_game()