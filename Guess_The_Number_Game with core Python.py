import random as r

#generate the lucky number
l = r.randint(1,6)

#prompt and accept the guessed number from the user
a = int(input("Guess the number from 1 to 6(You have 3 lives)"))

#compare
if(l==a):
    print("You Won!")

else:
    print("You lost! Try again")
    a = int(input("Guess the number from 1 to 6 again.(You have 2 more lives)"))

    #compare
    if(l==a):
        print("You Won!")

    else:
        print("You lost! Try again")
        a = int(input("Guess the number from 1 to 6 again.(This is your last life)"))

        #compare
        if(l==a):
            print("You Won!")

        else:
            print("You lost! The lucky number is",l)
