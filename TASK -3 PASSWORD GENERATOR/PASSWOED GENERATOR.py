import random
import string

# Function to generate a password
def generate_password(length):
    # Create a pool of characters: uppercase, lowercase, digits, and special characters
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Main program
def main():
    print("--- Password Generator ---")
    try:
        # User input for password length
        length = int(input("Enter the desired length of the password (minimum 6 characters): "))
        if length < 6:
            print("Password length should be at least 6 characters for better security.")
            return
        
        # Generate and display the password
        password = generate_password(length)
        print(f"Generated password: {password}")
    
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
