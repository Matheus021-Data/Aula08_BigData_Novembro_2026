#TUPLAS
#Coleção imutável
#Permitir elementos duplicados
#Permite acesso ao indice
#Mantém a ordem da inserção

frutas = ('Maçã', 'Uva','Manga', 'Pera', 'Melancia') #tuplas
print(type(frutas))
print(frutas)
print(frutas[1])
print(frutas.index('Pera'))

#frutas[1] = 'Melancia' #A TUPLA NÃO PODE SER ALTERADA

numeros = (5, 7, 1, 9, 10, 20, 30, 50, 80,20)
print(numeros.count(20)) #quantas vezes aparece o número 20
print(type(numeros))
