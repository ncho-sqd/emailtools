import imaplib

class LogIn:
    def __init__(self, id, pw
               , ORIG_EMAIL = "@gmail.com"
               , SMTP_SERVER = "imap.gmail.com"
               , SMTP_PORT = 993):
        self.ORG_EMAIL   = ORIG_EMAIL
        self.FROM_EMAIL  = id + self.ORG_EMAIL
        
        self.FROM_PWD    = pw
        self.SMTP_SERVER = SMTP_SERVER
        self.SMTP_PORT   = SMTP_PORT

    def reset_id(self, id):
        self.FROM_EMAIL = id + self.ORG_EMAIL

    def reset_password(self, pw):
        self.FROM_PWD = pw
    
    def login(self):
        mail = imaplib.IMAP4_SSL(self.SMTP_SERVER)
        mail.login(self.FROM_EMAIL, self.FROM_PWD)
        return(mail)