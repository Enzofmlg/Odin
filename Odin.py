# Odin - | Brute Force |
# code by ZNO
from itertools import product


def gerar_caracteres():
    return [chr(i) for i in range(97, 123)] + [chr(i) for i in range
                                               (65, 91)] + [chr(i) for i in range(48, 58)]


def forca_bruta(chars, senha, len_senha):
    tentativa = 0
    for comb in product(chars, repeat=len_senha):
        combina = ''.join(comb)
        tentativa += 1
        if (tentativa % 500000 == 0):
            print(f'{tentativa:10} -->{combina}')
        if senha == combina:
            return f'Senha encontrada é"{combina}", após {tentativa} tentativas.'
    return 'Senha NAO encontrada'


tentativa = 0


def forca_bruta_recursiva(chars, senha, len_senha, comb_anterior=''):
    global tentativa
    for letra in chars:
        combina = comb_anterior + letra
        tentativa += 1
        if (tentativa % 500000 == 0):
            print(f'{tentativa:10} --> {combina}')
        if senha == combina:
            print(
                f'Senha encontrada é "{combina}", após {tentativa} tentativas.')
            exit()
        elif (len_senha != 1):
            forca_bruta_recursiva(chars, senha, len_senha-1, combina)


def main():
    chars = gerar_caracteres()
    # <- Coloque a senha que deseja que o software quebre aqui.
    senha = 'lol9@'
    print(forca_bruta(chars, senha, len_senha=4))
    print('*' * 60 + '\n')
    print(forca_bruta_recursiva(chars, senha, len(senha)))
    print('*' * 60 + '\n')
    print(forca_bruta_recursiva(chars, 'cabo', 4))
    print('*' * 60 + '\n')
    print(forca_bruta_recursiva(chars, 'cabo', 5))


if __name__ == "__main__":
    main()
