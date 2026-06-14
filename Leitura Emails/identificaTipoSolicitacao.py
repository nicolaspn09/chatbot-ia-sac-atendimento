import sys
import os
import json

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(r"C:\rpa\Python")
from Classes.Postgres.Postgres.ConectaPG import ConectaPG
from Classes.Oracle.Oracle.ConectaOracle import ConectaOracle
from Classes.ZimbraMailer.ZimbraMailer.Zimbra import ZimbraMailer
from acessaEmailSAC import process_emails_api, mover_email_entre_labels, authenticate_gmail, responder_email_api_duvida
from dotenv import load_dotenv, find_dotenv
import google.generativeai as genai
from groq import Groq
from datetime import datetime, timedelta
import requests
import time


# Escopos desejados (leitura + marcação de e-mails)
SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

def envia_email_erro(assunto, corpo, erro):
    pass # Logica de negocio removida por seguranca corporativa

def busca_data(days=1):
    pass # Logica de negocio removida por seguranca corporativa



def is_maior_que_3_dias_uteis(data_emissao_str):
    pass # Logica de negocio removida por seguranca corporativa



def verifica_cnpj(codigo_cliente):
    pass # Logica de negocio removida por seguranca corporativa



def configura_valores_sheet(retorno_devolucao, numero_nf, motivo_devolucao, codigo_produto, ean_produto, descricao_produto, quantidade_devolver, data_emissao, lote_caixa, numero_protocolo_laboratorio, codigo_cliente, cnpj, email, lote_nota_fiscal, numero_protocolo_distribuidora, tipo_avaria, numero_chamado, assunto_email, data):
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



def verifica_itens_groq(descricao_mercadoria_cliente, dict_itens):
    pass # Logica de negocio removida por seguranca corporativa

def verifica_solicitacao_item_por_pk(pk):
    pass # Logica de negocio removida por seguranca corporativa



def verifica_solicitacoes_email():
    pass # Logica de negocio removida por seguranca corporativa



if __name__ == "__main__":
    verifica_solicitacoes_email()