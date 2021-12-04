from fastapi import FastAPI
from datetime import datetime
import time, requests, os

weather = 0
def update_weather():
    global weather
    data = requests.get("http://api.openweathermap.org/data/2.5/weather?lat=-23.658&lon=-46.6827&appid=d7ac1f99b520b6521c21eb7775399347",
        headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'}).json()

    weather = int(data['main']['temp'] - 273.15)

def get_time():
     return datetime.now().strftime("%d/%m/%y %H:%M:%S")

def get_server_status():
    return requests.get('http://127.0.0.1:8001/healthcheck').json()['status']

def get_last_n_lines(file_name, N):
    list_of_lines = []
    with open(file_name, 'rb') as read_obj:
        read_obj.seek(0, os.SEEK_END)
        buffer = bytearray()
        pointer_location = read_obj.tell()
        while pointer_location >= 0:
            read_obj.seek(pointer_location)
            pointer_location = pointer_location -1
            new_byte = read_obj.read(1)
            if new_byte == b'\n':
                list_of_lines.append(buffer.decode()[::-1])
                if len(list_of_lines) == N:
                    return list(reversed(list_of_lines))
                buffer = bytearray()
            else:
                buffer.extend(new_byte)
        if len(buffer) > 0:
            list_of_lines.append(buffer.decode()[::-1])
    return list(reversed(list_of_lines))

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'TIME: {get_time()}')
    print(f'WEATHER: {weather}')
    print(f'RADIOACTIVITY LVL: BEARABLE')
    print(f'\n\n\nSERVER STATUS: {get_server_status()}')
    print('--------------')
    [print(msg) for msg in get_last_n_lines('central_log.txt', 5)]
    time.sleep(1)
    update_weather()
