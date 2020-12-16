import hmac
import hashlib
import base64
import json 

secret_key = '52d3f853c19f8b63c0918c126422aa2d99b1aef33ec63d41dea4fadf19406e54'
JWT = 'eyJ0eXAiOiAiSldUIiwgImFsZyI6ICJIUzI1NiJ9.eyJ1c2VySWQiOiAiNTUzOTU0MjctMjY1YS00MTY2LWFjOTMtZGE2ODc5ZWRiNTdhIiwgImV4cCI6IDE1NTY4NDE2MDB9.09Rcd_IMo9dDVi0kJGeCpgS-YeTKtUxmMvHO1QnLC5c='

b64_header, b64_payload, b64_signature = JWT.split('.')
b64_signature_checker = base64.urlsafe_b64encode(
    hmac.new(
        key=secret_key.encode(), 
        msg=f'{b64_header}.{b64_payload}'.encode(), 
        digestmod=hashlib.sha256
    ).digest()
).decode()

payload = json.loads(base64.urlsafe_b64decode(b64_payload))

if b64_signature_checker != b64_signature:
    raise Exception('Assinatura inválida')

print(payload)