

import random
from CardModel import Card


class BirthCertificate(Card):

    def __init__(self, firstname, fathername, grandfathername, familyname,
                 mothername, fatherID, motherID
                 ):
        Card.__init__(self, firstname, fathername, grandfathername, familyname,

                      )

        self.motherID = motherID
        self.mothername = mothername
        self.fatherID = fatherID
        self.ID = random.randrange(000000000000, 999999999999)

    def PrintData(self):
        Card.PrintData(self)
        print('The ID NO : ', self.ID)
        print('mother name   is', self.mothername)
        print('fatherID is', self.fatherID)
        print('motherID  is', self.motherID)

    def PrintCard(self):
        print('-'*50)
        print(" "*1, "*"*4, "Republic of Yemen")
        print(" "*1, "*"*4, "Ministry of the Interior")
        print(" "*1, "*"*4, "Civil Status and Civil Registry Authority")
        print('The ID NO : ', self.ID)

        print(
            f'''{self.firstname} {self.fathername} {self.grandfathername} {self.familyname}''')

        print("Mother Name ", f"   {self.mothername}",)
        print('mother name   is', self.mothername)
        print('fatherID is', self.fatherID)
        print('motherID  is', self.motherID)
        print("release date", f"   {self.releasedate}",)

        print('-'*50)
