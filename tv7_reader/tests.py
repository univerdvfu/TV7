import requests
import json

# URL, на который будет отправлен запрос
url = 'http://127.0.0.1:8000/api/api/'
for i in range(1):

    # Данные, которые будут отправлены в формате JSON
    data = {
    "name": "test",
    "data": {
        "temp": 1
    }
}

    # Заголовки запроса
    headers = {
        'Content-Type': 'application/json'
    }


    response = requests.post(url, data=json.dumps(data), headers=headers)
    
   