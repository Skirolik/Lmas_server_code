


import requests
import time

while True:

    file_url = "http://52.172.4.41:8000/ota/manav/wifi/Combyte_v2.bin"
    response = requests.get(file_url)

    print(response.text)

    time.sleep(1)