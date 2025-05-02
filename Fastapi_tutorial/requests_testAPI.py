import requests

url = "192.168.0.106"
port = "3000"

path = "sla"

parameters = 4

print(f'http://{url}:{port}/')
if url is not None:
    if path is not None:
        if parameters is not None:
            print(f'http://{url}:{port}/{path}/{parameters}')
            r = requests.put(f'http://{url}:{port}/{path}/{parameters}')
            print(r)
        else:    
            r = requests.put(f'http://{url}:{port}/{path}')
            print(r)
    r = requests.put(f'http://{url}:{port}/')
    print("status code: ",r.status_code)
else:
    print("url: null")