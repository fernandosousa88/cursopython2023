"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
# """
# Resolução Fernando
# 
# valor = input('Digite um número inteiro: ')

# if valor.isdigit():
#     valor_int = int(valor)
#     if valor_int % 2 == 0:
#         print(f'O número {valor_int} é par')
#     else:
#         print(f'O número {valor_int} é impar')
# else:
#     print('Você não digitou um número inteiro')

# entrada = input('Digite um número: ')

# if entrada.isdigit():
#     entrada_int = int(entrada)
#     par_impar = entrada_int % 2 == 0
#     par_impar_texto = 'ímpar'

#     if par_impar:
#         par_impar_texto = 'par'

#     print(f'O número {entrada_int} é {par_impar_texto}')
# else:
#     print('Você não digitou um número inteiro')

# try:
#     entrada_int = float(entrada)
#     par_impar = entrada_int % 2 == 0
#     par_impar_texto = 'ímpar'

#     if par_impar:
#         par_impar_texto = 'par'

#     print(f'O número {entrada_int} é {par_impar_texto}')
# except:
#     print('Você não digitou um número inteiro')
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
# Resolução Fernando
# # 
# horario = input('Informe a hora: ') 

# if horario.isdigit():
#     horario_int = int(horario)
#     if horario_int >= 0 and horario_int <= 11:
#         print('Bom dia')
#     elif   horario_int >= 12 and horario_int <= 17:
#         print('Boa tarde')
#     else:
#         print('Boa noite')
# else:
#     print('Você não digitou um horário')


# entrada = input('Digite a hora em números inteiros: ')

# try:
#     hora = int(entrada)

#     if hora >= 0 and hora <= 11:
#         print('Bom dia')
#     elif hora >= 12 and hora <= 17:
#         print('Bom tarde')
#     elif hora >= 18 and hora <= 23:
#         print('Bom noite')
#     else:
#         print('Não conheço essa hora')
# except:
#     print('Por favor, digite apenas números inteiros')
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
# Resolução Fernando
# 
nome_usuario = input('Escreva seu nome: ')

if len(nome_usuario) > 7:
    print('Seu nome é muito grande')
elif len(nome_usuario) > 5:
    print('Seu nome é normal')
else:
     print('Seu nome é curto')   


nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Digite mais de uma letra.')
