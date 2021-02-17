import pandas as pd

pd.set_option('display.min_rows', 50)
pd.set_option('display.max_rows', 200)

url = 'http://bvmf.bmfbovespa.com.br/indices/ResumoCarteiraTeorica.aspx?Indice=IBOV&idioma=pt-br'
pd.read_html(url)

