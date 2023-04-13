# APRENDIZADO EM SISTEMAS DE CADASTRO UTILIZANDO:
#       DICIONÁRIOS E LISTAS
#       LOOPs: WHILE e FOR


# SISTEMA DE CADASTRO COM DICIONÁRIOS DENTRO DE LISTA
# O WHILE ESTA MANTENDO O CADASTRO EM LOOP; E
#              PREENCHENDO OS DICIONÁRIO DENTRO DA LISTA
# O FOR ESTA IMPRIMINDO EM LOOP COM A FORMATAÇÃO INTERNA DEFINIDA.

"""
produto = [{'empty'}]


while True:
    cadastro = int(input('Cadastrar: 1 ----- Sair: 2'))

    if cadastro == 2:
        break

    marca = input('Digite a Marca:').upper()
    preco = float(input('Digite o Preço:'))
    ano = int(input('Digite o Ano:'))

    produto.append({'marca': marca, 'preco': preco, 'ano': ano })

for i in range(1, len(produto)):

    print(f'---------- CADASTRO {i} ----------')
    print(f"Carro: {produto[i]['marca']}\nAno: {produto[i]['ano']}\nPreço: R$ {produto[i]['preco']:.2f}")
    print('-'*32)
"""

# ------------------------------------------------


# SISTEMA DE CADASTRO COM DICIONÁRIOS DENTRO DE LISTA A PARTIR DO ANTERIOR
# DIFERENÇA SE ENCONTRA NA IMPRESSÃO DO FOR
# O FOR POSSUI UM FOR INTERNO QUE ESTA IMPRIMINDO EM LOOP COM A FORMATAÇÃO DEFINIDA NA KEY DO DICIONÁRIO.
produto = [{'empty'}]

while True:
    cadastragem = int(input('Cadastrar: 1 ----- Sair: 2'))

    if cadastragem == 2:
        break

    marca = input('Digite a Marca:').upper()
    preco = float(input('Digite o Preço:'))
    ano = int(input('Digite o Ano:'))

    produto.append({'Marca': marca, 'Preço': preco, 'Ano': ano })

for i in range(1, len(produto)):
    cadastro = produto[i]
    print(f'---------- CADASTRO {i} ----------')
    
    # ESTE É O LOOP FOR INTERNO QUE ESTA IMPRIMINDO
    # O DIFERENCIAL ESTA NA IMPRESSÃO COM UMA SÓ LINHA DE CÓDIGO, SIMPLICIDADE E EFETIVIDADE
    for j, l in cadastro.items():
        print(f"{j}: {l}")

    print('-'*32)
        