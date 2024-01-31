import requests

url = "https://tahakh.pythonanywhere.com/api/outlets/"
headers = {
    "Authorization": "Api-Key ###################"
}

response = requests.get(url, headers=headers)
print(response.json())
