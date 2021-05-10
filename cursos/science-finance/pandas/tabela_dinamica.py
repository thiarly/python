import pandas as pd
#from google.colab.data_table import DataTable



URL = 'https://raw.githubusercontent.com/codigoquant/data/main/indicadores_fundamentalistas.csv'

#empresas = pd.read_csv(URL, index_col=0)

#DataTable(empresas)

#print (go(empresas))

#print (empresas)

# Filtrar empresas com liquidez média diaria maior do que R$ 1 bi
# DataTable(empresas, max_columns=25)

# Ordenar empresas por menores P/L
#DataTable(empresas, max_columns=25)

# Ordenar empresas por maiores Dividend Yield
#DataTable(empresas, max_columns=25)

# Listar as 5 empresas com maior ROIC
#DataTable(empresas, max_columns=25, num_rows_per_page=5)

# Listar as 5 empresas com menor EV/EBIT, excluindo EV/EBIT negativo.
#DataTable(empresas, max_columns=25, num_rows_per_page=5)

# Papel e P/L das 10 empresas com menor P/L não negativo, e com liq.2meses entre 1mi e 10mi
#DataTable(empresas, max_columns=25, num_rows_per_page=10)