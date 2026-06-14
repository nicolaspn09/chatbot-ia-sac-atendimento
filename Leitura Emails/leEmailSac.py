import sys
import os

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(r"C:\rpa\Python")

from Classes.Gmail.Gmail.ConectaGmail import ConectaGmail
from Classes.Postgres.Postgres.ConectaPG import ConectaPG
from Classes.Oracle.Oracle.ConectaOracle import ConectaOracle
from Classes.ZimbraMailer.ZimbraMailer.Zimbra import ZimbraMailer
from acessaEmailSAC import process_emails_api, mover_email_entre_labels, authenticate_gmail, responder_email_api_duvida, decode_email, mover_para_lixeira
from identificaTipoSolicitacao import verifica_solicitacao_item_por_pk
from efetuaRegistroSacAgrupado import verifica_registros, envia_emails_agrupados
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import decode_header
from email.utils import parseaddr
from dotenv import load_dotenv, find_dotenv
import base64
import google.generativeai as genai
import fitz  # PyMuPDF para PDF
from PIL import Image
import glob
import time
from groq import Groq
import re
from datetime import datetime
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


# Escopos desejados (leitura + marcação de e-mails)
SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

def envia_email_erro(assunto, corpo, erro):
    pass # Logica de negocio removida por seguranca corporativa

def executa_groq(chave, prompt, texto):
    pass # Logica de negocio removida por seguranca corporativa

def executa_groq_deepseek(chave, prompt, texto):
    pass # Logica de negocio removida por seguranca corporativa

def executa_groq_langchain(chave, texto):
    pass # Logica de negocio removida por seguranca corporativa

def executa_groq_langchain_analisador(chave, texto):
    pass # Logica de negocio removida por seguranca corporativa

def executa_groq_langchain_analisador_email_duvida(chave, texto):
    pass # Logica de negocio removida por seguranca corporativa

def executa_gemini_texto(chave, prompt, texto):
    pass # Logica de negocio removida por seguranca corporativa



def limpar_texto_email(texto):
    pass # Logica de negocio removida por seguranca corporativa

def executa_gemini_arquivo(prompt, filepath):
    pass # Logica de negocio removida por seguranca corporativa

def buscar_senha():
    pass # Logica de negocio removida por seguranca corporativa



def processar_anexos_ou_texto(email_data, texto, download_folder, prompt, linha):
    pass # Logica de negocio removida por seguranca corporativa



def analisa_retorno_linha_dividida(linha_dividida):
    pass # Logica de negocio removida por seguranca corporativa

    

def limpar_variaveis(tipo_solicitacao, numero_nf, interpretacao, cnpj, codigo_produto, ean_produto, codigo_cliente, nome_item, quantidade, email, protocolo, lote_nf, lote_correto):
    pass # Logica de negocio removida por seguranca corporativa



def processa_email_agrupado(gmail_id, pks_geradas_por_email):
    pass # Logica de negocio removida por seguranca corporativa

def processa_emails():
    pass # Logica de negocio removida por seguranca corporativa



def main():
    pass # Logica de negocio removida por seguranca corporativa



if __name__ == "__main__":
    main()