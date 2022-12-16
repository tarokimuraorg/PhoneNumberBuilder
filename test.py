from JPPhoneNumberBuilder import JPPhoneNumberBuilder

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

    """
    phone_number = pnbuilder.digits_only()
    print(phone_number)
        
    phone_number = pnbuilder.hyphenated()
    print(phone_number)
    """

    for cnt1 in range(0,10):

        #pnbuilder = JPPhoneNumberBuilder('012006{}000'.format(cnt))
        #pnbuilder = JPPhoneNumberBuilder('012007{}000'.format(cnt))
        #pnbuilder = JPPhoneNumberBuilder('012008{}000'.format(cnt))
        #pnbuilder = JPPhoneNumberBuilder('012009{}000'.format(cnt))

        #pnbuilder = JPPhoneNumberBuilder('012010{}000'.format(cnt))
        #pnbuilder = JPPhoneNumberBuilder('012011{}000'.format(cnt))
        #pnbuilder = JPPhoneNumberBuilder('012012{}000'.format(cnt))
        #pnbuilder = JPPhoneNumberBuilder('012013{}000'.format(cnt))
        #pnbuilder = JPPhoneNumberBuilder('012014{}000'.format(cnt))
        #pnbuilder = JPPhoneNumberBuilder('012015{}000'.format(cnt))
        #pnbuilder = JPPhoneNumberBuilder('012016{}000'.format(cnt))
        #pnbuilder = JPPhoneNumberBuilder('012017{}000'.format(cnt))
        #pnbuilder = JPPhoneNumberBuilder('012018{}000'.format(cnt))
        #pnbuilder = JPPhoneNumberBuilder('012019{}000'.format(cnt))

        #pnbuilder = JPPhoneNumberBuilder('012020{}000'.format(cnt))
        #pnbuilder = JPPhoneNumberBuilder('012021{}000'.format(cnt))
        #pnbuilder = JPPhoneNumberBuilder('012022{}000'.format(cnt))
        #pnbuilder = JPPhoneNumberBuilder('012023{}000'.format(cnt))
        #pnbuilder = JPPhoneNumberBuilder('012024{}000'.format(cnt))
        #pnbuilder = JPPhoneNumberBuilder('012025{}000'.format(cnt))
        #pnbuilder = JPPhoneNumberBuilder('012026{}000'.format(cnt))
        #pnbuilder = JPPhoneNumberBuilder('012027{}000'.format(cnt))
        #pnbuilder = JPPhoneNumberBuilder('012028{}000'.format(cnt))
        #pnbuilder = JPPhoneNumberBuilder('012029{}000'.format(cnt))

        for cnt2 in range(0,10):

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
        
except ValueError as ve:
    print(ve)
