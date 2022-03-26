import hashlib

class User(object):
    def __init__(self):
        self.username = ""
        self.ID = ""
        self.stamp = ""

    def Encrypted_Stamp(self, usrname, idNumber, encrypt_Stamp):
        if self.is_Number(idNumber):
            m = hashlib.md5()
            n = hashlib.md5()
            for s in usrname:
                for s2 in encrypt_Stamp:
                    m.update(s.encode())
                    n.update(s2.encode())
            encrypted_Name = m.hexdigest()
            encrypted_Stamp = n.hexdigest()
            self.username = encrypted_Name
            self.stamp = encrypted_Stamp
            self.Caesar_Cipher(idNumber)

    def get_details(self):
        print("\nEncrypted username: {0}"
              "\nEcrypted ID Number: {1}"
              "\nEncrypted signature: {2}"
              .format(self.username, self.ID, self.stamp))

    def Caesar_Cipher(self, idNumber):
        alphabet_Num = '0123456789'
        key = 5
        for i in idNumber:
            post = alphabet_Num.find(i)
            newpost = (post + key) % 10  # 10%10=0
            self.ID += alphabet_Num[newpost]

    def is_Number(self, IDinput_check):
        for i in range(len(IDinput_check)):
            if not IDinput_check[i].isdigit():
                print("Error - ID Number value is Not integer")
                return exit()
        return True

    def __del__(self):
        print("\n**************************")
        print("*  Encryption completed  *")
        print("**************************")
