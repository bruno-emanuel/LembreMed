import threading
import time
import schedule
from datetime import datetime

from .database import SessionLocal
from .models import Remedio, Historico
from .crud import criar_historico


def verificar_lembretes():
    db = SessionLocal()
    try:
        agora = datetime.now().strftime("%H:%M")
        remedios = db.query(Remedio).all()

        for remedio in remedios:
            if remedio.horario == agora:
                ja_registrado = (
                    db.query(Historico)
                    .filter(
                        Historico.remedio_id == remedio.id,
                        Historico.status == "pendente"
                    )
                    .order_by(Historico.data_hora.desc())
                    .first()
                )

                if not ja_registrado or ja_registrado.data_hora.strftime("%Y-%m-%d %H:%M") != datetime.now().strftime("%Y-%m-%d %H:%M"):
                    criar_historico(
                        db,
                        remedio.id,
                        "pendente",
                        f"Lembrete gerado automaticamente às {agora}"
                    )
                    print(f"[OK] Lembrete criado para {remedio.nome} às {agora}")
    finally:
        db.close()


def iniciar_scheduler():
    schedule.every(1).minutes.do(verificar_lembretes)

    def run():
        while True:
            schedule.run_pending()
            time.sleep(1)

    thread = threading.Thread(target=run, daemon=True)
    thread.start()