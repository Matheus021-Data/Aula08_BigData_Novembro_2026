#set "conjuntos"
#coleção mutável
#não garante ordem
#não indice
#NÃO PERMITE DUPLICADOS 

#criar sets vazios

dias = set()
dias.add('Segunda')
dias.add('Terça')
print(dias)

#conjunto inicializados
frutas = {'Maçã', 'Uva','Manga', 'Pera', 'Melancia'}
print(frutas)
print(type(frutas))

#remover pode usar o remove
frutas.discard('Uva')
print(frutas)

#contar
print(len(frutas))

#converter listas em sets
# lista = [5, 7, 1, 9, 10, 20, 30, 50, 80]
# conjunto_set = set(lista)
# print(conjunto_set)

lista = [5, 7, 1, 9, 10, 20, 30, 50, 80,50,80,50,50,50,80,80]
conjunto = set(lista) #converter para ser e dar para fazer para lista também
print(conjunto)
print(len(conjunto))
