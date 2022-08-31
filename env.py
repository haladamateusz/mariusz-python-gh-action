import os
URL = 'https://mariusz-backend.herokuapp.com'
LOGIN_URL = URL + '/login'
SEND_EMAIL_URL = URL + '/email'
SEND_SMS_URL = URL + '/text-message'
SAVE_INVOICE_LOG_URL = URL + '/invoice-log'

CREDENTIALS = {
        "username": os.environ['MARIUSZ_USERNAME'],
        "password": os.environ['MARIUSZ_PASSWORD']
}

