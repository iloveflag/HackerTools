import requests
import base64

r = requests.post('')

flag = r.headers['FLAG']

flag = base64.b64decode(flag).decode().split(':')[1]

para = {'key':flag}

r = requests.post('',data = para)

print(r.text)