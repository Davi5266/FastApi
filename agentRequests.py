import requests
import matplotlib.pyplot as plt


# i = 0

# while(True):
# r = requests.get("http://localhost:8000/clientesp/readtemperature")

# print(r)

# import requests

humidade = list
temperature_C = list 
temperature_F = list
tempo = list
while True:
	headers = {'Accept': 'application/json'}

	r = requests.get('http://192.168.0.105:3000/clientesp/readtemperature', headers=headers)

	# print(f"Response: {r.json()}")

	data_json = r.json()["message"]

	print(type(data_json))

	for i in data_json:
		# print(" ")
		humidade.append(i['humidade'])
		temperature_C.append(i['temperature_C'])
		temperature_F.append(i['temperature_F'])
		tempo.append(i['data_hora'])
		# print(i['id'])
		# print(" ")

	break
	# i = i + 1


plt.figure(figsize=(10, 6))

plt.plot(tempo, humidade, label="Humidade (%)", color="blue")
plt.plot(tempo, temperature_C, label="Temperatura (°C)", color="red")
plt.plot(tempo, temperature_F, label="Temperatura (°F)", color="green")

plt.xlabel("Tempo")
plt.ylabel("Valores")
plt.title("Gráfico de Sensores")
plt.legend()
plt.grid(True)
plt.show()

	# if i >= 10:
	# 	break
	# print(r.json())

# import requests
# i = 0
# url = "127.0.0.1:8000"
# rota = str
# parametro = "productclass"
# while True:
#     # r = requests.get("https://192.168.0.111/")
#     if parametro:
#         r = requests.get(f'http://{url}/{parametro}')
#         print("1")
#     else:
#         r = requests.get(f'http://{url}/')
#         print("2")

#     print("Stutus", r.status_code)
#     print("Response", r.json())
#     if i >= 11:
#         break
#     i= i + 1
