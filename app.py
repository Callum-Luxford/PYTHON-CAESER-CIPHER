# // ------------------------------- Ceaser Cipher ------------------------------

# // Only to encode the letters in this cipher.

# // Improved version:

# // Import the math module.
import math

# // Import logo
from logo import *
print(logo)

# // Welcome Message:
print("Welcome to the Python Caeser Cipher!\n")



# // Create a function called caeser, pass in 'start_text', 'shift_amount' &
# // 'cipher_direction' as the paramaters.
def caeser(start_text, shift_amount, cipher_direction):
    
    # // Create empty string and add to a new variable to store the end value.
    end_text = ""
       
# // Use (if) statement to check if the user typed "decode"
    if cipher_direction == "decode":
        
        # // If decode then 'shift_amount'(shift) multiply by -1
        shift_amount *= -1
                           
    # // Use (for) loop to check each letter(i) in the user entry text.
    for i in start_text:
        
        # // check if (i) Character entered is inside the alphabet, if it is
        # // run the code below.
        if i in alphabet:
            
            # // Get the alphabet list and find the index passing in the letter(i)
            # // from the loop and add to a new variable.
            position = alphabet.index(i)

            # // take the position and add it by the 'shift_amount', assign it to 
            # // new variable.
            new_position = position + shift_amount 

            # // Pass in the 'new_position' into the alphabet list and add it to
            # // the 'end_text' string variable.
            end_text += alphabet[new_position]
            
        # // Otherwise append the characters entered to the end of the 'end_text'.
        # // This can help when a user wants to declare something like 'Meet me
        # // at 5?'. 
        # // It will then add those numbers and symbols to the end of the message.
        else:
            end_text += i
            
    # // Print the text for the user passing in the 'cipher_direction' and
    # // 'end_text' as f string.
    print(f"The text {cipher_direction}d text is: {end_text}")


# // Create a boolean add to a variable and set to True.
should_continue = True

# // Use (while) loop to call the program with included inputs until the user
# // decides to stop using.
while should_continue:
    # // Create list for each letter in the alphabet.
        # // Be sure to copy the alphabet list and add the entire alphabet to the list
        # // again or you will not be able to use letters that start toward the latter
        # // end of the alphabet. Which would throw you an error.
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    # // Create input for user to 'encode' or 'decode'.
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    # // Create input for user to type their message.
    text = input("Type your message:\n").lower()

    # // Create input for user to enter a number of shifts on the cypher.
    shift = int(input("Type the shift number:\n"))

    # // If user enters number greater than the number of letters in alphabet
    # // use the modulus (%) to divide the shift number by 26 and use the remainder
    # // to shift the number entered into something that fits in with the number of 
    # // letters in the alphabet.
    shift = shift % 26

    # // Call the caeser function and set the arguments:
    # // start_text=text (from user)
    # // shit_amount=shift (from user)
    # // cipher_direction=direction / 'encode' | 'decode' (from user)
    caeser(start_text=text, shift_amount=shift, cipher_direction=direction)
    
    # // At the end of the program being run, ask the user if they would like
    # // to run the program again or not and add to a variable.
    result = input("Type 'yes' if you want to run the program again. Otherwise type 'no'.\n")
    
    # // Use (if) statement to check if the result variable == "no" and if so
    # // set the boolean for the program to False to break out of the loop.
    if result == "no":
        should_continue = False
        
        # // Print the message to the user.
        print("Thank you for using the Python Caeser Cipher! Goodbye.")