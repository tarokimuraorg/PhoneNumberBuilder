import re
from StringConvertor import StringConvertor
from ErrorMessageCreator import ErrorMessageCreator

class JPPhoneNumberBuilder:
    
    def __init__(self, phone_number : str):

        self._emcreator = ErrorMessageCreator()
        self._strconvertor = StringConvertor()

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
        out_phone_number = self._strconvertor.toHankaku(out_phone_number)

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

    def digits_only(self) -> str:

        if (re.match('^0\d{9}$',self._phone_number)):
            return self._phone_number

        raise ValueError(self._emcreator.message('PhoneNumberBuilder.py','init','invalid argument','the argument is an incompatible phone number.'))

    def hyphenated(self) -> str:
     
        if (re.match('^0\d{9}$',self._phone_number)):
            
            # 市外局番 : 4桁
            four_digits = []
            four_digits.append('1267')
            four_digits.append('1372')
            four_digits.append('1374')
            four_digits.append('1377')
            four_digits.append('1392')
            four_digits.append('1397')
            four_digits.append('1398')
            four_digits.append('1456')
            four_digits.append('1457')
            four_digits.append('1466')
            four_digits.append('1547')
            four_digits.append('1558')
            four_digits.append('1564')
            four_digits.append('1586')
            four_digits.append('1587')
            four_digits.append('1632')
            four_digits.append('1634')
            four_digits.append('1635')
            four_digits.append('1648')
            four_digits.append('1654')
            four_digits.append('1655')
            four_digits.append('1656')
            four_digits.append('1658')

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
            three_digits.append('142')
            three_digits.append('143')
            three_digits.append('144')
            three_digits.append('145')
            three_digits.append('146')
            three_digits.append('152')
            three_digits.append('153')
            three_digits.append('154')
            three_digits.append('155')
            three_digits.append('156')
            three_digits.append('157')
            three_digits.append('158')
            three_digits.append('162')
            three_digits.append('163')
            three_digits.append('164')
            three_digits.append('165')
            three_digits.append('166')
            three_digits.append('167')
            three_digits.append('172')
            three_digits.append('173')
            three_digits.append('174')
            three_digits.append('175')
            three_digits.append('176')
            three_digits.append('178')
            three_digits.append('179')
            three_digits.append('182')
            three_digits.append('183')
            three_digits.append('184')
            three_digits.append('185')
            three_digits.append('186')
            three_digits.append('187')
            three_digits.append('191')
            three_digits.append('192')
            three_digits.append('193')
            three_digits.append('194')
            three_digits.append('195')
            three_digits.append('197')
            three_digits.append('198')
            three_digits.append('220')
            three_digits.append('223')
            three_digits.append('224')
            three_digits.append('225')
            three_digits.append('226')
            three_digits.append('228')
            three_digits.append('229')
            three_digits.append('233')
            three_digits.append('234')
            three_digits.append('235')
            three_digits.append('237')
            three_digits.append('238')
            three_digits.append('240')
            three_digits.append('241')
            three_digits.append('242')
            three_digits.append('243')
            three_digits.append('244')
            three_digits.append('246')
            three_digits.append('247')
            three_digits.append('248')
            three_digits.append('250')
            three_digits.append('254')
            three_digits.append('255')
            three_digits.append('256')
            three_digits.append('257')
            three_digits.append('258')
            three_digits.append('259')
            three_digits.append('260')
            three_digits.append('261')
            three_digits.append('263')
            three_digits.append('264')
            three_digits.append('265')
            three_digits.append('266')
            three_digits.append('267')
            three_digits.append('268')
            three_digits.append('269')
            three_digits.append('270')
            three_digits.append('274')

            if (self._phone_number[1:4] in three_digits):
                return "{}-{}-{}".format(self._phone_number[0:4],self._phone_number[4:6],self._phone_number[6:])

            # 市外局番 : 2桁
            two_digits = []
            two_digits.append('11')
            two_digits.append('15')
            two_digits.append('17')
            two_digits.append('18')
            two_digits.append('19')
            two_digits.append('22')
            two_digits.append('23')
            two_digits.append('24')
            two_digits.append('25')
            two_digits.append('26')
            two_digits.append('27')

            if (self._phone_number[1:3] in two_digits):
                return "{}-{}-{}".format(self._phone_number[0:3],self._phone_number[3:6],self._phone_number[6:])

            raise ValueError(self._emcreator.message('PhoneNumberBuilder.py','init','invalid argument','the argument is an incompatible phone number.'))

        raise ValueError(self._emcreator.message('PhoneNumberBuilder.py','init','invalid argument','the argument must be a 10-digit number.'))
