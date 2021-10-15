IdentificationCardList = []
# قائمة لحفظ البطائق العائلية
FamilyCardList = []
# قائمة لحفظ البطائق العسكرية

MilitaryCardList = []
# قائمة لحفظ البطائق الخاصة

PrivateCardList = []
# قائمة لحفظ يطائق الوفاة
DeathCertificateList = []
# قائمة لحفظ يطائق الوفاة

BirthCertificateList = []

# كلاس  عمليات الحفظ والتعديل والاضافة للبطائق الشخصية


class OprationMethodsIdentificationCard:

    #IdentificationCardList = []

    @staticmethod
    def reviewAllCard():
        print("Index", "Data User")
        for i in range(len(IdentificationCardList)):
            print(i, "    {0}".format(IdentificationCardList[i]))

    @staticmethod
    def deleteOneCard(index):
        IdentificationCardList.pop(index)

    @staticmethod
    def updateOneCard(self, index):
        IdentificationCardList[index] = {
            "ID": self.ID,
            "firstname": self.firstname,
            "fathername": self.fathername,
            "grandfathername": self.grandfathername,
            "familyname": self.familyname,
            "datebirth": self.datebirth,
            "gender": self.gender,
            "placebirth": self.placebirth,
            "bloodtype": self.bloodtype,
            "release": self.releasedate,
            "expiry": self.expirydate,

        }
        print("Done Update Data")

    @staticmethod
    def saveNewCard(self):
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

# كلاس عمليات الحفظ والتعديل والاضافة للبطائق العائلية


class OprationMethodsFamilyCard:
    @staticmethod
    def saveNewCard(self):
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
        print("Index", "Data User")
        for i in range(len(FamilyCardList)):
            print(i, "    {0}".format(FamilyCardList[i]))

    @staticmethod
    def deleteOneCard(index):
        FamilyCardList.pop(index)

    @staticmethod
    def updateOneCard(self, index):
        FamilyCardList[index] = {
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
        print("Done Update Data")

# كلاس عمليات الحفظ والتعديل والاضافة لبطائق الوفاة


class OprationMethodsDeathCertificate:
    @staticmethod
    def saveNewCard(self):
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
        print("Index", "Data User")
        for i in range(len(DeathCertificateList)):
            print(i, "    {0}".format(DeathCertificateList[i]))

    @staticmethod
    def deleteOneCard(index):
        DeathCertificateList.pop(index)
        print("Done Delete Card")

    @staticmethod
    def updateOneCard(self, index):
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
    @staticmethod
    def saveNewCard(self):
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
        print("Index", "Data User")
        for i in range(len(BirthCertificateList)):
            print(i, "    {0}".format(BirthCertificateList[i]))

    @staticmethod
    def deleteOneCard(index):
        BirthCertificateList.pop(index)
        print("Done Delete Card")

    @staticmethod
    def updateOneCard(self, index):
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
        print("Index", "Data User")
        for i in range(len(PrivateCardList)):
            print(i, "    {0}".format(PrivateCardList[i]))

    @staticmethod
    def deleteOneCard(index):
        PrivateCardList.pop(index)
        print("Done Delete Card")

    @staticmethod
    def updateOneCard(self, index):
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
    def saveNewCard(self):
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
        print("Index", "Data User")
        for i in range(len(MilitaryCardList)):
            print(i, "    {0}".format(MilitaryCardList[i]))

    @staticmethod
    def deleteOneCard(index):
        MilitaryCardList.pop(index)
        print("Done Delete Card")

    @staticmethod
    def updateOneCard(self, index):
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
