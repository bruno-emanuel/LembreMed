# LembreMed

Sistema web desenvolvido para auxiliar no controle de medicamentos, com foco em idosos e cuidadores.

A proposta do projeto é simples: garantir que os medicamentos sejam tomados no horário correto, reduzindo esquecimentos e melhorando a rotina de quem depende de múltiplos remédios.

---

## Sobre o projeto

O LembreMed é uma aplicação web construída com Python que permite cadastrar usuários, idosos e medicamentos, além de monitorar automaticamente os horários definidos.

O sistema verifica continuamente os horários cadastrados e gera registros de lembretes de forma automática.

---

## Funcionalidades

* Cadastro de usuários
* Cadastro de idosos
* Cadastro de medicamentos
* Associação de medicamentos a um idoso
* Monitoramento automático de horários
* Geração de histórico de lembretes
* Estrutura preparada para integração com WhatsApp

---

## Tecnologias utilizadas

* Python
* FastAPI
* SQLAlchemy
* SQLite
* Jinja2
* HTML, CSS e JavaScript

---

## Estrutura do projeto

```bash
lembremed/
│
├── app/
│   ├── main.py
│   ├── models.py
│   ├── database.py
│   ├── crud.py
│   ├── auth.py
│   ├── scheduler.py
│   ├── whatsapp.py
│   ├── utils.py
│   └── templates/
│
├── static/
│   ├── css/
│   ├── js/
│   └── img/
│
├── requirements.txt
└── README.md
```

---

## Como executar o projeto

```bash
# criar ambiente virtual
python -m venv venv

# ativar ambiente
venv\Scripts\activate

# instalar dependências
pip install -r requirements.txt

# iniciar servidor
python -m uvicorn app.main:app --reload
```

Acesse no navegador:

```
http://127.0.0.1:8000
```

---

## Estado atual

O projeto já conta com as funcionalidades principais implementadas e funcionando:

* sistema de cadastro completo
* automação de verificação de horários
* geração automática de histórico

---

## Próximos passos

* integração com WhatsApp para envio de lembretes
* confirmação de medicação tomada
* melhoria da interface
* dashboard com mais informações
* controle por cuidador

---

## Objetivo

Este projeto foi desenvolvido com o intuito de praticar desenvolvimento backend e ao mesmo tempo criar uma solução que tenha utilidade real no dia a dia.

---

## Autor

Bruno Emanuel da Silva Cruz
