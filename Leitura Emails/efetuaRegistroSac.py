import requests
import sys

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(r"C:\rpa\Python")
from Classes.Postgres.Postgres.ConectaPG import ConectaPG
from Classes.Oracle.Oracle.ConectaOracle import ConectaOracle
from Classes.ZimbraMailer.ZimbraMailer.Zimbra import ZimbraMailer
from acessaEmailSAC import authenticate_gmail, mover_email_entre_labels, responder_email_api_duvida_quantidade, responder_email_api
from dotenv import load_dotenv
import google.generativeai as genai
from email.header import decode_header
from email.utils import parseaddr
from groq import Groq
import base64
import os
import json
from datetime import datetime, timedelta
import imaplib
import email
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# Escopos desejados (leitura + marcação de e-mails)
SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

def envia_email_erro(assunto, corpo, erro):
    pass # Logica de negocio removida por seguranca corporativa

def get_label_id(service, label_name):
    pass # Logica de negocio removida por seguranca corporativa

def get_message_id_from_message_id_header(service, message_id_header):
    pass # Logica de negocio removida por seguranca corporativa

def busca_data(days=1):
    pass # Logica de negocio removida por seguranca corporativa



def forma_email(ocorrencia, data_registro, data_limite, itens, codigo_cliente, cnpj, razao_social, endereco, bairro_cidade_uf, setor, entregador, solicitante, email_retorno, email_entregador, email_representante, tipo_ocorrencia):
    pass # Logica de negocio removida por seguranca corporativa



def envia_email(destinatarios_email, assunto_email, mensagem_email, destinatarios_copia=None, destinatarios_copia_oculta=None, anexos=None):
    pass # Logica de negocio removida por seguranca corporativa



def consulta_capa_registro(protocolo):
    pass # Logica de negocio removida por seguranca corporativa



def consulta_dados_cliente(codigo_cliente):
    pass # Logica de negocio removida por seguranca corporativa



def consulta_email_rca(setor):
    pass # Logica de negocio removida por seguranca corporativa



def consulta_dados_tipo_ocorrencia(ocorrencia):
    pass # Logica de negocio removida por seguranca corporativa

    

def consulta_dados_mercadoria(codigo_mercadoria):
    pass # Logica de negocio removida por seguranca corporativa



def consulta_protocolo_nota(numero_nf, codigo_produto, quantidade):
    pass # Logica de negocio removida por seguranca corporativa



def preenche_protocolo(protocolo, numero_nf):
    pass # Logica de negocio removida por seguranca corporativa

def url_api():
    pass # Logica de negocio removida por seguranca corporativa

def requisita_bearer_token():
    pass # Logica de negocio removida por seguranca corporativa



def efetua_registro(empresa, codigo_cliente, numero_nf, data_emissao, dict_mercadorias):
    pass # Logica de negocio removida por seguranca corporativa



def verifica_registros():
    pass # Logica de negocio removida por seguranca corporativa



def itera_notas(dict_notas):
    pass # Logica de negocio removida por seguranca corporativa



def itera_notas_envia_email(dict_notas):
    pass # Logica de negocio removida por seguranca corporativa



def analisa_notas_fora_prazo():
    pass # Logica de negocio removida por seguranca corporativa


def main():
    pass # Logica de negocio removida por seguranca corporativa



if __name__ == "__main__":
    dict_notas = verifica_registros()
    itera_notas(dict_notas)
    itera_notas_envia_email(dict_notas)