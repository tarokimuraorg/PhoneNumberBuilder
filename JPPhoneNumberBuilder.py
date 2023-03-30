import re
from StringConvertor import StringConvertor
import ErrorMessageBuilder
import JPPhoneBook

class JPPhoneNumberBuilder:
    
    def __init__(self, phone_number : str):

        out_phone_number = phone_number.strip()
        out_phone_number = out_phone_number.replace('　','')
        out_phone_number = out_phone_number.replace(' ','')
        out_phone_number = out_phone_number.replace('（','')
        out_phone_number = out_phone_number.replace('）','')
        out_phone_number = out_phone_number.replace('(','')
        out_phone_number = out_phone_number.replace(')','')
        out_phone_number = re.sub('[―－−—–‒-]','',out_phone_number)
        out_phone_number = out_phone_number.replace('-','')
        out_phone_number = out_phone_number.replace('+','')
        out_phone_number = out_phone_number.replace('＋','')
        out_phone_number = StringConvertor().toHankaku(out_phone_number)

        self._phone_number = out_phone_number
        self._phone_book = JPPhoneBook.create()

    def digits_only(self) -> str:

        if (re.match('^0\d{9}$',self._phone_number)):
            return self._phone_number

        raise ValueError(ErrorMessageBuilder.message('PhoneNumberBuilder.py','digits_only','invalid argument','the argument is an incompatible phone number.'))

    def hyphenated(self) -> str:

        if (re.match('^0\d{9}$', self._phone_number)):

            head_digits = self._phone_number[1:4]

            # 付加的役務電話番号 : 4桁
            if (head_digits == '180'):

                if (self._phone_number[4:7] in self._phone_book[head_digits]):
                    return f"{self._phone_number[0:4]}-{self._phone_number[4:]}"

            elif (head_digits == '120' or head_digits == '570'):

                if (self._phone_number[4:7] in self._phone_book[head_digits]):
                    return f"{self._phone_number[0:4]}-{self._phone_number[4:7]}-{self._phone_number[7:]}"

            # 固定電話番号 - 市外局番 : 5桁
            head_digits = self._phone_number[1:5]

            if (head_digits in self._phone_book):

                if (self._phone_number[5:6] in self._phone_book[head_digits]):
                    return f"{self._phone_number[0:5]}-{self._phone_number[5:6]}-{self._phone_number[6:]}"

            # 固定電話番号 - 市外局番 : 4桁
            head_digits = self._phone_number[1:4]

            if (head_digits in self._phone_book):

                if (self._phone_number[4:6] in self._phone_book[head_digits]):
                    return f"{self._phone_number[0:4]}-{self._phone_number[4:6]}-{self._phone_number[6:]}"
                
            # 固定電話番号 - 市外局番 : 3桁
            head_digits = self._phone_number[1:3]

            if (head_digits in self._phone_book):

                if (self._phone_number[3:6] in self._phone_book[head_digits]):
                    return f"{self._phone_number[0:3]}-{self._phone_number[3:6]}-{self._phone_number[6:]}"

            raise ValueError(ErrorMessageBuilder.message('PhoneNumberBuilder.py','hyphenated','invalid argument',f'the argument ({self._phone_number}) is an incompatible phone number.'))

        raise ValueError(ErrorMessageBuilder.message('PhoneNumberBuilder.py','hyphenated','invalid argument','the argument must be a 10-digit number.'))
