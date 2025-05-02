import random

def get_funny_motivational_quote():
    quotes = [
        "Keep going! You’re halfway to almost giving up!",
        "Don't worry if plan A fails, there are 25 more letters in the alphabet!",
        "If at first you don’t succeed, skydiving is not for you.",
        "Dream big! Unless your dreams are silly, then just dream moderately.",
        "The elevator to success is out of order. You'll have to use the stairs, one step at a time.",
        "You miss 100% of the naps you don’t take.",
        "If you think nobody cares if you’re alive, try missing a couple of car payments.",
        "Be yourself; everyone else is already taken, and probably not as funny.",
        "I find television very educational. Every time someone turns it on, I go read a book.",
        "People say nothing is impossible, but I do nothing every day.",
    ]
    return random.choice(quotes)

if __name__ == "__main__":
    print("Here's your funny motivational quote for the day:\n")
    print(get_funny_motivational_quote())
