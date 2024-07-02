import random
import string
import argparse

def generate_password(length, uppercase=False, digits=False, special_chars=False):
    # Define character sets based on requirements
    characters = string.ascii_lowercase
    if uppercase:
        characters += string.ascii_uppercase
    if digits:
        characters += string.digits
    if special_chars:
        characters += string.punctuation

    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    parser = argparse.ArgumentParser(description='Generate a random password with specified options.')
    parser.add_argument('length', type=int, help='Length of the password')
    parser.add_argument('--uppercase', action='store_true', help='Include uppercase letters')
    parser.add_argument('--digits', action='store_true', help='Include digits')
    parser.add_argument('--special-chars', action='store_true', help='Include special characters')

    args = parser.parse_args()

    # Validate at least one character type is included
    if not (args.uppercase or args.digits or args.special_chars):
        parser.error('At least one of --uppercase, --digits, or --special-chars must be provided.')

    password = generate_password(args.length, args.uppercase, args.digits, args.special_chars)
    print(f'Generated Password: {password}')

if __name__ == '__main__':
    main()
