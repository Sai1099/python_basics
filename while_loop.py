i = 1
while(i<=40):
    ##print(i)
    i+=1
    print(i)

secret_word = "zoo"
guess =""
guess_count=0
guess_limit=3
out_of_guesses = False

##Mistake did try to use the guess after the input  function so don't use the print function MMFU
while (guess != secret_word and not(out_of_guesses)):
    if(guess_count < guess_limit):
        guess = input("Enter the guess word:")
        guess_count +=1
    else:
      out_of_guesses = True

if(out_of_guesses):
    print("Out of Guesses, You Lose!")
else:
 print("You win")