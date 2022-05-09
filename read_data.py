import firebase_admin
from firebase_admin import credentials, firestore

#Setup
cred = credentials.Certificate("key.json")
firebase_admin.initialize_app(cred)

db = firestore.client()


# Read data
# Getting a document with a known ID
"""result = db.collection('people').document("student").get()
if result.exists:
    print(result.to_dict())"""


# Get all documents in a collection
"""docs = db.collection("people").get()
for doc in docs:
    print(doc.to_dict())
"""


# Querying
# Equel
"""docs = db.collection("people").where("age", "==", 21).get()
for doc in docs:
    print(doc.to_dict())"""

# == != < > <= >=

"""docs = db.collection("people").where("social", "array_contains", "linkedin").get()
for doc in docs:
    print(doc.to_dict())
"""

"""docs = db.collection("people").where("address", "in", ["London", "Milan"]).get()
for doc in docs:
    print(doc.to_dict())"""













"""   self.clubData = []
   for i in self.db.collection("clubs").document(self.ClubKey).get():
      self.clubData.append(i.to_dict())

   for i in range(len(self.clubData)):
       self.ui.lblInfoClubTitle.setText(self.clubData[i]['clubName'])
       self.ui.textBrowseClubBody.append('<p style="font-size: 18px">' + self.clubData[i]["clubInfo"] + '</p>')
       self.ui.lblClubLeader.setText(self.clubData[i]['clubLeader'])"""


"""def addStudent(self):
    data = {
        "name": self.ui.StudentName.text().title(),
        "surName": self.ui.StudentSurname.text().title(),
        "email": self.ui.StudentEmail.text().lower(),
        "number": self.ui.studentNumber.text(),
        "department": self.ui.StudentDepartment.text().title(),
        "year": self.ui.StudentYear.text().title() + ". Sınıf",
        "userName": self.ui.StudentEmail.text().replace("@pru.edu.tr", ""),
        "clubs": "",
        "nameAndSurname": self.ui.StudentName.text().title() + " " + self.ui.StudentSurname.text().title()
    }
    docs = self.db.collection("students").where("email", "==", self.ui.StudentEmail.text()).get()
    control = False
    for doc in docs:
        take_data = doc.to_dict()
        control = True
    if control:
        QMessageBox.warning(self, "UYARI", "Bu öğrenci zaten kayıtlı!")
    else:
        try:
            if self.ui.StudentName.text() == "" or self.ui.StudentSurname.text() == "" or self.ui.StudentEmail.text() == "" or self.ui.studentNumber.text() == "" or self.ui.StudentDepartment.text() == "" or self.ui.StudentYear.text() == "":
                QMessageBox.warning(self, "UYARI", "Boş alan bırakamazsınız.")
            else:
                self.db.collection('students').add(data)
                self.clearStudent()
                self.listStudent()
                QMessageBox.information(self, "BİLGİ", "Kayıt başarılı!")
        except Exception as e:
            self.show_popup("KAYIT HATASI", "Beklenmedik bir hata oluştu: ", e)"""

"""    def login(self):
        email = self.ui.adminUsername.text()
        password = self.ui.adminPassword.text()
        self.control = False
        try:
            account = au.get_user_by_email(email)
            self.uid = account.uid
            print(self.uid)
            data = []
            result = self.db.collection("Person").document(self.uid).get()
            data = [result.to_dict()]
            print(data)
            for i in range(len(data)):
                self.rol = data[i]["rol"]
            print(self.rol)
            if self.rol == "Admin":
                try:
                    auth.sign_in_with_email_and_password(email, password)
                    self.control = True
                    if self.control:
                        try:
                            self.nextAdminWindow()
                        except:
                            QMessageBox.warning(self, "SAYFA GEÇİŞ", "Beklenmedik bir hata oluştu.")
                except:
                    QMessageBox.warning(self, "HATALI GİRİŞ", "Hatalı e-posta ya da parola")
                    self.ui.adminPassword.clear()
            else:
                QMessageBox.warning(self, "HATA", "Lütfen admin hesabı ile giriş yapınız.")
        except:
            QMessageBox.warning(self, "HATA", "Kullanıcı bulunamadı")
            
            
                def forgetPassword(self):
        try:
            userEmail = self.ui.emailAdress.text()
            auth.send_password_reset_email(userEmail)
            self.ui.loginPages.setCurrentWidget(self.ui.loginAdmin)
            QMessageBox.information(self, "ŞİFRE SIFIRLAMA", "Şifrenizi değiştirmek için e-postanızı kontrol ediniz.")
        except:
            QMessageBox.warning(self, "HATA", "E-posta bulunamadı.")""
"""