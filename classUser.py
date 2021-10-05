import hashlib

class User(object):
    def __init__(self):
        self.name = ""
        self.stamp = ""
        self.Id = ""

    def Encrypted_Stamp(self, encrypt_Name, encrypt_Stamp,ID):
        if self.is_Number(ID):
            m = hashlib.md5()
            n = hashlib.md5()
            for s in encrypt_Name:
                for s2 in encrypt_Stamp:
                    m.update(s.encode())
                    n.update(s2.encode())
            encrypted_Name = m.hexdigest()
            encrypted_Stamp = n.hexdigest()
            self.name = encrypted_Name
            self.stamp = encrypted_Stamp
            self.Caesar_Cipher(ID)

    def get_name(self):
        print("\nEncrypted Name: {0}\nEcrypted Id Number: {1}\nEncrypted signature: {2}".format(self.name, self.Id,self.stamp))
        # print("",)

    def Caesar_Cipher(self,idNumber):
        alphabet_Num = '0123456789'
        key = 5
        for i in idNumber:
            post = alphabet_Num.find(i)
            newpost = (post + key) % 10  # 10%10=0
            self.Id += alphabet_Num[newpost]

    def is_Number(self,IDinput_check):
        for i in range(len(IDinput_check)):
            if IDinput_check[i].isdigit() != True:
                print("Error - ID Number value is Not integer")
                return exit()
        return True

    def __del__(self):
        print("\n**************************")
        print("*  Encryption completed  *")
        print("**************************")
