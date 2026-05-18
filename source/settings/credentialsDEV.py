import base64

user=''
pw=''

# headers for tests
x = base64.b64encode(f"{user}:{pw}".encode()).decode()
headers = {'Authorization': f'Basic {x}'}
