import pandas as pd

URL = 'https://raw.githubusercontent.com/codigoquant/data/main/indicadores_fundamentalistas.csv'

print (URL)

# 1. Ler arquivo CSV com Pandas e definir a Coluna 0 como índice
empresas = pd.read_csv(URL, index_col=0) # index_col=0 remover a primeira coluna.


# 2. Exibir o conteúdo do arquivo
#print(empresas)


# 3. Filtrar empresas com liquidez média diária maior do que R$ 1 bi
filtro = empresas ['Liq.2meses'] > 1000000000
#print (empresas[filtro])

# 4. Ordenar empresas por menores P/L
#print (empresas.sort_values('P/L'))

# 5. Ordenar empresas por maiores Dividend Yield
#print (empresas.sort_values('Div.Yield', ascending=False))

# 6. Listar as 5 empresas com maior ROIC
#print(empresas.sort_values('ROIC', ascending=False)[:5])

# 7. Listar as 5 empresas com menor EV/EBIT, excluindo EV/EBIT negativo
#print (empresas[empresas['EV/EBIT'] > 0].sort_values('EV/EBIT')[:5])

#print()
#print('-*-'*100)

# 8. Listar as 5 empresas com maior EV/EBIT, excluindo EV/EBIT negativo
#print (empresas[empresas['EV/EBIT'] > 0].sort_values('EV/EBIT', ascending=False)[:5])

# 9. Colunas Papel e P/L das 10 empresas com menor P/L nao negativo, e com Liq. 2 meses entre R$ 1 mi e R$ 10 mi

fil = (empresas['Liq.2meses'] > 1000000) &  (empresas['Liq.2meses'] < 10000000) & (empresas['P/L'] > 0)
#(empresas.sort_values('P/L',ascending=False))

#print (empresas['Liq.2meses'] > 1000000) &  (empresas['Liq.2meses'] < 10000000) & (empresas['P/L'] > 0)

#empresas.sort_values('P/L')[:10]
#empresas.sorte_values('P/L')[:10]
print (empresas[fil])


