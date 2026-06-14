import sys
import os

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(r"C:\rpa\Python")

from Classes.Postgres.Postgres.ConectaPG import ConectaPG
from Classes.Oracle.Oracle.ConectaOracle import ConectaOracle
from Classes.ZimbraMailer.ZimbraMailer.Zimbra import ZimbraMailer
from acessaEmailSAC import process_emails_api, mover_email_entre_labels, authenticate_gmail, responder_email_api_duvida, decode_email, mover_para_lixeira, envia_email_instrucao_portal
from dotenv import load_dotenv, find_dotenv
import google.generativeai as genai
import fitz  # PyMuPDF para PDF
from PIL import Image
import time
from groq import Groq
import re
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



def limpar_texto_email(texto):
    pass # Logica de negocio removida por seguranca corporativa

def executa_gemini_arquivo(prompt, filepath):
    pass # Logica de negocio removida por seguranca corporativa

def buscar_senha():
    pass # Logica de negocio removida por seguranca corporativa



def processar_anexos_ou_texto(email_data, texto, download_folder, prompt, linha):
    pass # Logica de negocio removida por seguranca corporativa

    

def consulta_canal_cliente(numero_nf):
    pass # Logica de negocio removida por seguranca corporativa

def processa_emails():
    pass # Logica de negocio removida por seguranca corporativa



def main():
    pass # Logica de negocio removida por seguranca corporativa



if __name__ == "__main__":
    main()