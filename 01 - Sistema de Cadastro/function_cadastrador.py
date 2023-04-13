# DICIONÁRIOS PARA TESTES
x = {'nome' : 'thiago', 'cor' : 'azul', 'idade' : 30}
x.copy()
print(x)

# LOOP CRIADOR DE CATEGORIA DE DADOS:
def loop_insert_data():

    lista_categorica = []

    while True:
        decision = input('Acrescentar Informação? "sim" ou "nao"\n')

        if decision == 'nao':
            break

        lista_categorica.append(input('Qual categoria de informação deseja acrescentar?\n'))

    return lista_categorica

# LISTA DE CATEGORIAS CRIADAS PELO LOOP
insertCateg = loop_insert_data()

# ACRESCENTADOR DE CATEGORIAS EM DICIONÁRIOS
getx = lambda : x.update(x.fromkeys(insertCateg, 'empty'))
getx()

# PRINT DE DICIONÁRIO MODIFICADO APÓS A INCLUSÃO DE NOVA CATEGORIA
print(x)



# GERADOR DE CATEGORIAS TERMINADO
# A IDEIA AGORA É:
#       MANIPULAR OS DADOS DOS DICIONÁRIOS
#       MODIFICAR AS CATEGORIAS JÁ CRIADAS
#       MANTER ESTE ARQUIVO COMO DE FUNÇÕES PRINCIPAIS
#       FAZER NOVO ARQUIVO PARA ARMAZENAMENTO DE CADASTROS
#       LINKar OS ARQUIVOS PARA QUE ESTE MODIFIQUE O ARMAZENAMENTO DE DADOS
