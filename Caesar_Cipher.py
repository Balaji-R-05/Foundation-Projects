# Caesar Cipher Algorithm
# Encrypts or decrypts a message by shifting each letter by a fixed number of positions.

def caesar(message, offset, cmd=1) -> str:
    """
    Encrypts or decrypts a message using the Caesar cipher.
    
    Args:
        message (str): The input message to process.
        offset (int): The number of positions to shift.
        cmd (int): Command - 1 for encryption, -1 for decryption.
    
    Returns:
        str: The processed message.
    """
    result = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    for char in message:
        if char.isalpha():  # Check if character is a letter
            is_upper = char.isupper()  # Preserve the case
            char = char.lower()  # Convert to lowercase for processing
            shift = alphabet.index(char) + (offset * cmd)  # Adjust shift based on cmd
            shifted_char = alphabet[shift % 26]  # Perform the shift
            result += shifted_char.upper() if is_upper else shifted_char  # Restore case
        else:
            result += char  # Keep non-alphabet characters unchanged
    
    return result


# User input
message = input("Enter the message to encrypt or decrypt: ").strip()
shift = int(input("Enter the shift value (positive for encryptio'n, negative for decryption): "))

# Perform Caesar Cipher
encrypted_message = caesar(message, shift, cmd=1)  # Encrypt
print(f"Encrypted message: {encrypted_message}")

decrypted_message = caesar(encrypted_message, shift, cmd=-1)  # Decrypt
print(f"Decrypted message: {decrypted_message}")
