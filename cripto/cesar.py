#Esse programa cifrar e decifrar uma mensagem, permitindo utilizar a cifra de cesar.


#Exemplo de uso:

#Entrada: INTERNET OF THINGS

#Processo: cifrar
#Chave: 6
#Texto: Entrada
#Saída: OTZKTZ UL ZNOTMY

#Entrada: BNQNMZ

#Processo: decifrar
#Chave: -1
#Texto: Entrada
#Saída: CORONA


def cesar_cipher(process, key, text):
    result = ""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for char in text:
        if char.isupper() and char in alphabet:
            index = alphabet.index(char)
            if process.lower() == "cifrar":
                new_index = (index + key) % 26
            else:  # decifrar
                new_index = (index - key) % 26
            result += alphabet[new_index]
        else:
            result += char
    return result

def main():
    process = input("Digite o processo (cifrar/decifrar): ")
    key = int(input("Digite a chave (inteiro): "))
    text = input("Digite o texto: ")
    result = cesar_cipher(process, key, text)
    print("Resultado:", result)

if __name__ == "__main__":
    main()


    