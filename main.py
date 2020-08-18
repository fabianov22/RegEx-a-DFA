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
            aux = s.format_string(string)
            head = 0
            val = [True, True, True, True]
            cont_val = [0, 0, 0, 0]
            for i in aux:
                s.value_format = i
                if s.validate_token_id() and val[0]:
                    val[0] = True
                    cont_val[0] += 1
                else:
                    val[0] = False
                    head = cont_val[0]

                if s.validate_token_num() and val[1]:
                    val[1] = True
                    cont_val[1] += 1
                else:
                    val[1] = False

                if s.validate_token_op_arit() and val[2]:
                    val[2] = True
                    cont_val[2] += 1
                else:
                    val[2] = False

                if s.validate_token_op_asign() and val[3]:
                    val[3] = True
                    cont_val[3] += 1
                else:
                    val[3] = False
                head += 1
            print(val)
            print(cont_val)
        else:
            exit()
