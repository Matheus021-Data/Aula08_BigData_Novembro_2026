produtos = [] #lista

for i in range(3):
    produto = input('Informe o nome do produto: ') #cria muma variaável que usuário digita e adiciona na lista produtos
    produtos.append(produto) #método que adiciona no final da sua lista 

print(produtos)

#Acesso ao elemento

# n = int(input('Digite a posição do elemento a acessar: '))
# print(produtos[n-1])


# #Trocando o nome de um elemento na lisa
# produtos[n-1] = input('Informe o nome do outro elemento na posição: ') #2
# print(produtos)

# #remover  da lista
# produto_a_remover = input('\nDigite o nome do produo a remover: ')

# if produto_a_remover in produtos:
#     produtos.remove(produto_a_remover)

# print(produtos)