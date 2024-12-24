
alfabet = ['a','b','c','d','e','f','g','h', 'i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
cifra = 3
repetir = 1

def cesar(mensagem):
    global cifra
    vet = []
    vet_criptografada = []
    texto_cifrado = []
    z = ''
    try:
        for i in range(mensagem.count('',1, 999999)):
            try: 
                x = str(alfabet.index(f'{mensagem[i]}'))
            except:
                if x.isnumeric: 
                    pass
                x = str(mensagem[i])
                pass
            vet.append(x)
        for item in vet:
            try:
                vet_criptografada.append(int(item)+cifra)
            except:
                vet_criptografada.append(' ')
        for caracter in vet_criptografada:
            try:
                texto_cifrado.append(alfabet[caracter])
            except:
                texto_cifrado.append(' ')
        for caract in texto_cifrado:
            z += caract
        if cifra >0:
            return print(f'\nA mensagem criptografada é: {z}')
        else:
            return print(f'\nA mensagem descriptografada é: {z}')
    except:
        pass

def main():
    global cifra, repetir
    while repetir == 1:
        try:
            opcao = int(input("Cifra de Cesar Por Julio Melo\n\nDigite oque deseja fazer:\n[1] - Criptografar\n[2] - Descriptografar\n\nDigite: "))
        except:
            pass
        if opcao == 1:
            cifra = 3
            cesar(mensagem=str(input("Digite a mensagem que deseja codificar: ")))
        elif opcao ==2:
            cifra = -3
            cesar(mensagem=str(input("Digite a mensagem que deseja decodificar: ")))
        else:
            print("Opcao não identificada tente novamente")
        try:
            repetir = int(input("\nDeseja executar novamente?\n[1] - Sim\n[2] - Não\n\nDigite: "))
        except:
            pass


if __name__ == __name__:
     main()
