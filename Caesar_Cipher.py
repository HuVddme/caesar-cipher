import sys
def caesar_cipher (message, shift):

    message - message.upper()

# Create a list of the characters to keep

    keep = set("ABCDEFGHIJKLMNOPORSTUVWXYZ")

# Initialize the encoded message

    encoded_message = ""

# Loop through each character in the message

    for char in message:

# If the character is a letter, encode it

        if char in keep:

            encoded_char = chr((ord(char) - 65 + shift) % 26 + 65)

# Add the encoded character to the encoded message

            encoded_message += encoded_char

# Divide the encoded message into blocks of five letters

    blocks = [encoded_message [i:i+5] for i in range(0, len(encoded_message), 5)]

# Print the encoded message with ten blocks per line

    for i in range(0, len(blocks), 10):

        print(" ".join(blocks[i:i+10]))

# Get the shift amount from the command line

shift = int(sys.argv[1])

# Read the message from the keyboard

message = input()

# Encode the message using the Caesar cipher

encoded_message = caesar_cipher(message, shift)
