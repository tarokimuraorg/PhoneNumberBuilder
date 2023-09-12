from JPPhoneNumberBuilder import JPPhoneNumberBuilder

for cnt in range(0,10):

    try:
        pnbuilder = JPPhoneNumberBuilder(f'01439{cnt}0000')
        phone_number = pnbuilder.hyphenated()
        print(phone_number)

    except ValueError as ve:
        print(ve)
        continue
