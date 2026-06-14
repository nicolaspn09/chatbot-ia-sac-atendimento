import sys

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(r"C:\rpa\Python")
from leEmailSac import main as le_email
from identificaTipoSolicitacao import verifica_solicitacoes_email
from efetuaRegistroSac import main as efetua_registro
from efetuaRegistroSacAgrupado import main as efetua_registro_agrupado
from movimentaInbox import main as movimenta_inbox
from leEmailSacDevPortal import processa_emails as le_email_sac_dev_portal
from Classes.ZimbraMailer.ZimbraMailer.Zimbra import ZimbraMailer


def envia_email(assunto, corpo, erro):
    pass # Logica de negocio removida por seguranca corporativa



def main():
    pass # Logica de negocio removida por seguranca corporativa



if __name__ == "__main__":
    # Executa a função principal
    main()