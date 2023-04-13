x = ["THIAGO", "SARA", "ADRIANA", "RONALDO", "HIGOR"]
y = []

print(f'Este é o x antes do append: {x}.')
print(f'Este é o y antes do append: {y}.')

tamanho = len(x)

for i in range(tamanho):
    y.append(x.pop(0))


print(f'Este é o y APÓS o append: {y}.')

print(f'Este é o x APÓS o append: {x}.') 

""" lista = []
print('Digite um nome ou sair:')

while True:
    
    nome = input()

    if nome == 'sair':
        break
    else:
        lista.append(nome)

print(lista)

listaAnimal = []
print('Indique um animal ou exit:')

for i in range(3):
    
    animal = input()
    if animal == 'exit':
        break
    else:
        listaAnimal.append(animal) 
        

print(listaAnimal) """


""" learnlist = []
x = [learnlist.append(input('Digite o nome dos gatinhos: ')) for i in range(0, 3)]
print(learnlist) """