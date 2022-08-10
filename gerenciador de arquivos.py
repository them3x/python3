import os, hashlib, pyaes

def encrypt(arquivos):

    for arquivo in arquivos:
        with open ("seguro/" + arquivo, "rb") as f:
            file = f.read()
        f.close()

        aes = pyaes.AESModeOfOperationCTR(hash_senha.encode("UTF-8"))
        data_encript = aes.encrypt(file)

        with open("seguro/" + arquivo + ".nck", "wb") as novo_arquivo:
            novo_arquivo.write(data_encript)
        novo_arquivo.close()
        os.remove("seguro/" + arquivo)

def decrypt(arquivos):
    for arquivo in arquivos:
        with open("seguro/" + arquivo, "rb") as f:
            file = f.read()

        f.close()

        aes = pyaes.AESModeOfOperationCTR(hash_senha.encode("UTF-8"))
        data = aes.decrypt(file)

        with open("seguro/" + arquivo.replace(".nck", ""), "wb") as novo_arquivo:
            novo_arquivo.write(data)
        novo_arquivo.close()
        os.remove("seguro/" + arquivo)


def listar_encriptados():
    crip = "./seguro/"
    caminho = os.listdir(crip)

    paradecript = []

    for achado in caminho:
        extensao = os.path.isfile(crip + achado)

        if extensao == True:
            if achado.split('.')[-1] == "nck":
                paradecript.append(achado)
        else:
            print("Arquivos decriptados!",)
    return paradecript


def listar_arquivos():
    crip = "./seguro/"
    caminho = os.listdir(crip)

    paracript = []

    for achado in caminho:
        extensao = os.path.isfile(crip + achado)

        if extensao == True:
            if achado.split('.')[-1] != "nck":
                paracript.append(achado)
        else:
            print("Todos os arquivos foram criptografados, exceto as pastas que não podem ser criptografadas!")
    return paracript

def alterar_senha():
    def lapis(var1):
        arquivo = open("arquivos/senha.txt", "w")
        arquivo.write(var1)
        arquivo.close()

    while True:
        senha1 = input("Digite sua senha: ")
        senha2 = input("Digite a senha novamente: ")
        tamanho = len(senha1)
        if tamanho > 7:
            if senha1 == senha2:
                hash_senha = hashlib.sha512(senha2.encode("UTF-8")).hexdigest()
                print("Senha alterada com sucesso!")
                lapis(hash_senha)
                break

            else:
                print ("As senhas não conferem")
        else:
            print("A senha precisa de no minimo 8 digitos")

def menu():
    while True:
        print("1) Descriptografar arquivos\t\t3)Alterar senha\n2) Criptografar arquivos\t4)Sair \n")
        resposta = input("-->  ")

        if int(resposta) == 1:
            arquivo = listar_encriptados()
            decrypt(arquivo)

        elif int(resposta) == 2:
                arquivo = listar_arquivos()
                encrypt(arquivo)

        elif int(resposta) == 3:
                alterar_senha()

        elif int (resposta) == 4:
                print("Usuario saiu")
                exit(0)
        else:
            print("Não achei essa opçao.")
            menu()

def login():

    tentativas = 3
    
    global hash_senha
    
    while tentativas > 0:
        file = open("arquivos/senha.txt", "r")
        read = file.read().replace("\n", "")
        senha = input("digite sua senha: ")
        hash_senha = hashlib.sha512(senha.encode("UTF-8")).hexdigest()
        
        if hash_senha == read:
            menu()
            tentativas = 0
        else:
            print ("Senha incorreta! Por favor tente novamente.")
            print ("Tentativas restantes" , tentativas)
        tentativas = tentativas - 1


login()
