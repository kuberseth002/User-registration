import re


def valid_first_name():
    """
    Validates the first name.
    
    - The name must start with an uppercase letter.
    - The remaining letters should be lowercase.
    - Minimum length: 1 characters.

    Returns:
        None
    """
    try:
        pattern = "^[A-Z][a-z]{1,}$"
        first_name = input("Enter first name: ").strip()

        if not first_name:
            raise ValueError("First name cannot be empty.")

        if re.match(pattern, first_name):
            print("It is a valid name.")
        else:
            print("It is an invalid name.")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def valid_last_name(last_name):
    """
    Validates the last name.
    
    - The last name must start with an uppercase letter.
    - Must be at least 2 characters long.

    Args:
        last_name (str): The last name entered by the user.

    Returns:
        None
    """
    try:
        pattern = "^[A-Z][a-z]{2,}$"
        
        if not last_name:
            raise ValueError("Last name cannot be empty.")

        if re.match(pattern, last_name):
            print("The last name is valid.")
        else:
            print("It is not a valid name.")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def valid_email():
    """
    Validates an email address.

    Returns:
        None
    """
    try:
        pattern = r"^[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)?@[a-zA-Z0-9]+\.[a-zA-Z]{2,}(\.[a-zA-Z]{2,})?$"
        email = input("Enter your email: ").strip()

        if not email:
            raise ValueError("Email cannot be empty.")

        if re.match(pattern, email):
            print("Valid email.")
        else:
            print("Not a valid email.")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def valid_mobile_number(mobile_number):
    """
    Validates an Indian mobile number.

    Args:
        mobile_number (str): The mobile number entered by the user.

    Returns:
        None
    """
    try:
        pattern = r"^(91)[6-9][0-9]{9}$"

        if not mobile_number:
            raise ValueError("Mobile number cannot be empty.")

        if re.match(pattern, mobile_number):
            print("Valid mobile number.")
        else:
            print("Not a valid number.")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def validate_password():
    """
    Validates if a password meets minimum length criteria.

    Returns:
        None
    """
    try:
        password = input("Enter your password: ").strip()
        pattern = r"^.{8,}$"

        if not password:
            raise ValueError("Password cannot be empty.")

        if re.match(pattern, password):
            print("Valid Password.")
        else:
            print("Invalid Password (Must be at least 8 characters long).")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def password_uppercase(password):
    """
    Checks if a password contains at least one uppercase letter.

    Args:
        password (str): The password entered by the user.

    Returns:
        None
    """
    try:
        pattern = r"^(?=.*[A-Z]).{8,}$"

        if not password:
            raise ValueError("Password cannot be empty.")

        if re.match(pattern, password):
            print("It is correct.")
        else:
            print("It is not correct.")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def password_numeric():
    """
    Checks if a password contains at least one numeric digit.

    Returns:
        None
    """
    try:
        pattern = r"^(?=.*[A-Z])(?=.*\d).{8,}$"
        password = input("Enter a password: ").strip()

        if not password:
            raise ValueError("Password cannot be empty.")

        if re.match(pattern, password):
            print("Valid password.")
        else:
            print("Not a valid password.")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def password_special_character(password):
    """
    Checks if a password contains at least one special character.

    Args:
        password (str): The password entered by the user.

    Returns:
        None
    """
    try:
        pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^a-zA-Z0-9]).{8,}$"

        if not password:
            raise ValueError("Password cannot be empty.")

        if re.match(pattern, password):
            print("It is correct.")
        else:
            print("It is not correct.")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def main():
    """
    Main function to execute all validation functions.
    """
    try:
        valid_first_name()
        
        last_name = input("Enter your last name: ").strip()
        valid_last_name(last_name)

        valid_email()

        number = input("Enter your phone number: ").strip()
        valid_mobile_number(number)

        validate_password()

        password = input("Enter the password for uppercase validation: ").strip()
        password_uppercase(password)

        password_numeric()

        password = input("Enter the password for special character validation: ").strip()
        password_special_character(password)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
