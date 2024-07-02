import argparse
import string
import secrets


def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special):
    allowed_chars = ""

    if use_uppercase:
        allowed_chars += string.ascii_uppercase
    if use_lowercase:
        allowed_chars += string.ascii_lowercase
    if use_digits:
        allowed_chars += string.digits
    if use_special:
        allowed_chars += string.punctuation

    if len(allowed_chars) == 0:
        raise ValueError("At least one character set (uppercase, lowercase, digits, special) must be enabled.")

    password = ''.join(secrets.choice(allowed_chars) for _ in range(length))
    return password


def main():
    parser = argparse.ArgumentParser(description="Generate a random password.")
    parser.add_argument("length", type=int, help="Length of the password")
    parser.add_argument("--upper", action="store_true", help="Include uppercase letters")
    parser.add_argument("--lower", action="store_true", help="Include lowercase letters")
    parser.add_argument("--digits", action="store_true", help="Include digits")
    parser.add_argument("--special", action="store_true", help="Include special characters")

    args = parser.parse_args()

    try:
        password = generate_password(args.length, args.upper, args.lower, args.digits, args.special)
        print("Generated Password:", password)
    except ValueError as ve:
        print(f"Error: {ve}")
        parser.print_help()


if __name__ == "__main__":
    main()
