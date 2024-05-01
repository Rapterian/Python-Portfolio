import random

def toInt(number_string):
    if str(number_string).isdigit()==False:

        while str(number_string).isdigit()==False:
            number_string=input("Please enter a number:\n")

    number=int(number_string)    
    
    return number


number_of_guesses=1

print("Let's play a guessing game!\n\
I will choose a number between 2 numbers you give me,\n\
then you guess which number I chose.")

bottom_of_range=toInt(input("Give me the lowest number I can choose:\n"))
top_of_range=toInt(input("Give me the highest number I can choose:\n"))


random_number=random.randint(bottom_of_range,top_of_range)

guess=toInt(input("Okey, guess the number I chose,\n\
I will tell you if the number is higher or lower than your guess:\n"))


while guess != random_number:

    number_of_guesses+=1

    if(guess>random_number):
        guess=toInt(input("That was incorrect :(\n\
Try guessing lower:"))
    else:
        guess=toInt(input("That was incorrect :(\n\
Try guessing higher:"))

possibilities=top_of_range-bottom_of_range+1

print("That is correct :)\n\
It took you ",number_of_guesses," tries and there were ",possibilities," possible answers!")

