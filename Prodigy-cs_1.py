def caesar_cipher(text, shift, mode='encrypt'):
    result = ""

    # Adjust shift for decryption
    if mode == 'decrypt':
        shift = -shift

    # Loop through each character in the text
    for char in text:
        # Encrypt/Decrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt/Decrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # Non-alphabetic characters are added unchanged
            result += char

    return result

def main():
    print("Welcome to the Caesar Cipher program!")
    while True:
        choice = input("Would you like to (e)ncrypt or (d)ecrypt a message? (e/d): ").lower()
        if choice not in ['e', 'd']:
            print("Invalid choice! Please enter 'e' for encrypt or 'd' for decrypt.")
            continue

        message = input("Enter your message: ")
        shift = int(input("Enter the shift value: "))

        if choice == 'e':
            mode = 'encrypt'
        else:
            mode = 'decrypt'

        result = caesar_cipher(message, shift, mode)
        print(f"Result: {result}")

        another = input("Would you like to encrypt/decrypt another message? (y/n): ").lower()
        if another != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
