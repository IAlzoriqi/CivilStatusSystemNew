import random
from datetime import date
from datetime import datetime
from MilitaryCardMain import MilitaryParentCard


class MilitaryCard(MilitaryParentCard):

    def __init__(self, firstname, fathername, grandfathername, familyname, side

                 ):

        MilitaryParentCard.__init__(
            self, firstname, fathername, grandfathername, familyname)

        today = date.today()

        self.side = side
        self.fathername = fathername
        self.grandfathername = grandfathername
        self.familyname = familyname
        self.ID = random.randrange(000000000000, 999999999999)
        self.releasedate = today

        expiryYears = datetime.now().year
        type(expiryYears+10)
        expiryYears = expiryYears+10
        self.expirydate = "{0}-{1}-{2}".format(expiryYears,
                                               datetime.now().month, datetime.now().day-1)

    def PrintData(self):
        print('military number  is', self.ID)
        print('first name is', self.firstname)
        print('father name is', self.fathername)
        print('grandfather name is', self.grandfathername)
        print('family name is', self.familyname)
        print("release date", f"   {self.releasedate}",)
        print("expiry date", f"   {self.expirydate}",)

    def PrintCard(self):
        print('-'*50)
        print(" "*1, "*"*4, "Republic of Yemen")
        print(" "*1, "*"*4, "Ministry of the Interior")
        print(" "*1, "*"*4, "Civil Status and Civil Registry Authority")
        print('The military NO : ', self.ID)
        print(
            f'''{self.firstname} {self.fathername} {self.grandfathername} {self.familyname}''')
        print('first name is', self.firstname)
        print('father name is', self.fathername)
        print('grand father name is', self.grandfathername)
        print('family name is', self.familyname)
        print("The side", f"   {self.side}",)

        print("release date", f"   {self.releasedate}",)
        print("expiry date", f"   {self.expirydate}",)
        print('-'*50)
