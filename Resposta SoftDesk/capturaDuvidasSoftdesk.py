from acessaSiteRetornaInformacao import RetornaInformacaoSoftDesk

import sys
import os

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(r"C:\rpa\Python")
from dotenv import load_dotenv, find_dotenv
from Classes.GoogleSheets.GoogleSheets.GoogleSheets import GoogleSheets
from Classes.Firefox.Firefox.conectaFirefox import FirefoxSeleniumManager
from Classes.Postgres.Postgres.ConectaPG import ConectaPG
from Classes.Groq.Groq.acessaGroq import ExecutaGroq
import requests
import smtplib
import time
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# Envia e-mails
def envia_email(mensagem_email, destinatarios_email, assunto_email):
    pass # Logica de negocio removida por seguranca corporativa



def acessa_captura_duvidas_softdesk():
    pass # Logica de negocio removida por seguranca corporativa



def consulta_dados_ia(resposta):
    pass # Logica de negocio removida por seguranca corporativa



def ajusta_dados_api(resposta, dados):
    pass # Logica de negocio removida por seguranca corporativa



def ajusta_dados_insert(resposta, dados):
    pass # Logica de negocio removida por seguranca corporativa
