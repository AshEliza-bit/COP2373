import re

def validate_phone(phone): # validate phone number
    pattern = r'^\d{3}[ -]?\d{3}[ -]?\d{4}$'
    return bool(re.match(pattern, phone)) # returns results

def validate_ssn(ssn): #validates social security number
    pattern = r'^\d{3}[ -]?\d{2}[ -]?\d{4}$'
    return bool(re.match(pattern, ssn)) # returns results

def validate_zip(zip_code): #validates zip code
    pattern = r'\d\d\d\d\d'
    return bool(re.match(pattern, zip_code)) # returns results

def main():
    phone = input("Enter a phone number: ")
    ssn = input("Enter a social security number: ")
    zip_code = input("Enter a 5 digit ZIP code: ")

    print(f"Phone number valid: {validate_phone(phone)}")
    print(f"Social Security number valid: {validate_ssn(ssn)}")
    print(f"ZIP code valid: {validate_zip(zip_code)}")

main()