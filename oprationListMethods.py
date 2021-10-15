IdentificationCardList = []
# قائمة لحفظ البطائق العائلية
FamilyCardList = []
# قائمة لحفظ البطائق العسكرية

MilitaryCardList = []
# قائمة لحفظ البطائق الخاصة

PrivateCardList = []
# قائمة لحفظ يطائق الوفاة
DeathCertificateList = []
# قائمة لحفظ يطائق الميلاد

BirthCertificateList = []


class OprationMethodsIdentificationCard:

    '''
    كلاس  عمليات الحفظ والتعديل والاضافة للبطائق الشخصية
    '''

    @staticmethod
    def reviewAllCard():
        '''
        دالة طباعة كل البطائق الشخصية مع الاندكس

        '''

        print("Index", "Data User")
        # دوارة على طول البيانات المحفوظة في قائمة البطائق الشخصية
        for i in range(len(IdentificationCardList)):
            # طباعة الاندكس والبيانات
            print(i, "    {0}".format(IdentificationCardList[i]))

    @staticmethod
    def deleteOneCard(index):
        '''
        دالة حذف بطاقة من قائمة البطائق الشخصية عن طريق الاندكس
        الدالة ستاتيك لذالك تستدعى بدون انشاء اوبجكت

        '''
        IdentificationCardList.pop(index)

    @staticmethod
    def updateOneCard(IdentificationCard, index):
        '''
        دالة تعديل بطاقة من قائمة البطائق الشخصية عن طريق الاندكس
        الدالة ستاتيك لذالك تستدعى بدون انشاء اوبجكت
        '''
        IdentificationCardList[index] = {
            "ID": IdentificationCard.ID,  # تعديل الرقم الوطني
            "firstname": IdentificationCard.firstname,  # تعديل الاسم الاول
            "fathername": IdentificationCard.fathername,  # تعديل اسم اللأب
            "grandfathername": IdentificationCard.grandfathername,  # تعديل اسم الجد
            "familyname": IdentificationCard.familyname,  # تعديل اسم العائلة
            "datebirth": IdentificationCard.datebirth,  # تعديل تاريخ الميلاد
            "gender": IdentificationCard.gender,  # تعديل الجنس
            "placebirth": IdentificationCard.placebirth,  # تعديل تاريخ الميلاد
            "bloodtype": IdentificationCard.bloodtype,  # تعديل نوع الدم
            "release": IdentificationCard.releasedate,  # تعديل تاريخ الاصدار
            "expiry": IdentificationCard.expirydate,  # تعديل تاريخ الانتهاء

        }
        print("Done Update Data")

    @staticmethod
    def saveNewCard(IdentificationCard):
        '''
        دالة اضافة بطاقة شخصية جديدة الى قائمة البطائق الشخصية عن طريق الاندكس
        الدالة ستاتيك لذالك تستدعى بدون انشاء اوبجكت
        '''

        IdentificationCardList.append(
            {
                "ID":    IdentificationCard.ID,
                "firstname":    IdentificationCard.firstname,
                "fathername":    IdentificationCard.fathername,
                "grandfathername":    IdentificationCard.grandfathername,
                "familyname": IdentificationCard.familyname,
                "datebirth": IdentificationCard.datebirth,
                "gender": IdentificationCard.gender,
                "placebirth": IdentificationCard.placebirth,
                "bloodtype": IdentificationCard.bloodtype,
                "release": IdentificationCard.releasedate,
                "expiry": IdentificationCard.expirydate,

            }
        )
        print("Done Save")


class OprationMethodsFamilyCard:

    '''
    كلاس عمليات الحفظ والتعديل والاضافة للبطائق العائلية
    '''

    @staticmethod
    def saveNewCard(FamilyCard):
        '''
        دالة حفظ بطاقة عائلية جديدة  
        الدالة ستاتيك لذالك تستدعى بدون انشاء اوبجكت

        '''
        FamilyCardList.append(
            {
                "ID": FamilyCard.ID,
                "firstname": FamilyCard.firstname,
                "fathername": FamilyCard.fathername,
                "grandfathername": FamilyCard.grandfathername,
                "familyname": FamilyCard.familyname,
                "wifename": FamilyCard.wifename,
                "city": FamilyCard.city,
                "directorate": FamilyCard.directorate,
                "street": FamilyCard.street,
                "releasedate": FamilyCard.releasedate,

            }
        )
        print("Done Save")

    @staticmethod
    def reviewAllCard():
        '''
        دالة طباعة كل البطائق العائلية مع الاندكس
        الدالة ستاتيك لذالك تستدعى بدون انشاء اوبجكت

        '''
        print("Index", "Data User")
        # دوارة على طول البيانات المحفوظة في قائمة البطائق الشخصية
        for i in range(len(FamilyCardList)):
            # طباعة الاندكس والبيانات
            print(i, "    {0}".format(FamilyCardList[i]))

    @staticmethod
    def deleteOneCard(index):
        '''
        دالة حذف بطاقة من قائمة البطائق العائلية عن طريق الاندكس
        الدالة ستاتيك لذالك تستدعى بدون انشاء اوبجكت
        '''
        FamilyCardList.pop(index)

    @staticmethod
    def updateOneCard(FamilyCard, index):
        '''
        دالة تعديل بطاقة من قائمة البطائق العائلية عن طريق الاندكس
        الدالة ستاتيك لذالك تستدعى بدون انشاء اوبجكت
        '''
        FamilyCardList[index] = {
            "ID": FamilyCard.ID,
            "firstname": FamilyCard.firstname,
            "fathername": FamilyCard.fathername,
            "grandfathername": FamilyCard.grandfathername,
            "familyname": FamilyCard.familyname,
            "wifename": FamilyCard.wifename,
            "city": FamilyCard.city,
            "directorate": FamilyCard.directorate,
            "street": FamilyCard.street,
            "releasedate": FamilyCard.releasedate,
        }
        print("Done Update Data")


class OprationMethodsDeathCertificate:
    """
     كلاس عمليات الحفظ والتعديل والاضافة لبطائق الوفاة

    """

    @staticmethod
    def saveNewCard(DeathCertificate):
        '''
        دالة حفظ  بطاقة جديدة  لقائمة  بطائق الوفة
        الدالة ستاتيك لذالك تستدعى بدون انشاء اوبجكت

        '''
        DeathCertificateList.append(
            {



                "ID": DeathCertificate.ID,
                "firstname": DeathCertificate.firstname,
                "fathername": DeathCertificate.fathername,
                "grandfathername": DeathCertificate.grandfathername,
                "familyname": DeathCertificate.familyname,
                "mothername": DeathCertificate.mothername,
                "IC_ID": DeathCertificate.IC_ID,
                "datedeath": DeathCertificate.datedeath,
                "placedath": DeathCertificate.placedath,
                "releasedate": DeathCertificate.releasedate,

            }
        )
        print("Done Save")

    @staticmethod
    def reviewAllCard():
        '''
        دالة عرض وطياعة  كل البطائق  المحفوظة من سابق  في قائمة بطائق الوفاة
        الدالة ستاتيك لذالك تستدعى بدون انشاء اوبجكت

        '''
        print("Index", "Data User")
        # دوارة على طول البيانات المحفوظة في قائمة البطائق الوفاة
        for i in range(len(DeathCertificateList)):
            # طباعة الاندكس والبيانات
            print(i, "    {0}".format(DeathCertificateList[i]))

    @staticmethod
    def deleteOneCard(index):
        '''
        دالة حذف بطاقة من قائمة بطائق الوفاة عن طريق الاندكس
        الدالة ستاتيك لذالك تستدعى بدون انشاء اوبجكت
        '''
        DeathCertificateList.pop(index)
        print("Done Delete Card")

    @staticmethod
    def updateOneCard(DeathCertificate, index):
        '''
        دالة تعديل بطاقة من قائمة بطائق الوفاة عن طريق الاندكس
        الدالة ستاتيك لذالك تستدعى بدون انشاء اوبجكت
        '''
        DeathCertificateList[index] = {

            "ID": DeathCertificate.ID,
            "firstname": DeathCertificate.firstname,
            "fathername": DeathCertificate.fathername,
            "grandfathername": DeathCertificate.grandfathername,
            "familyname": DeathCertificate.familyname,
            "mothername": DeathCertificate.mothername,
            "IC_ID": DeathCertificate.IC_ID,
            "datedeath": DeathCertificate.datedeath,
            "placedath": DeathCertificate.placedath,
            "releasedate": DeathCertificate.releasedate,


        }
        print("Done Update Data")

# كلاس عمليات الحفظ والتعديل والاضافة لبطائق الميلاد


class OprationMethodsBirthCertificate:
    """
     كلاس عمليات الحفظ والتعديل والاضافة لبطائق الميلاد

    """
    @staticmethod
    def saveNewCard(BirthCertificate):
        '''
        دالة حفظ بطاقة ميلاد جديدة  
        الدالة ستاتيك لذالك تستدعى بدون انشاء اوبجكت

        '''
        BirthCertificateList.append(
            {



                "ID": BirthCertificate.ID,
                "firstname": BirthCertificate.firstname,
                "fathername": BirthCertificate.fathername,
                "grandfathername": BirthCertificate.grandfathername,
                "familyname": BirthCertificate.familyname,
                "mothername": BirthCertificate.mothername,
                "motherID": BirthCertificate.motherID,
                "fatherID": BirthCertificate.fatherID,

                "releasedate": BirthCertificate.releasedate,

            }
        )
        print("Done Save")

    @staticmethod
    def reviewAllCard():
        '''
        دالة طباعة البطائق المحفوظة من سابق في قائمة يطائق الوفاة   
        الدالة ستاتيك لذالك تستدعى بدون انشاء اوبجكت

        '''
        print("Index", "Data User")
        for i in range(len(BirthCertificateList)):
            print(i, "    {0}".format(BirthCertificateList[i]))

    @staticmethod
    def deleteOneCard(index):
        '''
        دالة حذف بطاقة من قائمة بطائق الميلاد عن طريق الاندكس
        الدالة ستاتيك لذالك تستدعى بدون انشاء اوبجكت

        '''
        BirthCertificateList.pop(index)
        print("Done Delete Card")

    @staticmethod
    def updateOneCard(BirthCertificate, index):
        '''
        دالة تعديل بطاقة من قائمة بطائق الميلاد عن طريق الاندكس
        الدالة ستاتيك لذالك تستدعى بدون انشاء اوبجكت
        '''
        BirthCertificateList[index] = {


            "ID": BirthCertificate.ID,
            "firstname": BirthCertificate.firstname,
            "fathername": BirthCertificate.fathername,
            "grandfathername": BirthCertificate.grandfathername,
            "familyname": BirthCertificate.familyname,
            "mothername": BirthCertificate.mothername,
            "motherID": BirthCertificate.motherID,
            "fatherID": BirthCertificate.fatherID,

            "releasedate": BirthCertificate.releasedate,

        }
        print("Done Update Data")


class OprationMethodsPrivateCard:

    '''
    كلاس عمليات الحفظ والتعديل والاضافة لبطائق الخاصة
    '''

    @staticmethod
    def saveNewCard(PrivateCard):
        '''
        دالة حفظ  بطاقة جديدة  لقائمة  بطائق الخاصة
        الدالة ستاتيك لذالك تستدعى بدون انشاء اوبجكت

        '''
        PrivateCardList.append(
            {



                "ID": PrivateCard.ID,
                "firstname": PrivateCard.firstname,
                "fathername": PrivateCard.fathername,
                "grandfathername": PrivateCard.grandfathername,
                "familyname": PrivateCard.familyname,
                "place": PrivateCard.place,
                "releasedate": PrivateCard.releasedate,

            }
        )
        print("Done Save")

    @staticmethod
    def reviewAllCard():
        '''
        دالة طباعة البطائق المحفوظة من سابق في قائمة البطائق الخاصة   
        الدالة ستاتيك لذالك تستدعى بدون انشاء اوبجكت
        '''
        print("Index", "Data User")
        for i in range(len(PrivateCardList)):
            print(i, "    {0}".format(PrivateCardList[i]))

    @staticmethod
    def deleteOneCard(index):
        '''
        دالة حذف بطاقة من قائمة البطائق الخاصة عن طريق الاندكس
        الدالة ستاتيك لذالك تستدعى بدون انشاء اوبجكت

        '''
        PrivateCardList.pop(index)
        print("Done Delete Card")

    @staticmethod
    def updateOneCard(PrivateCard, index):
        '''
        دالة تعديل بطاقة من قائمة البطائق الخاصة عن طريق الاندكس
        الدالة ستاتيك لذالك تستدعى بدون انشاء اوبجكت
        '''
        PrivateCardList[index] = {
            "ID": PrivateCard.ID,
            "firstname": PrivateCard.firstname,
            "fathername": PrivateCard.fathername,
            "grandfathername": PrivateCard.grandfathername,
            "familyname": PrivateCard.familyname,
            "place": PrivateCard.place,
            "releasedate": PrivateCard.releasedate,
            }
        print("Done Update Data")

# كلاس عمليات الحفظ والتعديل والاضافة لبطائق العسكرية


class OprationMethodsMilitaryCard:
    '''
    كلاس عمليات الحفظ والتعديل والاضافة لبطائق الخاصة
    '''

    @staticmethod
    def saveNewCard(MethodsMilitary):
        '''
        دالة حفظ  بطاقة جديدة  لقائمة  بطائق العسكرية
        الدالة ستاتيك لذالك تستدعى بدون انشاء اوبجكت

        '''
        MilitaryCardList.append(
            {
                "ID": MethodsMilitary.ID,
                "firstname": MethodsMilitary.firstname,
                "fathername": MethodsMilitary.fathername,
                "grandfathername": MethodsMilitary.grandfathername,
                "familyname": MethodsMilitary.familyname,
                "releasedate": MethodsMilitary.releasedate,
                "expirydate": MethodsMilitary.expirydate

            }
        )
        print("Done Save")

    @staticmethod
    def reviewAllCard():
        '''
        دالة طباعة البطائق المحفوظة من سابق في قائمة البطائق العسكرية   
        الدالة ستاتيك لذالك تستدعى بدون انشاء اوبجكت
        '''
        print("Index", "Data User")
        for i in range(len(MilitaryCardList)):
            print(i, "    {0}".format(MilitaryCardList[i]))

    @staticmethod
    def deleteOneCard(index):
        '''
        دالة حذف بطاقة من قائمة بطائق العسكرية عن طريق الاندكس
        الدالة ستاتيك لذالك تستدعى بدون انشاء اوبجكت

        '''
        MilitaryCardList.pop(index)
        print("Done Delete Card")

    @staticmethod
    def updateOneCard(MethodsMilitary, index):
        '''
        دالة تعديل بطاقة من قائمة البطائق العسكرية عن طريق الاندكس
        الدالة ستاتيك لذالك تستدعى بدون انشاء اوبجكت
        '''
        MilitaryCardList[index] = {





            "ID": MethodsMilitary.ID,
            "firstname": MethodsMilitary.firstname,
            "fathername": MethodsMilitary.fathername,
            "grandfathername": MethodsMilitary.grandfathername,
            "familyname": MethodsMilitary.familyname,
            "releasedate": MethodsMilitary.releasedate,
            "expirydate": MethodsMilitary.expirydate


        }
        print("Done Update Data")
