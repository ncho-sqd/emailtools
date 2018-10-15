from LogIn import LogIn
import imaplib
import email
from tqdm import tqdm
import pandas as pd
import sys

# function to read emails
def read_email(con):
    """Reads email from given SMTP server provided in con object
    """
    collect = []
    con.select()

    type, data = con.search(None, 'ALL')
    mail_ids = data[0]

    id_list = mail_ids.split()   

    for i in id_list:
        typ, data = con.fetch(str(int(i)), '(RFC822)' )
        
        try:
            for response_part in data:
                if isinstance(response_part, tuple):
                    sys.stdout.write("\r{}".format(i))
                    sys.stdout.flush()
                
                    msg = email.message_from_string(response_part[1].decode('utf-8'))
                    email_subject = msg['subject']
                    email_from = msg['from']
                    collect.append([i, email_subject, email_from])
        except:
            print("Error")
            pass
    return(collect)


if __name__ == '__main__':
    # establish connection by receiving credentials from cli
    id = input("id: ")
    password = input("password: ")
    con = LogIn(id = id, pw = password).login()

    # collect email and export sender and subject line to csv
    pd.DataFrame(read_email_from_gmail(con)).to_csv("email.csv")