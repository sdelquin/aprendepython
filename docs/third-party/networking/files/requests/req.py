import requests

response = requests.get('https://twitter.com')
print(response.status_code)
print(len(response.text))
print(response.cookies.get('guest_id'))
print(response.headers.get('content-encoding'))
