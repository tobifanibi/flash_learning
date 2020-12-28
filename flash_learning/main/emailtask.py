from itsdangerous import URLSafeTimedSerializer
#issue importing app
def create_confirmation_token(email):
    serializer = URLSafeTimedSerializer(b'\xbf\x1b\xe1\x18\xaf\x8b\x1a\xb2\xa6\xb9\xcf\x7f\xe0+\xda\xd9')
    return serializer.dumps(email, salt='8UUWHlTewPpnTUcHhErlLn4X/X0swZHi')

def confirm_token(token,expiration=86400):
    serializer = URLSafeTimedSerializer(b'\xbf\x1b\xe1\x18\xaf\x8b\x1a\xb2\xa6\xb9\xcf\x7f\xe0+\xda\xd9')
    # confirm key if information is correct, raise error. Return False if not
    confirm = serializer.loads(
    token,
    salt='8UUWHlTewPpnTUcHhErlLn4X/X0swZHi',
    max_age=expiration)
    return confirm


