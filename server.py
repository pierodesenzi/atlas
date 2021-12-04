from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

def get_time():
     return datetime.now().strftime("%d/%m/%y %H:%M:%S")

@app.post('/central')
async def central_receiver(msg):
    with open('central_log.txt','a') as file:
        file.write(f'{get_time()} - {msg}\n')

@app.get('/healthcheck')
async def healthcheck():
    return {'status': 'RUNNING'}
