import pandas as pd

URL = 'https://raw.githubusercontent.com/codigoquant/data/main/indicadores_fundamentalistas.csv'

print (URL)

# 1. Ler arquivo CSV com Pandas e definir a Coluna 0 como índice
empresas = pd.read_csv(URL, index_col=0) # index_col=0 remover a primeira coluna.


# 2. Exibir o conteúdo do arquivo
#print(empresas)


# 3. Filtrar empresas com liquidez média diária maior do que R$ 1 bi
print('\033[35mFiltrar empresas com liquidez média diária maior do que R$ 1 bi\033[m\033[m')
filtro = empresas ['Liq.2meses'] > 1000000000
print (empresas[filtro])
print()
print('-*-'*75)

# 4. Ordenar empresas por menores P/L
print('\033[35mOrdenar empresas por menores P/L\033[m')
print (empresas.sort_values('P/L'))
print()
print('-*-'*75)

# 5. Ordenar empresas por maiores Dividend Yield
print('\033[35mOrdenar empresas por maiores Dividend Yield\033[m')
print (empresas.sort_values('Div.Yield', ascending=False))
print()
print('-*-'*75)

# 6. Listar as 5 empresas com maior ROIC
print('\033[35mListar as 5 empresas com maior ROIC\033[m')
print(empresas.sort_values('ROIC', ascending=False)[:5])
print()
print('-*-'*75)

# 7. Listar as 5 empresas com menor EV/EBIT, excluindo EV/EBIT negativo
print('\033[35mListar as 5 empresas com menor EV/EBIT, excluindo EV/EBIT negativo\033[m')
print (empresas[empresas['EV/EBIT'] > 0].sort_values('EV/EBIT')[:5])
print()
print('-*-'*75)

# 8. Listar as 5 empresas com maior EV/EBIT, excluindo EV/EBIT negativo
print('\033[35mListar as 5 empresas com maior EV/EBIT, excluindo EV/EBIT negativo\033[m')
print (empresas[empresas['EV/EBIT'] > 0].sort_values('EV/EBIT', ascending=False)[:5])
print()
print('-*-'*75)

# 9. Colunas Papel e P/L das 10 empresas com menor P/L nao negativo, e com Liq. 2 meses entre R$ 1 mi e R$ 10 mi
print('\033[35mColunas Papel e P/L das 10 empresas com menor P/L nao negativo, e com Liq. 2 meses entre R$ 1 mi e R$ 10 mi\033[m')
df = empresas[(empresas['Liq.2meses'] > 1000000) & (empresas['Liq.2meses'] < 10000000) & (empresas['P/L'] > 0)].sort_values('P/L')[:10][['Papel','P/L']]
print(df)
