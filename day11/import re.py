import re
from datetime import datetime

def validate_email(email_address):
    email_regex = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

    if not email_address:
        return False, "Input cannot be empty.", None

    if email_regex.match(email_address):
        username, domain = email_address.split('@')
        return True, "Email is valid!", {'username': username, 'domain': domain}
    else:
        return False, "Email is invalid.", None

def main():
    print("Welcome to the Utility Hub!")

    # --- Email Validator ---
    print("\n--- Email Validator ---")
    while True:
        email_input = input("Enter email (or 'q' to quit): ").strip()
        if email_input.lower() == 'q':
            break

        is_valid, message, extracted_data = validate_email(email_input)
        print(message)
        if is_valid:
            print(f"  Extracted: User='{extracted_data['username']}', Domain='{extracted_data['domain']}'")
        print("-" * 20)

    # --- Current Local Time ---
    print("\n--- Current Local Time ---")
    print(f"The current time is: {datetime.now().strftime('%Y-%m-%d %I:%M:%S %p')}")

if __name__ == "__main__":
    main()
