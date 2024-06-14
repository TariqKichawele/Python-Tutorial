# Closure is a function having access to the scope of its parent function
# after the parent function has returned.

def parent_function(person, coins):

    def play_game():
        nonlocal coins
        coins -= 1

        if coins > 1:
            print("\n " + person + " has " + str(coins) + "coins")
        elif coins == 1:
            print("\n" + person + " has " + str(coins) + "coin left")
        else:
            print("\n" + person + " is out of coins.")
    
    return play_game

topg = parent_function("topg", 5)
topz = parent_function("topz", 3)

topg()
topg()

topz()

topg()