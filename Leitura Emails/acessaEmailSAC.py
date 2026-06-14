import os.path
import base64
import sys

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(r"C:\rpa\Python")
from Classes.ZimbraMailer.ZimbraMailer.Zimbra import ZimbraMailer
from Classes.Postgres.Postgres.ConectaPG import ConectaPG
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from googleapiclient.discovery import build
from email import message_from_string
from email.header import decode_header
from email.utils import parseaddr
from email import message_from_bytes
from bs4 import BeautifulSoup
import chardet
import unicodedata


# Escopos desejados (leitura + marcação de e-mails)
SCOPES = ['https://www.googleapis.com/auth/gmail.modify']


def limpar_assunto(texto):
    pass # Logica de negocio removida por seguranca corporativa



def envia_email_erro(assunto, corpo, erro):
    pass # Logica de negocio removida por seguranca corporativa



def authenticate_gmail():
    pass # Logica de negocio removida por seguranca corporativa



def decode_mime_header(header_value):
    pass # Logica de negocio removida por seguranca corporativa



def decode_email(msg_raw):
    pass # Logica de negocio removida por seguranca corporativa



def get_label_id(service, label_name):
    pass # Logica de negocio removida por seguranca corporativa



def normalize_message_id(mid):
    pass # Logica de negocio removida por seguranca corporativa



def get_message_id_from_message_id_header(service, message_id_header):
    pass # Logica de negocio removida por seguranca corporativa

def mover_email_entre_labels(gmail_message_id, label_origem, label_destino):
    pass # Logica de negocio removida por seguranca corporativa



def mover_para_lixeira(service, gmail_id):
    pass # Logica de negocio removida por seguranca corporativa



def download_attachments(mime_msg, email_id, download_folder):
    pass # Logica de negocio removida por seguranca corporativa



def process_emails_api(destination_label=None, mark_unread=True, download_attachments_flag=False, download_folder="attachments"):
    pass # Logica de negocio removida por seguranca corporativa



def decode_subject(subject_raw):
    pass # Logica de negocio removida por seguranca corporativa



def decode_header_field(field_value):
    pass # Logica de negocio removida por seguranca corporativa



def responder_email_api_duvida(service, id_email, remetente_email=None):
    pass # Logica de negocio removida por seguranca corporativa



def responder_email_api_duvida_quantidade(service, id_email, quantidade_devolucao, quantidade_nota_fiscal):
    pass # Logica de negocio removida por seguranca corporativa



def responder_email_api(service, id_email, conteudo):
    pass # Logica de negocio removida por seguranca corporativa

def envia_email_instrucao_portal(service, id_email, remetente_email=None):
    pass # Logica de negocio removida por seguranca corporativa

if __name__ == '__main__':
    service = authenticate_gmail()