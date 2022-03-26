from classUser import *


def main():
    print("Enter user details")
    username = input("Username: ")
    ID = input("ID number: ")
    user_stamp = input("Enter Stamp for Encryption: ")

    user_input = User()
    user_input.Encrypted_Stamp(username, ID, user_stamp)
    user_input.get_details()


if __name__ == main():
    main()
