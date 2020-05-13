import requests
import time

while True:
    r = requests.get('https://google.com')
    print(r.content)
    time.sleep(5)