from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"mensagem": "API rodando com sucesso!"}

    remedios = []
    from pydantic import BaseModel

class Remedio(BaseModel):
    nome: str
    horario: str
    telefone: str

@app.post("/remedios")
def adicionar_remedio(remedio: Remedio):
    remedios.append(remedio)
    return {"msg": "Remédio cadastrado!"}

@app.get("/remedios")
def listar():
    return remedios
import schedule
import time
from datetime import datetime

def verificar_remedios():
    agora = datetime.now().strftime("%H:%M")

    for r in remedios:
        if r.horario == agora:
            print(f"Hora do remédio: {r.nome}")

schedule.every(1).minutes.do(verificar_remedios)

def rodar_agendador():
    while True:
        schedule.run_pending()
        time.sleep(1)