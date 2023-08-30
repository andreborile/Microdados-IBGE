import main
import pandas as pd

variaveis = main.extrair_variaveis('Data/dict_pessoas.xls')

colunas = [str(variavel) for variavel in variaveis]
linhas = []

with open('Data/PES2015.txt') as microdados:
    for idx, linha in enumerate(microdados):
        nova_linha = []
        for variavel in variaveis:
            valor = linha[variavel.posicao_inicial:variavel.posicao_inicial + int(variavel.tamanho)].strip()
            if valor:
                valor = int(valor)
            valor_final = variavel.categoria.get(valor) if variavel.categoria.get(valor) else valor
            nova_linha.append(valor_final)
        linhas.append(nova_linha)

        # limitando em n linhas o arquivo gerado
        if idx > 1000: # n
            break

df = pd.DataFrame(linhas, columns=colunas)
print(f'df shape: {df.shape}') # (356904 rows, 434 columns)
df.to_csv('microdados.csv', sep=';', encoding='utf-8-sig')