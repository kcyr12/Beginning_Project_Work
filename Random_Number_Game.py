
#Import random package
import random

#Display welcome message and outline rules of game
print("Welcome to Guess the Number Game!")
print("I have selected a random number between 1 and 100.Try and guess it!")

#Create random number
def generate_random_number():
    return random.randint(1,100)

#Define check_guess function
def check_guess(random_num, user_guess):
    if user_guess == random_num:
        return "correct"
    elif user_guess > random_num:
        return "high"
    else: 
        return "low"

 #Define extra_hint function 
def extra_hint(random_num):
    
    hint_type = random.randint(1,3)

    if hint_type == 1:
        if random_num % 2 == 0:
            return "The number is even."
        else:
            return "The number is odd"
    
    elif hint_type == 2:
        if random_num % 5 == 0:
            return "The number is a multiple of 5"
        else:
            return "The number is not a multiple of 5"
    
    else:
        if random_num * random_num > 1000:
            return "The number squared is greater than 1,000"
        else:
            return "The number squared is less than or equal to 1,000"

#Define Main Function
def main():
    random_num = generate_random_number()
    guess_count = 0
    correct_guess = False

    while correct_guess == False:
        user_guess = int(input("Enter your guess"))
        guess_count = guess_count + 1

        result = check_guess(random_num, user_guess)

        if result == "correct":
            print("Correct, you guessed the correct number!")
            correct_guess = True
        elif result == "low":
            print("Incorrect, try a higher number")
        else:
            print("Incorrect, try a lower number")

        if guess_count % 3 == 0 and correct_guess == False:
            print("Hint:", extra_hint(random_num))

    print("It took you", guess_count, "to guess the correct number!")

main()