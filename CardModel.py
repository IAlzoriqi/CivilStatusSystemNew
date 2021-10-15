import random
from datetime import date


class Card:

    def __init__(self, firstname, fathername, grandfathername, familyname,

                 ):
        today = date.today()

        self.firstname = firstname
        self.fathername = fathername
        self.grandfathername = grandfathername
        self.familyname = familyname
        self.releasedate = today

    def PrintData(self):
        print('first name is', self.firstname)
        print('father name is', self.fathername)
        print('grand father name is', self.grandfathername)
        print('family name is', self.familyname)
        print('release date is', self.releasedate)


# c = Card("dfhfhfh", "sjdjdj", "dhdhdhd", "dhdhdh")
# c.PrintData()
# print("---------------------------------")
# c.firstname = "Ibrahim"

# c.PrintData()
