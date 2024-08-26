import requests
import json

# URL, на который будет отправлен запрос
url = 'http://127.0.0.1:8000/api/api/'

# Данные, которые будут отправлены в формате JSON
data = {
    "device_type": None,
    
}

# Заголовки запроса
headers = {
    'Content-Type': 'application/json'
}


response = requests.post(url, data=json.dumps(data), headers=headers)
    
   