# # frase = 'aaaooo'
# # i = 0

# # qtd_mais_vezes = 0
# # letra_que_mais_apareceu = ''

# # while i < len(frase):
# #     letra_atual = frase[i]

# #     if letra_atual == 'o' or letra_atual == ' ' :
# #         i+=1
# #         continue

# #     qtd_apareceu_atual = frase.count(letra_atual)

# #     if qtd_mais_vezes < qtd_apareceu_atual:
# #         qtd_mais_vezes = qtd_apareceu_atual
# #         letra_que_mais_apareceu = letra_atual

# #     print(letra_atual, qtd_apareceu_atual)

# #     i+=1

# # print(f'A letra que mais apareceu foi "{letra_que_mais_apareceu}" {qtd_mais_vezes}x')





# # Texto_teste = 'Fernando'
# # iterador = iter(Texto_teste)

# # while True:
# #     try:
# #         letra = next(iterador)
# #         print(letra)
# #     except StopIteration:
# #         break        



# palavra_secreta = 'amoreco'
# letras_acertadas = ''
# qtd_tentativas = 0

# while True:
#     letra_digitada = input('Escolha uma letra: ')
#     qtd_tentativas += 1

#     if len(letra_digitada) > 1:
#         print('Digite apenas uma letra')
#         continue

#     if len(letra_digitada) == 0:
#         print('Digite a letra')
#         continue

#     if letra_digitada in palavra_secreta:
#         letras_acertadas += letra_digitada

#     palavra_formada = ''
#     for letra_secreta in palavra_secreta:
#         if letra_secreta in letras_acertadas:
#             palavra_formada += letra_secreta
#         else:
#             palavra_formada += ('*')
#     print(palavra_formada)

#     if palavra_formada == palavra_secreta:
#         print('O jogo acabou !')

#     continue


    

frase = 'O python é uma linguagem de programação multiparadigma. Python foi criado por Guido Van Rossum.'

print(frase.count('uma'))

i = 0
letra_nova = ''
for letra in frase:
    letra_nova += '*'
    print(letra)
    i += 1
print(letra_nova)



