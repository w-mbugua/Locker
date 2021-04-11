#!/usr/bin/env python3
from creds import Credentials
import string
import random

while True:
    choice = input("Enter 'create' to create new credentials, 'display' to view your saved credentials, 'delete' to delete credentials, or 'copy' to copy an account's password and 'none' to exit:\n")
    if choice == 'none':
        break

    if choice == "create":
        # enquire if account exists or not
        exists = input("Does the account exist already? Enter 'yes' or 'no': ")

        # create credentials for an existing account
        new_platform = input("Enter platform: ")
        new_username = input("Enter the username: ")
        if exists == 'yes':
            new_password = input("Enter password: ")
            # create credentials for a non-existing account
        elif exists == 'no':
            # generate passowrd or create?
            pswd_option = input("Enter 'generate' to autogenerate a password or 'create' to create your own\n")

            if pswd_option == 'create':
                new_password = input("Enter password: ")
            elif pswd_option == "generate":
                # generate a password using random
                pswd_string = ''

                for i in range(3):
                    pswd_string = pswd_string + random.choice(string.ascii_letters) + str(random.randint()) + random.choice('!$%&()*<>?@^_')
                
                new_password = pswd_string
            else:
                print("Incorrect input. Please try again")
                continue #test these continues
        else:
            print("Incorrect input. Please try again")
            continue
        # create the account and print a message
        new_account = Credentials(new_platform, new_username, new_password)
        print(f"Successfully saved credentials for {new_account.platform}!\nUsername - {new_account.username}\nPassword - {new_account.password}")
        new_account.save_password()
    elif choice == "display":
        print(Credentials.display_password())
    elif choice == "delete":
        to_delete = input("Enter the account to delete from locker\n")
        # check if it's in locker
        if to_delete in Credentials.locker:
            inp = input(f"Are you sure you would like to delete {to_delete} details from locker? y/n: ")
            if inp == 'y':
                new_account.delete_password()
            elif inp == 'n':
                continue
        else:
            print("Sorry. You don't seem to have such an account in locker")
    elif choice == "copy":
        pass
    else:
        print("Incorrect input. Please try again")
    