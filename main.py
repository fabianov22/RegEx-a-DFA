from models.identify_sentence import Sentence
from models.identity_token import Token
if __name__ == '__main__':
    vEntr = []
    while True:
        option = 0
        while option != 2 and option != 1:
            print("Reconocimiento de Tokens")
            print("[1] Ingresar Entrada")
            print("[2] Salir")
            option = input(" > ")
            if option.isdigit() and 1 <= int(option) <= 2:
                option = int(option)
            else:
                print("[!] Error: Opcion no valida")
                option = -1
        if option == 1:
            string = input("String de entrada > ")
            s = Token()
            s.format_string(string)
            s.split_add_vtokens
            s.verified_tokens
            print(s.value_format)
            print(s.vtokens)

        else:
            exit()
