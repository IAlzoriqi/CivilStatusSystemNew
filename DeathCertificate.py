

import random
from CardModel import Card


class DeathCertificate(Card):

    def __init__(self, firstname, fathername, grandfathername, familyname,
                 mothername, IC_ID, datedeath, placedath, socialstatus
                 ):
        Card.__init__(self, firstname, fathername, grandfathername, familyname)

        self.mothername = mothername
        self.IC_ID = IC_ID
        self.datedeath = datedeath
        self.placedath = placedath
        self.socialstatus = socialstatus
        self.ID = random.randrange(000000000000, 999999999999)

    def PrintData(self):
        Card.PrintData(self)
        print('The ID NO : ', self.ID)
        print('mother name   is', self.mothername)
        print('IC ID is', self.IC_ID)
        print('social status  is', self.socialstatus)
        print('date death  is', self.datedeath)
        print('place death  is', self.placedath)

    def PrintCard(self):
        print('-'*50)
        print(" "*1, "*"*4, "Republic of Yemen")
        print(" "*1, "*"*4, "Ministry of the Interior")
        print(" "*1, "*"*4, "Civil Status and Civil Registry Authority")
        print('The ID NO : ', self.ID)
        print(
            f'''{self.firstname} {self.fathername} {self.grandfathername} {self.familyname}''')
        print('IC ID is', self.IC_ID)
        print('mother name   is', self.mothername)
        print('social status  is', self.socialstatus)
        print('date death  is', self.datedeath)
        print('place death  is', self.placedath)
        print("release date", f"   {self.releasedate}",)
        print('-'*50)
