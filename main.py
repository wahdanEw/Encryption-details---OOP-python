from classUser import *

def main():
    name = input("Enter Name for Encryption: ")
    user_stamp = input("Enter Stamp for Encryption: ")
    ID= input("Enter ID Number for Encrypt: ")

    user_input = User()
    user_input.Encrypted_Stamp(name, user_stamp, ID)
    user_input.get_details()

if __name__ == main():
    main()
