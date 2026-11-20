numeros = []

print('QUANDO TERMINAR DE DIGITAR POR FAVOR DIGITE [S]')

while True:
    n = int(input('\nDigite qual número inteiro: '))
    numeros.append(n)
    
    resposta = input('\nTerminou de digitar [S/N]: ').upper() 
    
    if resposta == 'S'.upper():
        print(numeros)
        break

total = sum(numeros)
quatidade = len(numeros)
ordem = sorted(numeros)

print(f'Total: {total}')
print(f'Quantidade: {quatidade}')


