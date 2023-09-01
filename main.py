from JPPhoneNumberBuilder import JPPhoneNumberBuilder

if __name__ == "__main__":

    try:
        pnbuilder = JPPhoneNumberBuilder('0150756789')
        print(pnbuilder.digits_only())
        
        phone_number = pnbuilder.hyphenated()
        print(phone_number)
        
    except ValueError as ve:
        print(ve)
