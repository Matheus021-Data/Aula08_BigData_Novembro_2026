vendas = []

for i in range(2):
    vendidos = float(input('Quanto foi vendido: '))
    vendas.append(vendidos)
    print(vendas)

total = sum(vendas)
quantidade = len(vendas)

print(f'\nO total de vendas: {total}')
print(f'A quantidade vendida: {quantidade}')

#inserir venda

inserir_venda = float(input('Qual número deseja inserir? '))
vendas.insert(0,inserir_venda)
print(f'Venda inserida: {vendas}')
print('A posição')

