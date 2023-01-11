from JPPhoneNumberBuilder import JPPhoneNumberBuilder

"""
try:

    print()

    #pnbuilder = JPPhoneNumberBuilder('０１394５６７８９')
    #pnbuilder = JPPhoneNumberBuilder('０１３９－４５－６７８９')
    #pnbuilder = JPPhoneNumberBuilder('０１３９４５６７８９')
    #pnbuilder = JPPhoneNumberBuilder('0139 - 45 - 6789')
    #pnbuilder = JPPhoneNumberBuilder('（０１３９）４５－６７８９')
    #pnbuilder = JPPhoneNumberBuilder('０１３９（４５）６７８９')
    #pnbuilder = JPPhoneNumberBuilder('0139(45)6789')
    #pnbuilder = JPPhoneNumberBuilder('+81 0139(45)6789')
    #pnbuilder = JPPhoneNumberBuilder('send a message!')

    #pnbuilder = JPPhoneNumberBuilder('0997956789')
    #pnbuilder = JPPhoneNumberBuilder('0120009000')
    #pnbuilder = JPPhoneNumberBuilder('0120009000')
    #pnbuilder = JPPhoneNumberBuilder('0120019000')
    #pnbuilder = JPPhoneNumberBuilder('0120029000')
    #pnbuilder = JPPhoneNumberBuilder('0120039000')
    #pnbuilder = JPPhoneNumberBuilder('0120049000')
    #pnbuilder = JPPhoneNumberBuilder('0120059000')

    phone_number = pnbuilder.digits_only()
    print(phone_number)
        
    phone_number = pnbuilder.hyphenated()
    print(phone_number)

    for cnt1 in range(0,10):

        for cnt2 in range(0,10):

            #pnbuilder = JPPhoneNumberBuilder('01200{}{}000'.format(cnt1, cnt2))
            #pnbuilder = JPPhoneNumberBuilder('01201{}{}000'.format(cnt1, cnt2))
            #pnbuilder = JPPhoneNumberBuilder('01202{}{}000'.format(cnt1, cnt2))
            #pnbuilder = JPPhoneNumberBuilder('01203{}{}000'.format(cnt1, cnt2))
            #pnbuilder = JPPhoneNumberBuilder('01204{}{}000'.format(cnt1, cnt2))
            #pnbuilder = JPPhoneNumberBuilder('01205{}{}000'.format(cnt1, cnt2))
            #pnbuilder = JPPhoneNumberBuilder('01206{}{}000'.format(cnt1, cnt2))
            #pnbuilder = JPPhoneNumberBuilder('01207{}{}000'.format(cnt1, cnt2))
            #pnbuilder = JPPhoneNumberBuilder('01208{}{}000'.format(cnt1, cnt2))

            if cnt1 == 0 and cnt2 == 2:
                continue

            if cnt1 == 0 and cnt2 == 3:
                continue

            if cnt1 == 0 and cnt2 == 4:
                continue

            if cnt1 == 0 and cnt2 == 6:
                continue

            if cnt1 == 0 and cnt2 == 8:
                continue

            if cnt1 == 0 and cnt2 == 9:
                continue

            if cnt1 == 4 and cnt2 == 2:
                continue

            if cnt1 == 4 and cnt2 == 3:
                continue

            pnbuilder = JPPhoneNumberBuilder('01209{}{}000'.format(cnt1, cnt2))

            phone_number = pnbuilder.hyphenated()
            print(phone_number)

        print()

    for cnt in range(0,10):

        pnbuilder = JPPhoneNumberBuilder(f'018099{cnt}000')
        phone_number = pnbuilder.hyphenated()
        print(phone_number)

    for cnt1 in range(0,10):

        for cnt2 in range(0,10):

            pnbuilder = JPPhoneNumberBuilder(f'05700{cnt1}{cnt2}000')
            phone_number = pnbuilder.hyphenated()
            print(phone_number)

        print()

    for cnt in range(1,10):

        pnbuilder = JPPhoneNumberBuilder(f'057012{cnt}000')
        phone_number = pnbuilder.hyphenated()
        print(phone_number)
    
        
except ValueError as ve:
    print(ve)
"""
"""
for cnt in range(0,10):

    try:
        pnbuilder = JPPhoneNumberBuilder(f'057020{cnt}000')
        phone_number = pnbuilder.hyphenated()
        print(phone_number)

    except ValueError as ve:
        print(ve)
        continue
"""

for cnt1 in range(0, 10):

    for cnt2 in range(0, 10):

        try:
            pnbuilder = JPPhoneNumberBuilder(f'05709{cnt1}{cnt2}000')
            phone_number = pnbuilder.hyphenated()
            print(phone_number)

        except ValueError as ve:
            print(ve)
            continue
