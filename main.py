from IdentificationCardModel import IdentificationCard
from FamilyCardModel import FamilyCard
from BirthCertificate import BirthCertificate
from DeathCertificate import DeathCertificate
from PrivateCard import PrivateCard
from MilitaryCard import MilitaryCard

from oprationListMethods import *


def CheckTypeMilitarylServicessCard(noTypeInput):
    if noTypeInput == 2:
        print("""
        Welcome To birth Private Card services System
                    Enter number (1) For Add
                    Enter number (2) For Update
                    Enter number (3) For Delete
                    Enter number (4) For Review


        """)
        noOpration = int(input("Enter No : "))

        if noOpration == 1:
            firstname = str(input("Enter first name :"))
            fathername = str(input("Enter father name :"))
            grandfathername = str(input("Enter grandfather name :"))
            familyname = str(input("Enter family name :"))
            place = str(input("Enter place  :"))

            m = PrivateCard(firstname, fathername,
                            grandfathername, familyname, place)
            m.PrintCard()

            OprationMethodsPrivateCard.saveNewCard(m)

        elif noOpration == 2:

            # print(data[0]["IdentificationCard"])

            OprationMethodsPrivateCard.reviewAllCard()
            index = int(input("Enter index user updata data : "))

            firstname = str(input("Enter first name :"))
            fathername = str(input("Enter father name :"))
            grandfathername = str(input("Enter grandfather name :"))
            familyname = str(input("Enter family name :"))
            place = str(input("Enter place  :"))

            m = PrivateCard(firstname, fathername,
                            grandfathername, familyname, place)
            m.PrintCard()

            OprationMethodsPrivateCard.updateOneCard(p, index)

        elif noOpration == 3:

            OprationMethodsPrivateCard.reviewAllCard()

            index = int(input("Enter index user delet Card : "))

            OprationMethodsPrivateCard.deleteOneCard(index)

        elif noOpration == 4:

            OprationMethodsPrivateCard.reviewAllCard()

    elif noTypeInput == 1:
        print("""
        Welcome To birth Private Card services System
        """)
        firstname = str(input("Enter first name :"))
        fathername = str(input("Enter father name :"))
        grandfathername = str(input("Enter grandfather name :"))
        familyname = str(input("Enter family name :"))
        side = str(input("Enter side  :"))

        m = MilitaryCard(firstname, fathername,
                         grandfathername, familyname, side)
        m.PrintCard()


def CheckTypeCivilServicessCard(noTypeInput):
    if noTypeInput == 1:
        print("""
        Welcome  To personal card services system
        """)

        # fathername = fathername
        # grandfathername = grandfathername
        # familyname = familyname
        print("""
        ***** Welcome to the Civil Status Cards Service *****
                    Enter number (1) For Add
                    Enter number (2) For Update
                    Enter number (3) For Delete
                    Enter number (4) For Review


        """)
        noOpration = int(input("Enter No : "))

        if noOpration == 1:
            firstname = str(input("Enter first name :"))
            fathername = str(input("Enter father name :"))
            grandfathername = str(input("Enter grandfather name :"))
            familyname = str(input("Enter family name :"))
            bloodtype = str(input("Enter blood type :"))
            gender = str(input("Enter gender :"))
            mothername = str(input("Enter mother name :"))
            datebirth = str(input("Enter date birth :"))
            placebirth = str(input("Enter place birth :"))
            p = IdentificationCard(firstname, fathername, grandfathername, familyname, mothername,

                                   datebirth, gender, placebirth, bloodtype)

            p.PrintCard()
            OprationMethodsIdentificationCard.saveNewCard(p)

        elif noOpration == 2:

            # print(data[0]["IdentificationCard"])

            OprationMethodsIdentificationCard.reviewAllCard()
            index = int(input("Enter index user updata data : "))
            firstname = str(input("Enter first name :"))
            fathername = str(input("Enter father name :"))
            grandfathername = str(input("Enter grandfather name :"))
            familyname = str(input("Enter family name :"))
            bloodtype = str(input("Enter blood type :"))
            gender = str(input("Enter gender :"))
            mothername = str(input("Enter mother name :"))
            datebirth = str(input("Enter date birth :"))
            placebirth = str(input("Enter place birth :"))
            p = IdentificationCard(firstname, fathername, grandfathername, familyname, mothername,
                                   datebirth, gender, placebirth, bloodtype)

            p.PrintCard()
            OprationMethodsIdentificationCard.updateOneCard(p, index)
        elif noOpration == 3:

            OprationMethodsIdentificationCard.reviewAllCard()

            index = int(input("Enter index user delet Card : "))

            OprationMethodsIdentificationCard.deleteOneCard(index)

        elif noOpration == 4:

            OprationMethodsIdentificationCard.reviewAllCard()

    elif noTypeInput == 2:

        print("""
        ***** Welcome to the  Family Cards Service *****
                    Enter number (1) For Add
                    Enter number (2) For Update
                    Enter number (3) For Delete
                    Enter number (4) For Review


        """)
        noOpration = int(input("Enter No : "))

        if noOpration == 1:
            firstname = str(input("Enter first name :"))
            fathername = str(input("Enter father name :"))
            grandfathername = str(input("Enter grandfather name :"))
            familyname = str(input("Enter family name :"))
            # bloodtype = str(input("Enter blood type :"))
            # gender = str(input("Enter gender :"))
            wifename = str(input("Enter the wife name :"))
            city = str(input("Enter city:"))
            directorate = str(input("Enter directorate :"))
            street = str(input("Enter street :"))

            f = FamilyCard(firstname, fathername, grandfathername,
                           familyname, wifename, city, directorate, street)
            f.PrintCard()
            OprationMethodsFamilyCard.saveNewCard(f)
        elif noOpration == 2:
            OprationMethodsFamilyCard.reviewAllCard()
            index = int(input("Enter index user updata data : "))
            firstname = str(input("Enter first name :"))
            fathername = str(input("Enter father name :"))
            grandfathername = str(input("Enter grandfather name :"))
            familyname = str(input("Enter family name :"))
            wifename = str(input("Enter the wife name :"))
            city = str(input("Enter city:"))
            directorate = str(input("Enter directorate :"))
            street = str(input("Enter street :"))
            f = FamilyCard(firstname, fathername, grandfathername,
                           familyname, wifename, city, directorate, street)
            f.PrintCard()
            OprationMethodsFamilyCard.updateOneCard(f, index)
        elif noOpration == 3:
            OprationMethodsFamilyCard.reviewAllCard()

            index = int(input("Enter index user delet Card : "))

            OprationMethodsFamilyCard.deleteOneCard(index)
        elif noOpration == 4:
            OprationMethodsFamilyCard.reviewAllCard()

    elif noTypeInput == 3:
        print("""
        Welcome To death certificate services System
                    Enter number (1) For Add
                    Enter number (2) For Update
                    Enter number (3) For Delete
                    Enter number (4) For Review


        """)
        noOpration = int(input("Enter No : "))

        if noOpration == 1:

            firstname = str(input("Enter first name :"))
            fathername = str(input("Enter father name :"))
            grandfathername = str(input("Enter grandfather name :"))
            familyname = str(input("Enter family name :"))
            # bloodtype = str(input("Enter blood type :"))
            # gender = str(input("Enter gender :"))
            mothername = str(input("Enter the mother name :"))
            IC_ID = str(input("Enter Identification Card ID :"))
            datedeath = str(input("Enter date death :"))
            socialstatus = str(input("Enter social status :"))
            placedath = str(input("Enter place death:"))
            d = DeathCertificate(firstname, fathername,
                                 grandfathername, familyname, mothername, IC_ID,
                                 datedeath, placedath, socialstatus)
            d.PrintCard()
            OprationMethodsDeathCertificate.saveNewCard(d)
        elif noOpration == 2:
            OprationMethodsDeathCertificate.reviewAllCard()
            index = int(input("Enter index user updata data : "))
            firstname = str(input("Enter first name :"))
            fathername = str(input("Enter father name :"))
            grandfathername = str(input("Enter grandfather name :"))
            familyname = str(input("Enter family name :"))
            # bloodtype = str(input("Enter blood type :"))
            # gender = str(input("Enter gender :"))
            mothername = str(input("Enter the mother name :"))
            IC_ID = str(input("Enter Identification Card ID :"))
            datedeath = str(input("Enter date death :"))
            socialstatus = str(input("Enter social status :"))
            placedath = str(input("Enter place death:"))
            d = DeathCertificate(firstname, fathername,
                                 grandfathername, familyname, mothername, IC_ID,
                                 datedeath, placedath, socialstatus)
            d.PrintCard()
            OprationMethodsDeathCertificate.updateOneCard(d, index)
        elif noOpration == 3:
            OprationMethodsDeathCertificate.reviewAllCard()

            index = int(input("Enter index user delet Card : "))

            OprationMethodsDeathCertificate.deleteOneCard(index)
        elif noOpration == 4:
            OprationMethodsDeathCertificate.reviewAllCard()
    elif noTypeInput == 4:
        print("""
        Welcome To birth certificate services System
                    Enter number (1) For Add
                    Enter number (2) For Update
                    Enter number (3) For Delete
                    Enter number (4) For Review


        """)
        noOpration = int(input("Enter No : "))

        if noOpration == 1:

            firstname = str(input("Enter first name :"))
            fathername = str(input("Enter father name :"))
            grandfathername = str(input("Enter grandfather name :"))
            familyname = str(input("Enter family name :"))
            mothername = str(input("Enter mother name :"))
            motherID = str(input("Enter the mother Identification Card ID :"))
            fatherID = str(input("Enter the father Identification Card ID :"))
            d = BirthCertificate(firstname, fathername,
                                 grandfathername, familyname, mothername, fatherID,
                                 motherID)
            d.PrintCard()
            OprationMethodsBirthCertificate.saveNewCard(d)
        elif noOpration == 2:
            OprationMethodsBirthCertificate.reviewAllCard()
            index = int(input("Enter index user updata data : "))
            OprationMethodsBirthCertificate.updateOneCard(d, index)
        elif noOpration == 3:
            OprationMethodsBirthCertificate.reviewAllCard()

            index = int(input("Enter index user delet Card : "))

            OprationMethodsBirthCertificate.deleteOneCard(index)
        elif noOpration == 4:
            OprationMethodsBirthCertificate.reviewAllCard()


def CheckTypeCard(noTypeInput):
    # print("""
    #        Welcome To The civil Statuse System
    #     """)
    if noTypeInput == 1:
        print("""
        ***** Welcome to the Civil Status Cards Service *****
        Enter number (1) to request an ID card
        Enter number (2) to request a family card
        Enter number (3) to request a death certificate
        Enter number (4) to request a birth certificate
        Enter char   (E) or (e) For Exit


        """)
        noTypeInputssss = int(input("Enter No : "))
        CheckTypeCivilServicessCard(noTypeInputssss)

    if noTypeInput == 2:
        print("""
        Welcome To birth Military Card services System
        Enter number (1) to request a Military card
        Enter number (2) to request a Private card
        """)
        noMilitaryTypeInput = int(input("Enter No : "))
        CheckTypeMilitarylServicessCard(noMilitaryTypeInput)


def Welcome():
    print('''
    *********** Welcome To The civil Statuse System *****
    ''')

    print("""
        ***** Welcome to the Civil Status Cards Service *****
        Enter number (1) to request a civil card
        Enter number (2) to request a military card



        """)
    noTypeInputs = int(input("Enter no type card: "))
    CheckTypeCard(noTypeInputs)


# if __name__ == "__main__":
#     for i in data:
#         print(i, data[i])

while True:

    print("""
        ***** Welcome to the Civil Status Cards Service *****
        Enter number (1) to ingress System
        Enter number (2) to Exit



        """)
    ingressType = int(input("Enter no type card: "))

    if ingressType == 1:
        Welcome()
    else:
        break
