from acessaSiteRetornaInformacao import RetornaInformacaoSoftDesk

import sys
import os

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(r"C:\rpa\Python")
from dotenv import load_dotenv
from pathlib import Path
from Classes.GoogleSheets.GoogleSheets.GoogleSheets import GoogleSheets
from Classes.Firefox.Firefox.conectaFirefox import FirefoxSeleniumManager
from Classes.Postgres.Postgres.ConectaPG import ConectaPG
import requests
import smtplib
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# Envia e-mails
def envia_email(mensagem_email, destinatarios_email, assunto_email):
    pass # Logica de negocio removida por seguranca corporativa



def informa_dados_backup(retorno_devolucao, numero_nf, data_emissao, codigo_produto, ean, descricao_produto, quantidade, motivo, lote_caixa, protocolo_laboratorio, codigo_cliente, cnpj, email, lote_nota, protocolo_distribuidora, tipo_avaria, chamado, data_hora_leitura):
    pass # Logica de negocio removida por seguranca corporativa



def remove_linha(linha):
    pass # Logica de negocio removida por seguranca corporativa

def verifica_dados_planilha():
    pass # Logica de negocio removida por seguranca corporativa



if __name__ == "__main__":
    verifica_dados_planilha()