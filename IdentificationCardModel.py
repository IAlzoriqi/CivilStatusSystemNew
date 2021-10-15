from datetime import date
from datetime import datetime

import random
from CardModel import Card


class IdentificationCard(Card):

    def __init__(self, firstname, fathername, grandfathername, familyname,
                 mothername, datebirth, gender, placebirth, bloodtype
                 ):
        Card.__init__(self, firstname, fathername, grandfathername, familyname,

                      )

        expiryYears = datetime.now().year
        type(expiryYears+10)
        expiryYears = expiryYears+10
        expirydate = "{0}-{1}-{2}".format(expiryYears,
                                          datetime.now().month, datetime.now().day-1)
        self.bloodtype = bloodtype

        self.expirydate = expirydate
        self.ID = random.randrange(000000000000, 999999999999)
        self.placebirth = placebirth
        self.mothername = mothername
        self.datebirth = datebirth
        self.gender = gender
        self.IdentificationCardList = []

    def PrintData(self):
        Card.PrintData(self)
        print('blood type  is', self.bloodtype)
        print('release date is', self.releasedate)
        print('expiry date is', self.expirydate)
        print('place of birth  is', self.placebirth)
        print('date of birth is', self.datebirth)
        print('mother name is', self.mothername)
        print('Gender is', self.gender)

    def PrintCard(self):
        print('-'*50)
        print(" "*1, "*"*4, "Republic of Yemen")
        print(" "*1, "*"*4, "Ministry of the Interior")
        print(" "*1, "*"*4, "Civil Status and Civil Registry Authority")
        print('The ID NO : ', self.ID)

        print(
            f'''{self.firstname} {self.fathername} {self.grandfathername} {self.familyname}''')

        print("Brith and Place of Date ",
              f"{self.placebirth}", f"   {self.datebirth}",)
        print(f"blood type\n", f"   {self.bloodtype}",)

        print(" "*5, "*"*20)

        print(" "*5, "*"*20)

        print(" "*5, "*"*20)

        print("release date", f"   {self.releasedate}",)
        print("expiry date", f"   {self.expirydate}",)
        print('-'*50)


# p = IdentificationCard("djdjdjd", "djdjdjd", "dddhdhd", "djdjdjd", "djdjhdd",

#                        "2019-5-4", "Male", "Taiz", "o+")
# p.PrintCard()
