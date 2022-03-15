import socket
import sys # fornrcr acesso e variaveis e funcoes do interpretador

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) # AF_INET informa que será utilizado o protocolo IP. SOCK.STREAM informa que utilizaremos TCP.
    except socket.error as e:
        print("A conexão falhou!!!")
        print("Erro^: {}".format(e))
        sys.exit() # sai do programa

    print("Socket criando com sucesso.")

    HostAlvo = input("Digite o host ou ip a ser conectado: ")
    PortaAlvo = input("Digite a porta a ser concetada: ")

    try:
        s.connect((HostAlvo, int(PortaAlvo)))
        print("Cliente TCP conectado com sucesso no Host" + HostAlvo + " e na Porta: " + PortaAlvo)
        s.shutdown(2)
    except socket.error as e:
        print("Não foi possível conectar ao Host: " + HostAlvo + " -Porta: " + PortaAlvo)
        print("Erro: {}".format(e))
        sys.exit

if __name__ == "__main__":
    main()