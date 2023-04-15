# DICIONÁRIOS PARA TESTES
x = {'nome' : 'thiago'}
print('Seja Bem Vindo ao Cadastrador de Dados')

# LOOP CRIADOR DE CATEGORIA DE DADOS:
def loop_insert_data():

    lista_categorica = []

    while True:
        decision = int(input('Acrescentar Informação?\n[1] SIM ----- [2] NÃO\n'))

        if decision == 2:
            break

        lista_categorica.append(input('Qual categoria de informação deseja acrescentar?\n'))

    return lista_categorica

# INTERFACE INICIAL DO PROGRAMA:
def inicial_interface():
    # SISTEMA DE CONTROLE DE ERROS: TRY e EXCEPT
    try:
        while True:
            # OPÇÕES NA INTERFACE INICIAL
            wantDo = int(input('O que deseja fazer?\n[1] ADD NOVAS CATEGORIAS DE DADOS ----- [2] MANIPULAR DADOS ----- [3] APAGAR DADOS ----- [4] FECHAR PROGRAMA'))
            if wantDo == 1:
                # LISTA DE CATEGORIAS CRIADAS PELO LOOP
                listCategory = loop_insert_data()

                # ACRESCENTADOR DE CATEGORIAS EM DICIONÁRIOS
                addCategory = lambda : x.update(x.fromkeys(listCategory, 'empty'))

                addCategory()
            elif wantDo == 4:
                print('-'*30 )
                print('\nCadastrador finalizado. Até a próxima!')
                break            
        
    except Exception as errorWantDo:
        print('-'*30)
        print(f'{errorWantDo}')
        print('COLOQUE UM CÓDIGO VÁLIDO')
        print('-'*30)
        inicial_interface()
    

# EXECUÇÃO DAS FUNÇÕES E PRINTS
x.copy()
print(x)
inicial_interface()
print('-'*30 )
print(f'\nEstas são as novas categorias de dados:\n{x}')



# GERADOR DE CATEGORIAS TERMINADO
# OPÇÕES DE INTERFACE TERMINADA
# A IDEIA AGORA É:
#       MANIPULAR OS DADOS DOS DICIONÁRIOS
#       MODIFICAR AS CATEGORIAS JÁ CRIADAS
#       MANTER ESTE ARQUIVO COMO DE FUNÇÕES PRINCIPAIS
#       FAZER NOVO ARQUIVO PARA ARMAZENAMENTO DE CADASTROS
#       LINKar OS ARQUIVOS PARA QUE ESTE MODIFIQUE O ARMAZENAMENTO DE DADOS
