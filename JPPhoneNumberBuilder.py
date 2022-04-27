import re
from StringConvertor import StringConvertor
from ErrorMessageCreator import ErrorMessageCreator

class JPPhoneNumberBuilder:
    
    def __init__(self, phone_number : str):

        self._emcreator = ErrorMessageCreator()
        self._strconvertor = StringConvertor()

        out_phone_number = phone_number.replace('　',' ')
        out_phone_number = out_phone_number.replace('（',' ')
        out_phone_number = out_phone_number.replace('）',' ')
        out_phone_number = out_phone_number.replace('(',' ')
        out_phone_number = out_phone_number.replace(')',' ')
        out_phone_number = re.sub('[―－−—–‒-]',' ',out_phone_number)
        out_phone_number = out_phone_number.replace('-',' ')
        out_phone_number = out_phone_number.strip()
        out_phone_number = re.sub(' +','-',out_phone_number)
        out_phone_number = self._strconvertor.toHankaku(out_phone_number)

        if (phone_number[0] != "0"):
            raise ValueError(self._emcreator.message('PhoneNumberBuilder.py','init','invalid argument','the argument is an incompatible phone number.'))

        self._phone_number = out_phone_number

    def isJPPhoneNumber(self) -> bool:
        
        if (re.match('^0\d{1}-\d{4}-\d{4}$',self._phone_number)):
            return True

        if (re.match('^0\d{2}-\d{3}-\d{4}$',self._phone_number)):
            return True

        if (re.match('^0\d{3}-\d{2}-\d{4}$',self._phone_number)):
            return True

        if (re.match('^0\d{4}-\d{1}-\d{4}$',self._phone_number)):
            return True
          
        return False

    def hyphenated(self) -> str:

        if (self.isJPPhoneNumber()):
            return self._phone_number

        if (re.match('^0\d{9}$',self._phone_number)):
            
            # 市外局番 : 4桁
            four_digits = []
            four_digits.append('1267')
            four_digits.append('1372')
            four_digits.append('1374')
            four_digits.append('1377')
            four_digits.append('1392')

            if (self._phone_number[1:5] in four_digits):
                return "{}-{}-{}".format(self._phone_number[0:5],self._phone_number[5:6],self._phone_number[6:])

            # 市外局番 : 3桁
            three_digits = []
            three_digits.append('123')
            three_digits.append('124')
            three_digits.append('125')
            three_digits.append('126')
            three_digits.append('133')
            three_digits.append('134')
            three_digits.append('135')
            three_digits.append('136')
            three_digits.append('137')
            three_digits.append('138')
            three_digits.append('139')

            if (self._phone_number[1:4] in three_digits):
                return "{}-{}-{}".format(self._phone_number[0:4],self._phone_number[4:6],self._phone_number[6:])

            # 市外局番 : 2桁
            two_digits = []
            two_digits.append('11')

            if (self._phone_number[1:3] in two_digits):
                return "{}-{}-{}".format(self._phone_number[0:3],self._phone_number[3:6],self._phone_number[6:])

            raise ValueError(self._emcreator.message('PhoneNumberBuilder.py','init','invalid argument','the argument is an incompatible phone number.'))

        raise ValueError(self._emcreator.message('PhoneNumberBuilder.py','init','invalid argument','the argument must be a 10-digit number.'))
