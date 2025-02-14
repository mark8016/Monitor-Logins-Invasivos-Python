import re

def monitor_log_file(logfile):
    """
    Função para monitorar o arquivo de log de autenticação em busca de tentativas de login falhas.
    :param logfile: Caminho para o arquivo de log
    :return: None
    """
    with open(logfile, "r") as file:
        logs = file.readlines()
    
    for line in logs:
        if "Failed password" in line:
            ip = re.findall(r"from (\S+)", line)
            if ip:
                print(f"Tentativa de login falha detectada de {ip[0]}")

# Exemplo de uso: Monitorando o log de autenticação (arquivo syslog, por exemplo)
logfile = "/var/log/auth.log"  # Caminho do log de autenticação em sistemas Linux
monitor_log_file(logfile)
