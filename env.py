import os
URL = 'https://backend.mariuszhalada.pl'
LOGIN_URL = URL + '/login'
SEND_EMAIL_URL = URL + '/email'
SEND_SMS_URL = URL + '/text-message'
SAVE_INVOICE_LOG_URL = URL + '/invoice-log'
SAVE_INVOICE_TO_BACKBLAZE_URL = URL + '/invoice-data/upload-invoice'

CREDENTIALS = {
        "username": os.environ['MARIUSZ_USERNAME'],
        "password": os.environ['MARIUSZ_PASSWORD']
}

