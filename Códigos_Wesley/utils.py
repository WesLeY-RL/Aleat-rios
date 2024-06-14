from utils import webscraping, clean_data, plot

# Instrução: 
# A partir da tabela em https://pt.wikipedia.org/wiki/Lista_de_filmes_de_maior_bilheteria,
# criar um gráfico dos TOP 10 diretores e TOP 10 Distribuidoras com maior bilheteria.

# coleta de dados
df = webscraping()
print(df)

# tratamento
df = clean_data(df)
print(df)

# visualização
plot(df)