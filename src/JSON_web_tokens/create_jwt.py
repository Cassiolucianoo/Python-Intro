import hmac
import hashlib
import base64
import json

secret_key = '52d3f853c19f8b63c0918c126422aa2d99b1aef33ec63d41dea4fadf19406e54'

header = json.dumps({
    'typ': 'JWT',
    'alg': 'HS256'
}).encode()

payload = json.dumps({
    'userId': '55395427-265a-4166-ac93-da6879edb57a',
    'exp': 1556841600,
}).encode()

b64_header = base64.urlsafe_b64encode(header).decode()
b64_payload = base64.urlsafe_b64encode(payload).decode()

signature = hmac.new(
    key=secret_key.encode(), 
    msg=f'{b64_header}.{b64_payload}'.encode(),
    digestmod=hashlib.sha256
).digest()

JWT = f'{b64_header}.{b64_payload}.{base64.urlsafe_b64encode(signature).decode()}'

print(JWT)