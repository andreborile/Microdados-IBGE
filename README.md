Projeto de estudo criado para extrair dados de um arquivo txt de microdados do IBGE relacionado a um dicionario do mesmo e criar arquivo CSV.

Extraindo valores de arquivo de microdados do IBGE referente a PNAD 2015.
link: https://www.ibge.gov.br/estatisticas/sociais/educacao/9127-pesquisa-nacional-por-amostra-de-domicilios.html?=&t=microdados

Arquivos usados:
- Dados: https://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_anual/microdados/2015/Dados_20170517.zip
- Dicionarios e input: https://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_anual/microdados/2015/Dicionarios_e_input_20170517.zip

Deve se abrir o arquivo "extracao" e rodá-lo para gerar um arquivo CSV com o resultado.
Na linha 21 do arquivo "extracao.py" pode-se alterar o número total de linhas geradas pelo arquivo final. Sendo que o arquivo sem limitacao gera um total de 356904 linhas.