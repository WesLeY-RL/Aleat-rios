import matplotlib.pyplot as plt
from matplotlib import rc
from pandas import read_html, DataFrame
from selenium.webdriver import Chrome
def webscraping() -> DataFrame:
    driver = Chrome()
    driver.get('https://pt.wikipedia.org/wiki/Lista_de_filmes_de_maior_bilheteria')
    return read_html(driver.page_source)[0]


def clean_data(df: DataFrame) -> DataFrame:
    df['Diretor(a)'] = df['Diretor(a)'].str.split(' / ')
    df = df.explode('Diretor(a)')

    df['Bilheteria (US$)'] = df['Bilheteria (US$)'].str.replace(' ', '')
    df['Bilheteria (US$)'] = df['Bilheteria (US$)'].astype('int64')
    
    df = df.groupby('Diretor(a)')['Bilheteria (US$)'].sum()
    df = df.sort_values(ascending=False)
    return df[:10]


def plot(df: DataFrame):
    rc('font', size=16)

    fig, ax = plt.subplots()
    ax: plt.Axes

    ax.set_title('Top 10 Diretores')
    ax.set_xlabel('Diretor(a)')
    ax.set_ylabel('Bilheteria Total')

    bars = ax.bar(df.index, df)
    ax.bar_label(bars, fmt='${:,.0f}', size=12)
    
    ax.grid(axis='y')
    ax.tick_params('x', labelrotation=45)
    ax.yaxis.set_major_formatter('${x:,.0f}')

    plt.subplots_adjust(0.12, 0.2, 0.98, 0.95)
    plt.get_current_fig_manager().window.state('zoomed')
    plt.show()
    
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