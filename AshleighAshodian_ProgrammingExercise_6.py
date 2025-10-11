import re

def validate_phone(phone):
    pattern = r'\d\d\d[ -]\d\d\d[ -]\d\d\d\d'
    return bool(re.match(pattern, phone))

def validate_ssn(ssn):
    pattern = r'\d\d\d\d\d\d\d\d\d'
    return bool(re.match(pattern, ssn))

def validate_zip(zip_code):
    pattern = r'\d\d\d\d\d'
    return bool(re.match(pattern, zip_code))

def main():
    phone = input("Enter a phone number (can have dashes, spaces, or neither of those but no parenthesis): ")
    ssn = input("Enter a social security number (do not include spaces or special characters): ")
    zip_code = input("Enter a 5 digit ZIP code: ")

    print("\nValidation Results:")
    print(f"Phone number valid: {validate_phone(phone)}")
    print(f"Social Security number valid: {validate_ssn(ssn)}")
    print(f"ZIP code valid: {validate_zip(zip_code)}")

main()