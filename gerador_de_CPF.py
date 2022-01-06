from random import randint
# Gerador de CPF (Matematicamente Válido)

num = str(randint(100000000, 999999999))        # Gerar um valor randomico dos primeiros 9 dígitos do CPF
novo_cpf = num

contagem_reversa_1 = 11                 # Contagem reversa para multiplicação (Digito 1)
contagem_reversa_2 = 12                 # Contagem reversa para multiplicação (Digito 2)
total_1 = 0                             # Acúmulo total dos valores para a primeira operação
total_2 = 0                             # Acúmulo total dos valores para a segunda operação

#Descobrir o primeiro digito pós os 9 iniciais

for i in range(9):
    contagem_reversa_1 -= 1                 # Contagem reversa regredindo
    total_1 += int(novo_cpf[i]) * contagem_reversa_1
    digito_1 = 11 - (total_1 % 11)          # Formula para encontrar o primeiro digito

    if digito_1 > 9:
        digito_1 = 0

novo_cpf_1 = novo_cpf + str(digito_1)        # Transformando a variavel digito_1 em string

for m in range(10):
    contagem_reversa_2 -= 1                  # Contagem reversa regredindo
    total_2 += int(novo_cpf_1[m]) * contagem_reversa_2
    digito_2 = 11 - (total_2 % 11)
    if digito_2 > 9:
        digito_2 = 0


novo_cpf_final = novo_cpf_1 + str(digito_2)

print(novo_cpf_final)                         # Mostrar na tela o CPF gerado