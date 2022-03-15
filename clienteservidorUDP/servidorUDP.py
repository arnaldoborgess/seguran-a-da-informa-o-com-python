import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Socket Criado com Sucesso.")

host = "localhost"
port = 5432

s.bind((host, port)) # faz a ligação entre cliente e servidor através do host e da porta
mensagem = "Servidor: Oláaaaa Cliente e ai beleza?"

while 1:
    dados, end = s.recvfrom(4096)

    if dados:
        print("Servidor enviando mensagem...")
        s.sendto(dados + (mensagem.encode(), end))
