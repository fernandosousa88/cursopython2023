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

import os

lista = []
# opcao = input('Selecione uma opção: ')

while True:
    print('Selecione uma opção: ')
    opcao = input('[i]nserir, [a]pagar, [l]istar ')

    if opcao.startswith('i'):
        os.system('clear')
        valor = input('Digite o item que gostaria de inserir: ')
        lista.append(valor) 

    if opcao.startswith('a'):
        os.system('clear')
        valor = input('Digite o item que gostaria de alterar: ')


    if opcao.startswith('l'):
        os.system('clear')
        print(enumerate(lista))

