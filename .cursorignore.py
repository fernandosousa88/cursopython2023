# # qtd_linhas = 5 
# # qtd_colunas =  50
# # linha = 1


# # while linha <=  qtd_linhas:
# #     coluna = 1
# #     while coluna <= qtd_colunas:
# #         print(f'{linha=} {coluna=}')
# #         coluna += 1
# #     linha += 1

# # print('Acabou!')


# # nome = 'Theresa Cristina'
# # indice = 0
# # tamanho_nome = len(nome)
# # novo_nome = ''


# # while indice < tamanho_nome:
# #     letra = nome[indice]
# #     # print(letra)
# #     novo_nome += f'*{letra}'
# #     # print('*', novo_nome)
# #     indice += 1
# # # novo_nome += '*'
# # print(novo_nome)


# # frase = 'O python é uma linguagem de programação multiparadigma. Python foi criado por Guido Van Rossum.'
# # i = 0
# # qtd_apareceu_mais_vezes = 0
# # letra_apareceu_mais_vezes = ''
# # # print(frase.count('i'))

# # while i < len(frase):
# #     letra_atual = frase[i]
# #     if letra_atual == ' ':
# #         i += 1
# #         continue

# #     qtd_letra = frase.count(letra_atual)
# #     # print(letra_atual, qtd_letra)
# #     if qtd_apareceu_mais_vezes < qtd_letra:
# #             qtd_apareceu_mais_vezes = qtd_letra
# #             letra_apareceu_mais_vezes = letra_atual
# #     i += 1
# # print(f'A letra foi "{letra_apareceu_mais_vezes}" foi a que apareceu mais vezes. \
# #      No total foram "{letra_apareceu_mais_vezes}" vezes')

# from cgi import print_arguments
# from cgitb import text


# texto = 'Fernando'
# novo_texto = ''

# for letra in texto:
#     novo_texto += f'*{letra}'
#     print(letra)

# print(f'{novo_texto}*')


# qtd_linhas = range(1,5)
# qtd_colunas = range(0,10)
# i = 0
# coluna = 0

# for linha in qtd_linhas:
#     if linha == 1:
#         print('Pulando')
        
#     for coluna in qtd_colunas:
#         print(linha, coluna)
#         coluna += 1     
#     i += 1

# import os
 
# palavra_secreta = 'fernando'
# letras_acertadas = ''
# tentativas = 0

# while True:

#     letra_digitada = input('Digite uma letra: ')
#     tentativas += 1

#     if len(letra_digitada) > 1:
#         print('Digite apenas uma letra')
#         continue

#     if letra_digitada in palavra_secreta:
#         letras_acertadas += letra_digitada
    
#     palavra_formada = ''
#     for letra_secreta in palavra_secreta:
#         # CORREÇÃO AQUI: Verificamos se está nas letras ACERTADAS
#         if letra_secreta in letras_acertadas:
#             palavra_formada += letra_secreta
#         else:
#             palavra_formada += '*'
            
#     print(palavra_formada, tentativas)

#     if palavra_formada == palavra_secreta:
#         os.system('clear')
#         print('Você ganhou! Parabéns')
#         print(f'A palavra era {palavra_formada}')
#         print(f'Tentativas {tentativas}')
#         letras_acertadas = ''
#         tentativas = 0
#         palavra_formada = ''


# lista = ['MARIA', 'HELENA', 'LUIZ']
# i = 0

# indicex = range(len(lista))

# print(indicex)

# for indice in lista:
#     print(lista[i], 'Seu indice é ' ,i)
#     i += 1


#----------------#
# import re
# import sys

# # Entrada de dados
# entrada = input("Informe seu CPF: ")

# # AJUSTE 1: Correção do Regex. Usar '^' e não 'ˆ'.
# # Isso remove tudo que não for número (pontos, traços, espaços).
# cpf_enviado = re.sub(
#     r'[^0-9]',
#     '',
#     entrada
# )

# # Verifica se a entrada tem dados suficientes ou se são números repetidos
# # (Ex: 111.111.111-11 passa no cálculo matemático, mas é inválido)
# input_repetido = cpf_enviado == cpf_enviado[0] * len(cpf_enviado)

# if input_repetido:
#     print('Você enviou dados sequenciais (ex: 111.111...). Isso é inválido.')
#     sys.exit() # Encerra o programa

# # Pega apenas os 9 primeiros dígitos para calcular
# nove_digitos = cpf_enviado[:9]
# contador_regressivo_1 = 10

# # --- Primeiro Dígito ---
# resultado_1 = 0
# for digito in nove_digitos:
#     resultado_1 += int(digito) * contador_regressivo_1
#     contador_regressivo_1 -= 1

# digito_1 = (resultado_1 * 10) % 11
# digito_1 = digito_1 if digito_1 <= 9 else 0

# # --- Segundo Dígito ---
# # dez_digitos = nove_digitos + str(digito_1)
# # contador_regressivo_2 = 11

# # resultado_2 = 0
# # for digito in dez_digitos:
# #     resultado_2 += int(digito) * contador_regressivo_2
# #     contador_regressivo_2 -= 1

# # digito_2 = (resultado_2 * 10) % 11
# # digito_2 = digito_2 if digito_2 <= 9 else 0

# # # Monta o CPF calculado baseado nos 9 primeiros números
# # cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

# # # Exibe o que foi calculado
# # # print(f'CPF calculado: {nove_digitos}-{digito_1}{digito_2}')

# # # AJUSTE 2: Compara o CPF limpo enviado pelo usuário com o calculado
# # if cpf_enviado == cpf_gerado_pelo_calculo:
# #     print(f'O CPF {entrada} é VÁLIDO')
# # else:
# #     print(f'O CPF {entrada} NÃO é válido')


# #----------------#
# # Gerador de cpf
# import re
# import sys
# import random

# # Entrada de dados
# for i in range(10):
#     nove_digitos = ''
#     for i in range(9):
#         nove_digitos += str(random.randint(0, 9))

#     contador_regressivo_1 = 10

#     # --- Primeiro Dígito ---
#     resultado_1 = 0
#     for digito in nove_digitos:
#         resultado_1 += int(digito) * contador_regressivo_1
#         contador_regressivo_1 -= 1

#     digito_1 = (resultado_1 * 10) % 11
#     digito_1 = digito_1 if digito_1 <= 9 else 0

#     # --- Segundo Dígito ---
#     dez_digitos = nove_digitos + str(digito_1)
#     contador_regressivo_2 = 11

#     resultado_2 = 0
#     for digito in dez_digitos:
#         resultado_2 += int(digito) * contador_regressivo_2
#         contador_regressivo_2 -= 1

#     digito_2 = (resultado_2 * 10) % 11
#     digito_2 = digito_2 if digito_2 <= 9 else 0

#     # Monta o CPF calculado baseado nos 9 primeiros números
#     cpf_gerado_pelo_calculo = f'{nove_digitos}-{digito_1}{digito_2}'
#     print(cpf_gerado_pelo_calculo)

#     #----------------#

# função para multiplicar todos os argumentos nào nomeados
# def multiplicar(*args):
#     total = 1
#     for numero in args:
#         total *= numero
#     return total

# teste = multiplicar(10, 20, 45)
# print(teste)

# def verfica(x):
#     return print(f'O número {x} é par') if x % 2 == 0 else print(f'O número {x} é ímpar')
#     # if x % 2 == 0:
#     #     return print('O número é par')
#     # else:
#     #     return print('O número é ímpar')


# teste_2 = verfica(568476841654684864)

pessoa = {}

pessoa['nome'] = 'Fernando'
pessoa['Sobrenome'] = 'Sousa'
pessoa['Idade'] = 37


# print(pessoa)
# print()

# print(pessoa['Idade'])
# print(pessoa['Idade1'])

print(pessoa.items(), type(pessoa))

d1 = ['a', 'b','c']

d2 = d1

print()
print(d1.reverse())
print(d2)