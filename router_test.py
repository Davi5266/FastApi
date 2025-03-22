import requests
i = 0
url = "127.0.0.1:8000"
rota = str
parametro = "productclass"
while True:
    # r = requests.get("https://192.168.0.111/")
    if parametro:
        r = requests.get(f'http://{url}/{parametro}')
        print("1")
    else:
        r = requests.get(f'http://{url}/')
        print("2")

    print("Stutus", r.status_code)
    print("Response", r.json())
    if i >= 11:
        break
    i= i + 1
