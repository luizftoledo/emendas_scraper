#!/usr/bin/env python
# coding: utf-8

# In[70]:


import glob
import os
import pandas as pd
import time
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options



# In[71]:

# Pasta de downloads
DATA_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data')
DOWNLOAD_DIR = Path.home() / 'Downloads'

# Configure Chrome options
options = webdriver.ChromeOptions()
options.add_argument('--headless=new')
options.add_argument('--remote-debugging-port=9222')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)


# In[72]:


driver.get("https://www9.senado.gov.br/QvAJAXZfc/opendoc.htm?document=senado%2Fsigabrasilpainelcidadao.qvw&host=QVS%40www9&anonymous=true&Sheet=SH14")

#driver eh a nossa webpage
print('ABRI O LINK')


# In[73]:


# o site demora muito pra carregar, então vamos aguardar tudo
time.sleep(25)
print('ESPEREI 25 SEG')


# In[75]:



# fechar o balaozinho

element = driver.find_element(by=By.XPATH, value='/html/body/div[17]/div/div/div[7]/div[2]/table/tbody/tr/td')
element.click()
print('FECHEI O BALAO')


# In[76]:


time.sleep(5)
print('ESPEREI MAIS 5')


# In[77]:


# clicar em gráficos customizados
element = driver.find_element(by=By.XPATH, value='/html/body/div[17]/div/div/div[694]/div[2]/table/tbody/tr/td')
element.click()
print('CLIQUEI EM GRAFICO CUSTOMIZADO')


# In[78]:


time.sleep(15)
print('ESPEREI MAIS 15')


# In[79]:


# clicar em 2023
element = driver.find_element(by=By.XPATH, value='/html/body/div[17]/div/div/div[55]/div[2]/div/div[1]/div[6]/div[1]')
element.click()
print('ESCOLHI 2023')


# In[80]:


time.sleep(15)
print('ESPEREI MAIS 15')


# In[81]:


# clicar em AUTOR DA EMENDA
element = driver.find_element(by=By.XPATH, value='/html/body/div[17]/div/div/div[31]/div[2]/div/div[1]/div[4]/div[3]')
element.click()
print('ESCOLHI AUTOR DA EMENDA')


# In[82]:


time.sleep(15)
print('ESPEREI MAIS 15')


# In[83]:



# CLICAR EM EMPENHADO

element = driver.find_element(by=By.XPATH, value='/html/body/div[17]/div/div/div[31]/div[2]/div/div[1]/div[20]/div[3]')
element.click()

print('ESCOLHI EMPENHADO')
time.sleep(10)
print('ESPEREI 10')

# AUTORIZADO
element = driver.find_element(by=By.XPATH, value='/html/body/div[17]/div/div/div[31]/div[2]/div/div[1]/div[19]/div[3]')
element.click()

print('ESCOLHI AUTORIZADO')
time.sleep(10)
print('ESPEREI MAIS 10')


# clicar em pago

element = driver.find_element(by=By.XPATH, value='/html/body/div[17]/div/div/div[31]/div[2]/div/div[1]/div[24]/div[3]')
element.click()
print('ESCOLHI PAGO')

time.sleep(10)
print('ESPEREI MAIS 10')

# clicar em pago rp

element = driver.find_element(by=By.XPATH, value='/html/body/div[17]/div/div/div[31]/div[2]/div/div[1]/div[25]/div[3]')
element.click()
print('ESCOLHI PAGO RP')

time.sleep(10)
print('ESPEREI MAIS 10')



# In[84]:


time.sleep(5)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# clicar com o botao direito em cima da planilha

# Localizar o elemento e clicar com o botão direito
element = driver.find_element(By.XPATH, '/html/body/div[17]/div/div/div[52]/div[2]/div[1]/div[1]/div[2]/div/div[9]/div[1]')
actions = ActionChains(driver)
actions.context_click(element).perform()
print('CLIQUEI COM O BOTAO DIREITO NA TABELA')


# In[85]:


time.sleep(10)
print('ESPEREI MAIS 10')
# Localizar o item do menu e clicar nele
item_menu = driver.find_element(By.XPATH, '/html/body/ul[3]/li[6]/a/span')
item_menu.click()
print('BAIXEI A PLANILHA')


# In[86]:


time.sleep(10)
print('ESPEREI MAIS 10')


# In[92]:


import pandas as pd
import glob
from datetime import datetime, timedelta


# Data e hora de criação desejada (uma hora atrás)
data_hora_desejada = datetime.now() - timedelta(hours=1)


# Procurar arquivo XLSX na pasta de downloads
arquivos_xlsx = glob.glob(os.path.join(DOWNLOAD_DIR, '*.xlsx'))

# Verificar se há pelo menos um arquivo XLSX encontrado
if arquivos_xlsx:
    arquivo_desejado = None
    data_hora_recente = None
    for arquivo in arquivos_xlsx:
        # Obter o tempo de criação do arquivo
        data_criacao = os.path.getctime(arquivo)
        # Converter o tempo de criação em uma estrutura de data e hora
        data_criacao = datetime.fromtimestamp(data_criacao)
        # Verificar se a data de criação é maior que a data desejada
        if data_criacao > data_hora_desejada:
            # Verificar se é o arquivo mais recente dentro do intervalo desejado
            if data_hora_recente is None or data_criacao > data_hora_recente:
                arquivo_desejado = arquivo
                data_hora_recente = data_criacao

    if arquivo_desejado:
        # Ler o arquivo XLSX desejado com o pandas
        df = pd.read_excel(arquivo_desejado)
        print(f'baixei o {arquivo_desejado}')

        # Exemplo de uso do DataFrame
        print(df.columns)  # Imprime as primeiras linhas do DataFrame
    else:
        print('Nenhum arquivo XLSX encontrado baixado na última hora.')
else:
    print('Nenhum arquivo XLSX encontrado na pasta de downloads.')


# In[93]:


# Data de hoje
from datetime import date
data_atual = date.today()
nome_arquivo = os.path.join(
    DATA_DIR,
    f'dados_{data_atual.strftime("%Y-%m-%d")}.csv'
)
df.to_csv(nome_arquivo, index=False)
print('SALVEI O CSV')


# In[94]:


df_geral = pd.read_csv(nome_arquivo)


df_geral.columns = df_geral.columns.str.lower().str.replace(' ', '_').str.replace('(', '_').str.replace(')', '').str.replace('__', '_')
df_geral = df_geral[['autor', 'autor_tipo', 'partido', 'autor_uf', 'autorizado_r$', 'empenhado_r$', 'pago_r$', 'rp_pago_r$']]
df_geral.to_csv(nome_arquivo, index=False)
df_geral.head(3)


# In[95]:


df_geral.head(3)


# In[97]:


df_soma = pd.DataFrame({
    'autorizado_r$': [df_geral['autorizado_r$'].sum()],
    'empenhado_r$': [df_geral['empenhado_r$'].sum()],
    'pago_r$': [df_geral['pago_r$'].sum()],
    'rp_pago_r$': [df_geral['rp_pago_r$'].sum()]
})

# Exibir o DataFrame com a porcentagem total de cada partido
tabela_final = df_soma
tabela_final_path = os.path.join(
    DATA_DIR,
    f'tabela_final_{data_atual.strftime("%Y-%m-%d")}.csv'
)

tabela_final.to_csv(tabela_final_path)

tabela_final


# In[ ]:





# In[ ]:




