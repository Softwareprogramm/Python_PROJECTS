import random
prompt = "Welcome to the HARDEST number guessing game.\n"
prompt += "Press '1' to continue or '0' to end\n➜ "
secret_number = random.randint(1, 1000)


def guess():
    count = 0
    while True:
        #print(secret_number)
        while True:
            user = input("Guess the number to win: ")
            if user.isdigit():
                user = int(user)
                break
            else:
                print("You must enter a number!")
        if user != secret_number:
            count += 1
            if user > secret_number:
                print("Your number is greater than the secret number.")
            elif user < secret_number:
                print("Your number is less than the secret number.")
        else:
            print(f"Well done, you tried {count} times")
            break

#guess()

def loop():
    while True:
        try:
            start = int(input(prompt))
            if start == 1:
                guess()
            elif start == 0:
                print("Thanks for playing, Goodbye!!")
                break
            else:
                print("Please enter the numbers you see on your screen.")
        except ValueError:
            print("Unknown value, Try again.")

loop()