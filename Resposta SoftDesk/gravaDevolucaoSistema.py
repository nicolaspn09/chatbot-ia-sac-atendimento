import requests
import sys

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(r"C:\rpa\Python")
from Classes.Hangouts.Hangouts.Hangouts import Hangouts
from Classes.Postgres.Postgres.ConectaPG import ConectaPG
from Classes.Oracle.Oracle.ConectaOracle import ConectaOracle
from Classes.ZimbraMailer.ZimbraMailer.Zimbra import ZimbraMailer
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from dotenv import load_dotenv, find_dotenv
from groq import Groq
import os
import json
import time
import smtplib
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from datetime import datetime, timedelta


# Caminho do arquivo JSON
def diretorio_json():
    pass # Logica de negocio removida por seguranca corporativa

def busca_data(days=1):
    pass # Logica de negocio removida por seguranca corporativa



def preenche_dados_sheet(linha, protocolo):
    pass # Logica de negocio removida por seguranca corporativa



def verifica_quantidade_nota(numero_nf, codigo_produto):
    pass # Logica de negocio removida por seguranca corporativa



def verifica_cnpj(codigo_cliente):
    pass # Logica de negocio removida por seguranca corporativa



def verifica_nota(numero_nf, codigo_produto):
    pass # Logica de negocio removida por seguranca corporativa



def verifica_nota_cnpj(numero_nf, codigo_produto, numero_cnpj):
    pass # Logica de negocio removida por seguranca corporativa



def verifica_nota_itens(numero_nf):
    pass # Logica de negocio removida por seguranca corporativa



def verifica_nota_itens_cnpj(numero_nf, numero_cnpj):
    pass # Logica de negocio removida por seguranca corporativa



def verifica_nota_itens_ean(numero_nf, ean):
    pass # Logica de negocio removida por seguranca corporativa



def consulta_capa_registro(protocolo):
    pass # Logica de negocio removida por seguranca corporativa



def consulta_dados_cliente(codigo_cliente):
    pass # Logica de negocio removida por seguranca corporativa



def consulta_dados_cliente_email(codigo_cliente):
    pass # Logica de negocio removida por seguranca corporativa



def consulta_dados_cliente_nao_encontrado(codigo_cliente):
    pass # Logica de negocio removida por seguranca corporativa



def consulta_email_rca(setor):
    pass # Logica de negocio removida por seguranca corporativa



def consulta_dados_tipo_ocorrencia(tipo_ocorrencia, subtipo_ocorrencia):
    pass # Logica de negocio removida por seguranca corporativa



def consulta_dados_mercadoria(codigo_mercadoria):
    pass # Logica de negocio removida por seguranca corporativa



def consulta_mercadoria_ean(ean_mercadoria):
    pass # Logica de negocio removida por seguranca corporativa



def consulta_protocolo_nota(numero_nf, codigo_produto, quantidade):
    pass # Logica de negocio removida por seguranca corporativa

    

def consulta_tipo_mercadoria(codigo_mercadoria):
    pass # Logica de negocio removida por seguranca corporativa



def forma_email(ocorrencia, data_registro, data_limite, itens, codigo_cliente, cnpj, razao_social, endereco, bairro_cidade_uf, setor, entregador, solicitante, email_retorno, email_entregador, email_representante, tipo_ocorrencia):
    pass # Logica de negocio removida por seguranca corporativa



def envia_email(destinatarios_email, assunto_email, mensagem_email, destinatarios_copia=None, destinatarios_copia_oculta=None, anexos=None):
    pass # Logica de negocio removida por seguranca corporativa



def verifica_itens_groq(descricao_mercadoria_cliente, dict_itens):
    pass # Logica de negocio removida por seguranca corporativa

def solicita_tabela_base():
    pass # Logica de negocio removida por seguranca corporativa

def busca_data(days=1):
    pass # Logica de negocio removida por seguranca corporativa

def url_api():
    pass # Logica de negocio removida por seguranca corporativa

def requisita_bearer_token():
    pass # Logica de negocio removida por seguranca corporativa



def efetua_registro(payload_completo):
    pass # Logica de negocio removida por seguranca corporativa



def verifica_registros():
    pass # Logica de negocio removida por seguranca corporativa



def itera_notas(payload_por_protocolo):
    pass # Logica de negocio removida por seguranca corporativa



def main():
    pass # Logica de negocio removida por seguranca corporativa



if __name__ == "__main__":
    main()