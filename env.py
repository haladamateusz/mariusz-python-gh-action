import os

URL = 'https://www.backend.mariuszhalada.pl'
LOGIN_URL = URL + '/login'
SEND_EMAIL_URL = URL + '/email'
SEND_TEXT_MESSAGE_URL = URL + '/text-message'
SAVE_INVOICE_LOG_URL = URL + '/invoice-log'
BACKBLAZE_UPLOAD_REQUEST = URL + '/invoice-data/upload-invoice'
CONTRARIAN = 'InPost Paczkomaty Sp. z o.o.'

CREDENTIALS = {
        "username": os.environ['MARIUSZ_USERNAME'],
        "password": os.environ['MARIUSZ_PASSWORD']
}

