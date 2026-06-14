import time
from datetime import datetime
from gravaDevolucaoSistema import main
from informaRetornoSoftDesk import verifica_dados_planilha


# Chama o código que grava os dados de devolução no sistema
main()

time.sleep(10)

# Verifica se o horário atual está entre 13:00 e 23:59
hora_atual = datetime.now().time()

# if hora_atual >= datetime.strptime("13:00", "%H:%M").time() and hora_atual <= datetime.strptime("23:59", "%H:%M").time():

# Chama o código que responde no sistema da Clamed
verifica_dados_planilha()

# else:
#     print("Horário fora do intervalo permitido para execução do script de resposta no SoftDesk.")