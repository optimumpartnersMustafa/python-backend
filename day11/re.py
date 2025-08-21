import re
from datetime import datetime
import pytz 

# Exercise 1: 
def validate_email(email_address):
    email_regex = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    if email_regex.match(email_address):
        username, domain = email_address.split('@')
        return True, "Email is valid!", {'username': username, 'domain': domain}
    else:
        return False, "Email is invalid.", None

# Exercise 2: 
def extract_dates(text):
    date_regex = re.compile(r'\b(\d{2}[-/]\d{2}[-/]\d{4})\b')
    return date_regex.findall(text)

# Exercise 3: 
def time_until_next_birthday():
    try:
        birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
        birthdate = datetime.strptime(birthdate_str, '%Y-%m-%d').date()
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    today = datetime.now().date()
    current_year = today.year
    next_birthday = birthdate.replace(year=current_year)

    if next_birthday < today:
        next_birthday = next_birthday.replace(year=current_year + 1)

    time_remaining = datetime.combine(next_birthday, datetime.min.time()) - datetime.combine(today, datetime.min.time())

    days = time_remaining.days
    hours = time_remaining.seconds // 3600
    minutes = (time_remaining.seconds % 3600) // 60

    print(f"Time until your next birthday: {days} days, {hours} hours, and {minutes} minutes.")

# Exercise 4: 
def convert_timezone(time_str, from_tz_name, to_tz_name):
    try:
        dt_obj = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
        from_tz = pytz.timezone(from_tz_name)
        to_tz = pytz.timezone(to_tz_name)

        localized_dt = from_tz.localize(dt_obj)
        converted_dt = localized_dt.astimezone(to_tz)
        return converted_dt.strftime("%Y-%m-%d %H:%M:%S %Z%z")
    except pytz.UnknownTimeZoneError:
        return "Error: Unknown timezone name."
    except ValueError:
        return "Error: Invalid time string format. Use YYYY-MM-DD HH:MM:SS."

# Exercise 5: 
def parse_log_timestamps(log):
    timestamp_regex = re.compile(r'\[(\d{2}/[A-Za-z]{3}/\d{4}:\d{2}:\d{2}:\d{2} \+\d{4})\]')
    matches = timestamp_regex.findall(log)
    converted_timestamps = []
    for match in matches:
        try:
            # Parse the original format
            dt_obj = datetime.strptime(match, "%d/%b/%Y:%H:%M:%S %z")
            # Convert to UTC and then format
            converted_timestamps.append(dt_obj.astimezone(pytz.utc).strftime("%Y-%m-%d %H:%M:%S UTC"))
        except ValueError:
            converted_timestamps.append(f"Invalid timestamp format: {match}")
    return converted_timestamps

def main():
    print("Welcome to the Utility Hub!")

    # Exercise 1 Demo
    print("\n--- Exercise 1: Email Validation ---")
    while True:
        email_input = input("Enter email (or 'q' to quit): ").strip()
        if email_input.lower() == 'q':
            break
        is_valid, message, extracted_data = validate_email(email_input)
        print(message)
        if is_valid:
            print(f"  Extracted: User='{extracted_data['username']}', Domain='{extracted_data['domain']}'")
        print("-" * 20)

    # Exercise 2 Demo
    print("\n--- Exercise 2: Date Extraction ---")
    text_with_dates = "Meeting on 25-12-2023. Project deadline 01/01/2024. Next review 15-03-2024."
    extracted = extract_dates(text_with_dates)
    print(f"Text: '{text_with_dates}'")
    print(f"Extracted Dates: {extracted}")
    print("-" * 20)
    # Exercise 3 Demo
    print("\n--- Exercise 3: Time Until Next Birthday ---")
    time_until_next_birthday()
    print("-" * 20)

    # Exercise 4 Demo
    print("\n--- Exercise 4: Timezone Converter ---")
    time_to_convert = "2023-10-27 10:00:00"
    from_timezone = "America/New_York"
    to_timezone = "Europe/London"
    converted_time = convert_timezone(time_to_convert, from_timezone, to_timezone)
    print(f"'{time_to_convert}' from {from_timezone} to {to_timezone}: {converted_time}")
    print("-" * 20)

    # Exercise 5 Demo
    print("\n--- Exercise 5: Log Timestamp Extraction ---")
    log_string = (
        "INFO: [27/Oct/2023:14:30:05 +0000] User logged in.\n"
        "ERROR: [27/Oct/2023:15:00:10 +0000] Failed attempt.\n"
        "DEBUG: [28/Nov/2024:08:15:20 +0530] Data processed."
    )
    extracted_timestamps = parse_log_timestamps(log_string)
    print("Original Log Snippet:\n", log_string)
    print("Extracted & Converted Timestamps:")
    for ts in extracted_timestamps:
        print(ts)
    print("-" * 20)

    print("\nProgram finished. Goodbye!")

if __name__ == "__main__":
    main()
