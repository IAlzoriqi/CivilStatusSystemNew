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


#  كلاس  عمليات الحفظ والتعديل والاضافة للبطائق الشخصية


class OprationMethodsIdentificationCard:

    # IdentificationCardList = []
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
    def updateOneCard(self, index):
        '''
        دالة تعديل بطاقة من قائمة البطائق الشخصية عن طريق الاندكس
        الدالة ستاتيك لذالك تستدعى بدون انشاء اوبجكت
        '''
        IdentificationCardList[index] = {
            "ID": self.ID,  # تعديل الرقم الوطني
            "firstname": self.firstname,  # تعديل الاسم الاول
            "fathername": self.fathername,  # تعديل اسم اللأب
            "grandfathername": self.grandfathername,  # تعديل اسم الجد
            "familyname": self.familyname,  # تعديل اسم العائلة
            "datebirth": self.datebirth,  # تعديل تاريخ الميلاد
            "gender": self.gender,  # تعديل الجنس
            "placebirth": self.placebirth,  # تعديل تاريخ الميلاد
            "bloodtype": self.bloodtype,  # تعديل نوع الدم
            "release": self.releasedate,  # تعديل تاريخ الاصدار
            "expiry": self.expirydate,  # تعديل تاريخ الانتهاء

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
                "ID":    self.ID,
                "firstname":    self.firstname,
                "fathername":    self.fathername,
                "grandfathername":    self.grandfathername,
                "familyname": self.familyname,
                "datebirth": self.datebirth,
                "gender": self.gender,
                "placebirth": self.placebirth,
                "bloodtype": self.bloodtype,
                "release": self.releasedate,
                "expiry": self.expirydate,

            }
        )
        print("Done Save")


class OprationMethodsFamilyCard:

    '''
    كلاس عمليات الحفظ والتعديل والاضافة للبطائق العائلية
    '''

    @staticmethod
    def saveNewCard(self):
        '''
        دالة حفظ بطاقة عائلية جديدة  
        الدالة ستاتيك لذالك تستدعى بدون انشاء اوبجكت

        '''
        FamilyCardList.append(
            {
                "ID": self.ID,
                "firstname": self.firstname,
                "fathername": self.fathername,
                "grandfathername": self.grandfathername,
                "familyname": self.familyname,
                "wifename": self.wifename,
                "city": self.city,
                "directorate": self.directorate,
                "street": self.street,
                "releasedate": self.releasedate,

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
    def updateOneCard(self, index):
        '''
        دالة تعديل بطاقة من قائمة البطائق العائلية عن طريق الاندكس
        الدالة ستاتيك لذالك تستدعى بدون انشاء اوبجكت
        '''
        FamilyCardList[index] = {
            "ID": self.ID,  # تعديل الرقم الوطني
            "firstname": self.firstname,
            "fathername": self.fathername,
            "grandfathername": self.grandfathername,
            "familyname": self.familyname,
            "wifename": self.wifename,
            "city": self.city,
            "directorate": self.directorate,
            "street": self.street,
            "releasedate": self.releasedate,

        }
        print("Done Update Data")


class OprationMethodsDeathCertificate:
    """
     كلاس عمليات الحفظ والتعديل والاضافة لبطائق الوفاة

    """

    @staticmethod
    def saveNewCard(self):
        '''
        دالة حفظ  بطاقة جديدة  لقائمة  بطائق الوفة
        الدالة ستاتيك لذالك تستدعى بدون انشاء اوبجكت

        '''
        DeathCertificateList.append(
            {



                "ID": self.ID,
                "firstname": self.firstname,
                "fathername": self.fathername,
                "grandfathername": self.grandfathername,
                "familyname": self.familyname,
                "mothername": self.mothername,
                "IC_ID": self.IC_ID,
                "datedeath": self.datedeath,
                "placedath": self.placedath,
                "releasedate": self.releasedate,

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
    def updateOneCard(self, index):
        '''
        دالة تعديل بطاقة من قائمة بطائق الوفاة عن طريق الاندكس
        الدالة ستاتيك لذالك تستدعى بدون انشاء اوبجكت
        '''
        DeathCertificateList[index] = {

            "ID": self.ID,
            "firstname": self.firstname,
            "fathername": self.fathername,
            "grandfathername": self.grandfathername,
            "familyname": self.familyname,
            "mothername": self.mothername,
            "IC_ID": self.IC_ID,
            "datedeath": self.datedeath,
            "placedath": self.placedath,
            "releasedate": self.releasedate,

        }
        print("Done Update Data")

# كلاس عمليات الحفظ والتعديل والاضافة لبطائق الميلاد


class OprationMethodsBirthCertificate:
    """
     كلاس عمليات الحفظ والتعديل والاضافة لبطائق الميلاد

    """
    @staticmethod
    def saveNewCard(self):
        '''
        دالة حفظ بطاقة ميلاد جديدة  
        الدالة ستاتيك لذالك تستدعى بدون انشاء اوبجكت

        '''
        BirthCertificateList.append(
            {



                "ID": self.ID,
                "firstname": self.firstname,
                "fathername": self.fathername,
                "grandfathername": self.grandfathername,
                "familyname": self.familyname,
                "mothername": self.mothername,
                "motherID": self.motherID,
                "fatherID": self.fatherID,

                "releasedate": self.releasedate,

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
    def updateOneCard(self, index):
        '''
        دالة تعديل بطاقة من قائمة بطائق الميلاد عن طريق الاندكس
        الدالة ستاتيك لذالك تستدعى بدون انشاء اوبجكت
        '''
        BirthCertificateList[index] = {


            "ID": self.ID,
            "firstname": self.firstname,
            "fathername": self.fathername,
            "grandfathername": self.grandfathername,
            "familyname": self.familyname,
            "mothername": self.mothername,
            "motherID": self.motherID,
            "fatherID": self.fatherID,

            "releasedate": self.releasedate,

        }
        print("Done Update Data")

# كلاس عمليات الحفظ والتعديل والاضافة لبطائق الخاصة


class OprationMethodsPrivateCard:
    @staticmethod
    def saveNewCard(self):
        PrivateCardList.append(
            {



                "ID": self.ID,
                "firstname": self.firstname,
                "fathername": self.fathername,
                "grandfathername": self.grandfathername,
                "familyname": self.familyname,
                "place": self.place,
                "releasedate": self.releasedate,

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
    def updateOneCard(self, index):
        '''
        دالة تعديل بطاقة من قائمة البطائق الخاصة عن طريق الاندكس
        الدالة ستاتيك لذالك تستدعى بدون انشاء اوبجكت
        '''
        PrivateCardList[index] = {





            "ID": self.ID,
            "firstname": self.firstname,
            "fathername": self.fathername,
            "grandfathername": self.grandfathername,
            "familyname": self.familyname,
            "place": self.place,
            "releasedate": self.releasedate,


        }
        print("Done Update Data")

# كلاس عمليات الحفظ والتعديل والاضافة لبطائق العسكرية


class OprationMethodsMilitaryCard:
    @staticmethod
    def saveNewCard(MethodsMilitary):
        MilitaryCardList.append(
            {



                "ID": self.ID,
                "firstname": self.firstname,
                "fathername": self.fathername,
                "grandfathername": self.grandfathername,
                "familyname": self.familyname,
                "releasedate": self.releasedate,
                "expirydate": self.expirydate

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
    def updateOneCard(self, index):
        '''
        دالة تعديل بطاقة من قائمة البطائق العسكرية عن طريق الاندكس
        الدالة ستاتيك لذالك تستدعى بدون انشاء اوبجكت
        '''
        MilitaryCardList[index] = {





            "ID": self.ID,
            "firstname": self.firstname,
            "fathername": self.fathername,
            "grandfathername": self.grandfathername,
            "familyname": self.familyname,
            "releasedate": self.releasedate,
            "expirydate": self.expirydate


        }
        print("Done Update Data")
