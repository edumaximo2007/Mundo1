print('-=-'*10)
print('''\033[7m         DESAFI0 15             \33[m''')
print('-=-'*10)
print('\033[1mEscreva um programa que pergunte a quantidade de Km percorrido por um carro alugado e \na quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo queo carro custa R$60 por dia e R$0,15 por Km rodado.\033[m')
print('-=-'*40)
print('Preencha o formulário abaixo para prosseguir.')
print('')
print('Digite o nome e sobrenome nos campos abaixo.')
no = str(input('nome: ')).strip()
sn = str(input('Sobrenome: ')).strip()
print('')
print('Informe o dia, mês e o ano do nascimento.')
dia = input('Dia do nascimento: ')
m = str(input('Mês: '))
a = int(input('Ano: '))
print('')
print('E-mail cadastrado.')
e = str(input('e-mail: ')).strip()
print('')
print('\033[1mTABELA DE PREÇOS\033[m')
print('')
print('Fiat Palio 2021 \033[1mR$90,00\033[m dia, custo KM \033[1mR$0.40\033[m')
print('Corsa 2020 \033[1mR$80,00\033[m dia, Km custo \033[1mR$0.30\033[m')
print('Gol G7 2021 \033[1mR$100,00\033[m dia, km custo \033[1mR$0.80\033[m')
print('Fiat Mobi 2020 \033[1mR$60,00\033[m dia, km custo \033[1mR$0.15\033[m')
print('')
v = float(input('Informe o valor do veiculo alugado:R$'))
v1 = int(input('Infome o número de dias de locação do veiculo: '))
v2 = float(input('Informe o km anterior: '))
v3 = float(input('Informe a km atual: '))
v4 = float(input('Custo por Km rodado do veiculo locado:R$'))
print('')
n = v*v1
n1 = v3-v2
n2 = (v4*n1)+n
print('Esse veiculo utilizou \033[1m{}Km\033[m o valor a ser pago com a diaria e de \033[1mR${:.2f}\033[m '.format(n1, n2))
print('')
print('Por favor confira se os dados acima estão corretos antes de proseguir com o pagamento')
