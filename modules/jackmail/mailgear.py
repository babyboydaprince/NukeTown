# e-mailing module
import os
import sys
import json
from colorama import Fore
from getpass import getpass, getuser
from smtplib import SMTP, SMTPAuthenticationError
import modules.bones.crypt.sparkle as sparkle


# Login data
sender_email_database = 'modules/jackmail/sender.json'
sparkle_encryption_key = getuser() + ':SPARKLE'
smtp_server = 'smtp.gmail.com'
smtp_port = 587


"""Write sender email"""


def WriteSenderEmail():
    username = input(
        f'{Fore.BLUE}[?] {Fore.MAGENTA}Please enter sender gmail address: {Fore.BLUE}')
    password = getpass(
        f'{Fore.BLUE}[?] {Fore.MAGENTA}Please enter sender gmail password: {Fore.BLUE}')
    server = SMTP(smtp_server, smtp_port)
    server.ehlo()
    server.starttls()
    # Try login to account
    try:
        server.login(username, password)
    except SMTPAuthenticationError:
        print(
            f'{Fore.RED}[!] {Fore.MAGENTA}Wrong'
            ' account password, if not, try enabling this:'
            f'\n    https://myaccount.google.com/lesssecureapps{Fore.RESET}'
        )
        sys.exit(1)
    else:
        print(
            f'{Fore.GREEN}[+] {Fore.YELLOW}Log in Success!{Fore.RESET}'
        )

    # Save data to db?
    confirm = input(
        '{Fore.BLUE}[?] {Fore.MAGENTA}Whould you like to save this information for future reference? (y/n) : {Fore.BLUE}')
    confirm = confirm.upper() in ('Y', 'YES', '1', 'TRUE')
    if confirm:
        # Write database
        with open(sender_email_database, 'w') as db:
            json.dump(
                {
                    'username':
                        sparkle.Encrypt(username, sparkle_encryption_key),
                    'password':
                        sparkle.Encrypt(password, sparkle_encryption_key)
                }, db
            )
        print(
            f'{Fore.GREEN}[+] {Fore.YELLOW}Data saved'
            ' to: {repr(sender_email_database)}{Fore.RESET}'
        )
    return [server, username]


""" Read sender email """


def ReadSenderEmail():
    # Creat if it doesn't exist
    if not os.path.exists(sender_email_database):
        return WriteSenderEmail()
    # Read db
    with open(sender_email_database, 'r') as db:
        auth = json.load(db)
        auth['username'] = sparkle.Decrypt(
            auth['username'], sparkle_encryption_key)
        auth['password'] = sparkle.Decrypt(
            auth['password'], sparkle_encryption_key)
    # Login
    server = SMTP(smtp_server, smtp_port)
    server.ehlo()
    server.starttls()
    try:
        server.login(
            auth['username'],
            auth['password']
        )
    except SMTPAuthenticationError:
        print(
            f'{Fore.RED}[!] {Fore.MAGENTA}Wrong password{Fore.RESET}'
        )
        os.remove(sender_email_database)
        sys.exit(1)
    else:
        return [server, auth['username']]
