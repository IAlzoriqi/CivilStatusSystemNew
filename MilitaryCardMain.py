import random
from datetime import date
from datetime import datetime


class MilitaryParentCard:

    def __init__(self, firstname, fathername, grandfathername, familyname,

                 ):
        today = date.today()

        self.firstname = firstname
        self.fathername = fathername
        self.grandfathername = grandfathername
        self.familyname = familyname
        self.releasedate = today

    def PrintData(self):
        print('military number  is', self.ID)
        print('first name is', self.firstname)
        print('father name is', self.fathername)
        print('grandfather name is', self.grandfathername)
        print('family name is', self.familyname)
