from JPPhoneNumberBuilder import JPPhoneNumberBuilder

if __name__ == "__main__":

    try:
        pnbuilder = JPPhoneNumberBuilder('0139456789')        
        phone_number = pnbuilder.hyphenated()
        print(phone_number)
        
    except ValueError as ve:
        print(ve)
