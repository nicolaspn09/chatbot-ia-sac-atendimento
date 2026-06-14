import os
import streamlit as st
import pandas as pd
import re # Para validar o input
from ConectaOracle import ConectaOracle # Importe a classe local

st.set_page_config(page_title="Consulta de Ocorrências", layout="wide")

# --- SEGURANÇA: LOGIN NATIVO COM SECRETS ---
def check_password():
    pass # Logica de negocio removida por seguranca corporativa
