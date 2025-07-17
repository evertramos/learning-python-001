
# Writen by Evert Ramos

# Import print functions
from utils.print import sucesso, aviso, padrao, erro, pergunta

# Escrever suas funções aqui
def jogar():
    resultado = pular_nuvens([0, 0, 1, 0, 0, 1, 0])
    print('Resultado teste 1:', resultado)
    resultado = pular_nuvens([0, 0, 0, 0, 1, 0])
    print('Resultado teste 2:', resultado)

# Pular Nuvem
def pular_nuvens(nuvens):
    saltos = 0
    indice = 0
    while indice < (len(nuvens) - 2):
        # Pula no máximo duas nuvens
        if nuvens[indice +2] != 1:
            indice += 2
        else:
            indice += 1
        saltos += 1
    return saltos
    

# Menu da aplicação
while True:
    print()
    padrao('Menu Principal:')
    padrao('1. Jogar')
    # padrao('2. Opção 2')
    padrao('0. Sair')
    print()
    padrao('00. Para sair em qualquer tela!')
    print()

    try:
        escolha = int(pergunta('Escolha uma opção: '))
        print('<fim [Menu]')
        print() 
    except ValueError:
        erro('Entrada inválida, por favor insira um número.')
        continue

    if escolha == 0:
        break
    elif escolha == 1:
        jogar()
    # elif escolha == 2:
        # print('Você escolheu a Opção 2.')
    else:
        print('Opção inválida, tente novamente.')

print('Programa encerrado.')