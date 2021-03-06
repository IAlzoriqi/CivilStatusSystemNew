from IdentificationCardModel import IdentificationCard
from FamilyCardModel import FamilyCard
from BirthCertificate import BirthCertificate
from DeathCertificate import DeathCertificate
from PrivateCard import PrivateCard
from MilitaryCard import MilitaryCard

from oprationListMethods import *


def CheckTypeMilitarylServicessCard(noTypeInput):
    """
    دالة التحقق من نوع البطائق العسكرية
    """
    if noTypeInput == 2:  # التحقق من القيمة المدخلة بتوع البطاقة الشخصية

        # طبتعة التعليمات
        print("""
        Welcome To birth Private Card services System
                    Enter number (1) For Add
                    Enter number (2) For Update
                    Enter number (3) For Delete
                    Enter number (4) For Review


        """)
        noOpration = int(input("Enter No : "))  # ادخال قيمة العملية

        if noOpration == 1:  # التحقق من قيمة العملية اذا كانت واحد يعني حفظ بطاقة جديدة
            firstname = str(input("Enter first name :"))  # ادخال اسم الاول
            fathername = str(input("Enter father name :"))  # ادخال اسم الاب
            grandfathername = str(
                input("Enter grandfather name :"))  # ادخال اسم الجد
            familyname = str(input("Enter family name :"))  # ادخال اسم العائلة
            place = str(input("Enter place  :"))  # ادخال المكان

            m = PrivateCard(firstname, fathername,
                            grandfathername, familyname, place)  # أنشاء كائن من كلاس البطائق الخاصة  واسناد اليم المدخله لها

            m.PrintCard()  # استداء دالة طباقة البطاقة الجديدة

            #  استداء دالة حفظ البطاقة الى قائمة البطائق الخاصة
            OprationMethodsPrivateCard.saveNewCard(m)

        elif noOpration == 2:

            # print(data[0]["IdentificationCard"])

            OprationMethodsPrivateCard.reviewAllCard()  # استدعاء دالة عرض كل البطائق الخاصة
            index = int(input("Enter index user updata data : "))

            firstname = str(input("Enter first name :"))
            fathername = str(input("Enter father name :"))
            grandfathername = str(input("Enter grandfather name :"))
            familyname = str(input("Enter family name :"))
            place = str(input("Enter place  :"))

            m = PrivateCard(firstname, fathername,
                            grandfathername, familyname, place)
            m.PrintCard()
            '''
             استداء دالة تعديل البيانات  البطاقة من  قائمة البطائق الخاصة 
              عن طريق الاندكس المدخل من قبل المستخدم

            '''

            OprationMethodsPrivateCard.updateOneCard(p, index)

        elif noOpration == 3:

            OprationMethodsPrivateCard.reviewAllCard()  # استدعاء دالة عرض كل البطائق الخاصة

            index = int(input("Enter index user delet Card : "))

            OprationMethodsPrivateCard.deleteOneCard(
                index)  # استدعاء دالة حذف بطاقة خاصة

        elif noOpration == 4:

            OprationMethodsPrivateCard.reviewAllCard()  # استدعاء دالة عرض كل البطائق الخاصة

    elif noTypeInput == 1:
        print("""
        Welcome To birth Private Card services System
                    Enter number (1) For Add
                    Enter number (2) For Update
                    Enter number (3) For Delete
                    Enter number (4) For Review


        """)
        noOpration = int(input("Enter No : "))  # ادخال قيمة العملية

        if noOpration == 1:
            firstname = str(input("Enter first name :"))
            fathername = str(input("Enter father name :"))
            grandfathername = str(input("Enter grandfather name :"))
            familyname = str(input("Enter family name :"))
            side = str(input("Enter side  :"))

            m = MilitaryCard(firstname, fathername,
                             grandfathername, familyname, side)
            m.PrintCard()
            #  استداء دالة حفظ البطاقة الى قائمة البطائق العسكرية
            OprationMethodsMilitaryCard.saveNewCard(m)
        elif noOpration == 2:

            # print(data[0]["IdentificationCard"])

            # استدعاء دالة عرض كل البطائق العسكرية
            OprationMethodsMilitaryCard.reviewAllCard()
            index = int(input("Enter index user updata data : "))

            firstname = str(input("Enter first name :"))
            fathername = str(input("Enter father name :"))
            grandfathername = str(input("Enter grandfather name :"))
            familyname = str(input("Enter family name :"))
            side = str(input("Enter side  :"))

            m = MilitaryCard(firstname, fathername,
                             grandfathername, familyname, side)
            m.PrintCard()
            #  استداء دالة تعديل البيانات  البطاقة من  قائمة البطائق العسكرية  عن طريق الاندكس المدخل من قبل المستخدم
            '''
             استداء دالة تعديل البيانات  البطاقة من  قائمة البطائق العسكرية 
              عن طريق الاندكس المدخل من قبل المستخدم

            '''
            OprationMethodsMilitaryCard.updateOneCard(m, index)

        elif noOpration == 3:

            # استدعاء دالة عرض كل البطائق العسكرية
            OprationMethodsMilitaryCard.reviewAllCard()

            index = int(input("Enter index user delet Card : "))

            OprationMethodsMilitaryCard.deleteOneCard(
                index)  # استدعاء دالة حذف بطاقة عسكرية

        elif noOpration == 4:
            # استدعاء دالة عرض كل البطائق الخاصة
            OprationMethodsMilitaryCard.reviewAllCard()


def CheckTypeCivilServicessCard(noTypeInput):
    if noTypeInput == 1:
        print("""
        *****       Welcome  To personal card services system  *****
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
            #  استداء دالة حفظ البطاقة الى قائمة البطائق الشخصية
            OprationMethodsIdentificationCard.saveNewCard(p)

        elif noOpration == 2:

            # استدعاء دالة عرض كل البطائق الشخصية
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
            #  استداء دالة تعديل البيانات  البطاقة من  قائمة البطائق الشخصية  عن طريق الاندكس المدخل من قبل المستخدم
            '''
             استداء دالة تعديل البيانات  البطاقة من  قائمة البطائق الشخصية 
              عن طريق الاندكس المدخل من قبل المستخدم

            '''
            OprationMethodsIdentificationCard.updateOneCard(p, index)
        elif noOpration == 3:

            # استدعاء دالة عرض كل البطائق الشخصية
            OprationMethodsIdentificationCard.reviewAllCard()

            index = int(input("Enter index user delet Card : "))

            OprationMethodsIdentificationCard.deleteOneCard(
                index)  # استدعاء دالة حذف بطاقة شخصية

        elif noOpration == 4:

            # استدعاء دالة عرض كل البطائق الشخصية
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
            #  استداء دالة حفظ البطاقة الى قائمة البطائق العائلية
            OprationMethodsFamilyCard.saveNewCard(f)
        elif noOpration == 2:
            # استدعاء دالة عرض كل البطائق العائلية
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
            '''
             استداء دالة تعديل البيانات  البطاقة من  قائمة البطائق العائلية 
              عن طريق الاندكس المدخل من قبل المستخدم

            '''
            OprationMethodsFamilyCard.updateOneCard(f, index)
        elif noOpration == 3:
            # استدعاء دالة عرض كل البطائق العائلية
            OprationMethodsFamilyCard.reviewAllCard()

            index = int(input("Enter index user delet Card : "))

            OprationMethodsFamilyCard.deleteOneCard(
                index)  # استدعاء دالة حذف بطاقة عائلية
        elif noOpration == 4:
            # استدعاء دالة عرض كل البطائق العائلية
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
            #  استداء دالة حفظ البطاقة الى قائمة بطائق الوفاة
            OprationMethodsDeathCertificate.saveNewCard(d)
        elif noOpration == 2:
            # استدعاء دالة عرض كل بطائق الوفاة
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
            '''
             استداء دالة تعديل البيانات  البطاقة من  قائمة شهائد الوفاة 
              عن طريق الاندكس المدخل من قبل المستخدم

            '''
            OprationMethodsDeathCertificate.updateOneCard(d, index)
        elif noOpration == 3:
            # استدعاء دالة عرض كل بطائق الوفاة
            OprationMethodsDeathCertificate.reviewAllCard()

            index = int(input("Enter index user delet Card : "))

            OprationMethodsDeathCertificate.deleteOneCard(
                index)  # استدعاء دالة حذف شهادو  وفاة
        elif noOpration == 4:
            # استدعاء دالة عرض كل بطائق الوفاة
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
            #  استداء دالة حفظ البطاقة الى قائمة شهادة الميلاد
            OprationMethodsBirthCertificate.saveNewCard(d)
        elif noOpration == 2:
            # استدعاء دالة عرض كل شهادة الميلاد
            OprationMethodsBirthCertificate.reviewAllCard()

            index = int(input("Enter index user updata data : "))
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
            '''
             استداء دالة تعديل البيانات  البطاقة من  قائمة شهائد الميلاد 
              عن طريق الاندكس المدخل من قبل المستخدم

            '''
            OprationMethodsBirthCertificate.updateOneCard(d, index)
        elif noOpration == 3:
            # استدعاء دالة عرض كل بطائق الميلاد
            OprationMethodsBirthCertificate.reviewAllCard()

            index = int(input("Enter index user delet Card : "))

            OprationMethodsBirthCertificate.deleteOneCard(
                index)  # استدعاء دالة حذف شهادة ميلاد
        elif noOpration == 4:
            # استدعاء دالة عرض كل بطائق الميلاد
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
    # استدعاء الدالة ويلكم وهي تعتبر الدالة الرئيسية  والتي يبداء النظام منها
    CheckTypeCard(noTypeInputs)



if __name__== "__main__":
    while True:  # دوارة لاتاحت الاضافة والتعديل والحذف وعدم الخروج من النظام بسبب التنفيذ لأول مره

        print("""
            ***** Welcome to the Civil Status Cards Service *****
            Enter number (1) to ingress System
            Enter number (2) to Exit



            """)

        # ادخال رقم لتحقق من الدخول لنظام او الخروج منه
        ingressType = int(input("Enter no : "))

        if ingressType == 1:  # التحقق من الرقم المدخل
            Welcome()  # استدعاء الدالة ويلكم وهي تعتبر الدالة الرئيسية  والتي يبداء النظام منها
        else:
            break
