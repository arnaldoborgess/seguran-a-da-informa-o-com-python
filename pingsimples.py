import os # importa o módulo ou biblioteca os (integra programas ou recursos do sistema)_clear()

print("#" * 60)

ip_ou_host = input("Digite o IP ou host a ser verificado: ") # criando uma variável que recebe do usuário o IP.
print("_" * 60)
os.system('ping -n 6 {}'.format(ip_ou_host)) # chamando o método system da bliblioteca os chamando o comando ping com 6 pacotes virão do IP {}
print("_" * 60)
