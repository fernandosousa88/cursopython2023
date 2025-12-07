"""
Iterando strings com while
"""
#       012345678910
# nome = 'Luiz Otávio'  # Iteráveis
#      1110987654321

nome_fernando = 'Fernando'
indice_fernando = 0
novo_nome_fernando = ''

while indice_fernando < len(nome_fernando):
    letra_fernando = nome_fernando[indice_fernando]
    novo_nome_fernando += f'*{letra_fernando}'
    indice_fernando += 1


novo_nome_fernando += '*'
print(novo_nome_fernando)

nome = 'Maria Helena'  # Iteráveis

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)
