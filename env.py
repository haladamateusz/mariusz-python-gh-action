import os

URL = 'https://backend.mariuszhalada.pl'
LOGIN_URL = URL + '/login'
SEND_EMAIL_URL = URL + '/email'
SEND_SMS_URL = URL + '/text-message'
SAVE_INVOICE_LOG_URL = URL + '/invoice-log'
BACKBLAZE_UPLOAD_REQUEST = URL + '/invoice-data/upload-invoice'
CONTRARIAN = 'InPost Paczkomaty Sp. z o.o.'

CREDENTIALS = {
        "username": os.environ['MARIUSZ_PASSWORD'],
        "password": os.environ['MARIUSZ_PASSWORD']
}

