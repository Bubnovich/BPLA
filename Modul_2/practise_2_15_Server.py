# pip install PyJWT
import  jwt
import datetime

SECRET_KEY = 'myKEY-111'

def genetate_token(user_id):
    payload = {
        'user_id': user_id,
        "exp": datetime.datetime.now(tz=datetime.UTC) + datetime.timedelta(seconds=5)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token


def get_token(user_id):
    if user_id:
        token = genetate_token(user_id)
        print(token)
        return token
    return None

if __name__ == "__main__":
    user_id = "egor1"
    token = genetate_token(user_id)
    print(token)