#!/usr/bin/env python3
from creds import Credentials

while True:
    choice = input("Enter 'create' to create new credentials, 'display' to view your saved credentials, 'delete' to delete credentials, or 'copy' to copy an account's password and 'none' to exit:\n")
    if choice == 'none':
        break

    if choice == "create":
        # enquire if account exists or not
        exists = input("Does the account exist alread? Enter 'yes' or 'no': ")

        # create credentials for an existing account
        if exists == 'yes':
            
            new_platform = input("Enter platform: ")
            new_username = input("Enter the username: ")
            new_password = input("Enter password: ")
            # create credentials for a non-existing account
        elif exists == 'no':
            # create for a new/non-existent account
            new_platform = input("Enter platform: ")
            new_username = input("Enter the username: ")

            # generate passowrd or create?
            pswd_option = input("Enter 'generate' to autogenerate a password or 'create' to create your own\n")

            if pswd_option == 'create':
                new_password = input("Enter password: ")
            elif pswd_option == "generate":
                pass
            else:
                print("Incorrect password. Please try again")
                continue #test these continues
        else:
            print("Incorrect input. Please try again")
            continue
        # create the account and print a message
        new_account = Credentials(new_platform, new_username, new_password)
        print(f"Successfully saved credentials for {new_account.platform}!\nUsername - {new_account.username}\nPassword - {new_account.password}")
    elif choice == "display":
        pass
    elif choice == "display":
        pass
    elif choice == "copy":
        pass
    else:
        print("Incorrect input. Please try again")
    