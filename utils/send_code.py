from twilio.rest import Client
from django.conf import settings


def send_verification_code(phone_number, code):
    account_sid = settings.twilio["account_sid"]
    auth_token = settings.twilio["auth_token"]
    from_number = settings.twilio["from_number"]

    client = Client(account_sid, auth_token)

    try:
        message = client.messages.create(
            to="+61{}.".format(phone_number[1:]),
            from_=from_number,
            body="Your Order management system verification code is: {}".format(code)
        )
        return True, message.sid
    except Exception as e:
        return False, e
