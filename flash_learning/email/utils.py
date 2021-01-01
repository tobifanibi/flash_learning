from flask_mail import Message

from flash_learning import mail


def send_email(user, subject, template):
    msg = Message(subject,
                  recipients=[user],
                  html=template)
    mail.send(msg)
