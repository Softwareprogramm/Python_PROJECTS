welcome = """
───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───
───█▒▒░░░░░░░░░▒▒█───
────█░░█░░░░░█░░█────
─▄▄──█░░░▀█▀░░░█──▄▄─
█░░█─▀▄░░░░░░░▄▀─█░░█
█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█
█░░║║║╠─║─║─║║║║║╠─░░█
█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█
"""

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]


def encrypt():
    encrypt_message = ""
    message = input("enter your message: ").lower()
    direction = input("'encode' or 'decode': ").lower()

    while True:
        shift = input("enter a number: ")
        if shift.isdigit():
            shift = int(shift)
            break
        else:
            print("Please a number.")

    for letter in message:
        if letter in alphabet:
            position = alphabet.index(letter)
            if direction == "encode":
                new_position = position + shift
                encrypt_message += alphabet[new_position]
            else:
                new_position = position - shift
                encrypt_message += alphabet[new_position]
        else:
            continue
    print(f"{encrypt_message}")


#encrypt()

# Define a new funtion that keeps running until user enters "stop"
print(welcome)
def encrypt_loop():
    loop = True
    prompt = "Welcome to the ENCRYPTER.\n"
    prompt += "Enter 'y' to continue and 'n' to quit\n➜ "
    while loop:
        user = input(prompt).lower()
        if user == "y":
            encrypt()
        else:
            print("Thanks for using The Encrypter, see you next time..")
            loop = False

encrypt_loop()