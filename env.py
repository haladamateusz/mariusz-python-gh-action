import os
URL = 'http://localhost:3000'
LOGIN_URL = URL + '/login'
SEND_EMAIL_URL = URL + '/email'
SEND_SMS_URL = URL + '/sms'
SAVE_INVOICE_LOG_URL = URL + '/invoice-log'

CREDENTIALS = {
        "username": os.environ['MARIUSZ_USERNAME'],
        "password": os.environ['MARIUSZ_PASSWORD']
}

