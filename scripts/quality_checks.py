import logging
from logging.handlers import SMTPHandler
import sys
from pathlib import Path
from decouple import config,Csv

#to help is setting logging file path
BASE_DIR = Path(__file__).resolve().parent.parent

#logging config
logger = logging.getLogger("qualityCheckLogger")
ADMIN_EMAIL = config('ADMIN_EMAIL',cast=Csv()) #list of admin emails to send critical error messages to

#formatter
formatter = logging.Formatter(fmt='%(name)s: %(asctime)s %(levelname)s: - %(message)s')

#what appears on terminal
console_handler = logging.StreamHandler(stream=sys.stdout)
console_handler.setFormatter(formatter)

#what goes to a file
file_handler = logging.FileHandler(filename='logs.txt')
file_formatter = file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)


def setup_email_alert(logger, admin_email):
    #configure the email handler
    mail_handler = SMTPHandler(
        mailhost=(config("EMAIL_HOST"), 587), #(Host, Port) #
        fromaddr=config("EMAIL_HOST_USER"),
        toaddrs=admin_email,
        credentials=(config('EMAIL_HOST_USER'), config('EMAIL_HOST_PASSWORD')),
        secure=(),
        subject="Annex ABC Data: Quality Check Failed"
    )

    #email set for errors and above
    mail_handler.setLevel(logging.ERROR)
    formatter = logging.Formatter('''
    Loger: %(name)s
    Time: %(asctime)s
    Module: %(module)s
    Line: %(lineno)d
    Message: %(message)s
    ''')
    #set email alert logger
    mail_handler.setFormatter(formatter)

    logger.addHandler(mail_handler)

setup_email_alert(logger, ADMIN_EMAIL)

def data_quality_check():
    result = (1 + 1 == 3) # This is just False

    if result == False:
        # This is how you force the error to happen
        raise logger.error(f"Some serious error occured:",exc_info=True)

if __name__ == '__main__':
    data_quality_check()