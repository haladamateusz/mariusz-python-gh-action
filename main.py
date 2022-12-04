import requests
import env
from datetime import datetime
import urllib.parse

class InvoiceGenerator:
    TOKEN_REQUEST = None
    EMAIL_REQUEST = None
    SMS_REQUEST = None
    INVOICE_EXISTS_REQUEST = None
    INVOICE_LOG_REQUEST = None
    BACKBLAZE_UPLOAD_REQUEST = None
    headers = None

    def __init__(self):
        self.run_procedure()

    def run_procedure(self):
        self.get_token()
        if not self.TOKEN_REQUEST.ok:
            print(f'{self.current_date()}| ERROR {str(self.TOKEN_REQUEST.status_code)} Authentication fault')
            exit(0)

        self.set_headers()
        self.check_invoice_exists()
        if self.INVOICE_EXISTS_REQUEST.ok and self.invoice_exists():
            print(f'{self.current_date()}| INVOICE EXISTS, SHUTTING DOWN...')
            exit(0)
        if not self.INVOICE_EXISTS_REQUEST.ok:
            print(f'{self.current_date()}| INVOICELOG REQUEST FAILURE...')
            exit(0)

        self.send_email()
        if not self.EMAIL_REQUEST.ok:
            print(f'{self.current_date()}| ERROR {str(self.EMAIL_REQUEST.status_code)} sending email fault ')
            exit(0)
        if self.EMAIL_REQUEST.ok: print('EMAIL OK')

        self.send_sms()
        if not self.SMS_REQUEST.ok:
            print(f'{self.current_date()}| ERROR {str(self.SMS_REQUEST.status_code)} sending sms fault ')
        if self.SMS_REQUEST.ok: print('SMS OK')

        self.save_invoice_log()
        if not self.INVOICE_LOG_REQUEST.ok:
            print(f'{self.current_date()}| ERROR {str(self.INVOICE_LOG_REQUEST.status_code)} saving invoice fault')
        if self.INVOICE_LOG_REQUEST.ok: print('INVOICELOG OK')

        self.upload_invoice()
        if not self.BACKBLAZE_UPLOAD_REQUEST.ok:
             print(f'{self.current_date()}| ERROR {str(self.BACKBLAZE_UPLOAD_REQUEST.status_code)} saving invoice fault')
        if self.BACKBLAZE_UPLOAD_REQUEST.ok: print('BACKBLAZE UPLOAD OK')

    def get_token(self):
        self.TOKEN_REQUEST = requests.post(env.LOGIN_URL, env.CREDENTIALS)

    def set_headers(self):
        self.headers = {"Authorization": f'Bearer {self.TOKEN_REQUEST.json().get("token")}'}

    def check_invoice_exists(self):
        dateNow = datetime.today().strftime('%m%Y')
        self.INVOICE_EXISTS_REQUEST = requests.get(env.SAVE_INVOICE_LOG_URL + f'/{dateNow}', headers=self.headers)

    def invoice_exists(self):
        return bool(self.INVOICE_EXISTS_REQUEST.text)

    def send_email(self):
        self.EMAIL_REQUEST = requests.post(env.SEND_EMAIL_URL + f'/{urllib.parse.quote(env.CONTRARIAN)}',
        json={ "contrarian": env.CONTRARIAN}, headers=self.headers)

    def send_sms(self):
        self.SMS_REQUEST = requests.post(env.SEND_SMS_URL, {}, headers=self.headers)

    def save_invoice_log(self):
        self.INVOICE_LOG_REQUEST = requests.post(env.SAVE_INVOICE_LOG_URL + f'/{urllib.parse.quote(env.CONTRARIAN)}',
         json={ "contrarian": env.CONTRARIAN}, headers=self.headers)

    def upload_invoice(self):
        self.BACKBLAZE_UPLOAD_REQUEST = requests.post(env.BACKBLAZE_UPLOAD_REQUEST,
         json={ "contrarian": env.CONTRARIAN}, headers=self.headers)

    def current_date(self):
        return datetime.today().strftime('%d.%m.%Y %H:%M:%S ')


if __name__ == "__main__":
    x = InvoiceGenerator()
