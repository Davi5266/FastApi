import requests

i = 0

while(True):
	r = requests.get("http://localhost:8000/")
	i = i + 1

	if i >= 10:
		break
	print(r.json())
