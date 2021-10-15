import random
from CardModel import Card


class FamilyCard(Card):
    def __init__(self, firstname, fathername, grandfathername, familyname,
                 wifename, city, directorate, street
                 ):
        Card.__init__(self, firstname, fathername, grandfathername, familyname,

                      )

        self.directorate = directorate
        self.city = city
        self.street = street
        self.wifename = wifename
        self.ID = random.randrange(000000000000, 999999999999)
       


    def PrintData(self):
        Card.PrintData(self)
        print('The ID NO : ', self.ID)
        print('wife name   is', self.wifename)
        print('city is', self.city)
        print('directorate  is', self.directorate)
        print('street  is', self.street)


    def PrintCard(self):
        print('-'*50)
        print(" "*1, "*"*4, "Republic of Yemen")
        print(" "*1, "*"*4, "Ministry of the Interior")
        print(" "*1, "*"*4, "Civil Status and Civil Registry Authority")
        print('The ID NO : ', self.ID)

        print(
            f'''{self.firstname} {self.fathername} {self.grandfathername} {self.familyname}''')

        print("Mother Name ", f"   {self.wifename}",)
        print("city ", f"   {self.city}",)
        print("directorate ", f"   {self.directorate}",)
        print("street ", f"   {self.street}",)
        print("release date", f"   {self.releasedate}",)
        print('-'*50)

    