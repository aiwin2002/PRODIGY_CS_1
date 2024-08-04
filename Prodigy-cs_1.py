def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) + shift - shift_amount) % 26 + shift_amount)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    choice = input("Do you want to (e)ncrypt or (d)ecrypt? ").lower()
    if choice not in ['e', 'd']:
        print("Invalid choice!")
        return

    message = input("Enter your message: ")
    shift = int(input("Enter the shift value: "))

    if choice == 'e':
        result = encrypt(message, shift)
    else:
        result = decrypt(message, shift)

    print(f"Result: {result}")

if __name__ == "__main__":
    main()
