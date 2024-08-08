# Write a Python program that encrypts text given by the user. The program should 
#ask the user for a plain text sentence and print the encrypted text. The text 
#should be encrypted using a caesar cipher with a right shift of 5.

#Here is an example execution of the program:

#Please enter a senctence: python is fun!
#The encrypted sentence is: udymts nx kzs!


#shift operator
#chr() function
#ord() function



user_input = input("Please enter a sentence.")

encrypted_message = ""

shift = 5

for char in user_input:
  encrypted_char = chr((ord(char) - 97 + shift) % 26 + 97)
  encrypted_message += encrypted_char

print(encrypted_message)

