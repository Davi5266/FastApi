import requests
i = 0
url = "192.168.0.111:8000"
rota = "user"
parametro = "teste"
while True:
    # r = requests.get("https://192.168.0.111/")
    if parametro:
        r = requests.get(f'http://{url}/{parametro}')
    else:
        r = requests.get(f'http://{url}/')

    print("Stutus", r.status_code)
    print("Response", r.json())
    if i >= 11:
        break
    i= i + 1
