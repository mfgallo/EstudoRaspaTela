# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 13:20:36 2020

@author: MGallo
"""

import pandas as pd

from selenium import webdriver

import numpy as np
import time
chrome_ = webdriver.Chrome(r'C:\Users\MGallo\Desktop\GuildTibia\chromedriver.exe')

chrome_.get("https://www.tibia.com/news/?subtopic=latestnews")

chrome_.find_element_by_id("community_Label").click()

chrome_.find_element_by_id("ActiveSubmenuItemLabel_guilds").click()

chrome_.find_element_by_name("world").send_keys('Xandebra')

chrome_.find_element_by_name("Submit").click()

linhas_tabela = chrome_.find_element_by_class_name('TableContent').find_elements_by_tag_name('tr')


for linhas in linhas_tabela:
    if (linhas.text == 'Vingadores'):
        linha = linhas.find_elements_by_tag_name('td')

linha_exata = linha[3]



# caminho_ao_botao = linha_exata.find_element_by_name('GuildName')

linha_exata.find_element_by_class_name('BigButton').click()               
#botao = caminho_ao_botao.find_element_by_name('View')

# botao.click()


tabela = chrome_.find_element_by_class_name('TableContentContainer').find_element_by_class_name('TableContent')
table_html = tabela.get_attribute('outerHTML')

df = pd.read_html(str(table_html))

df_final = df[0]

df_final[0] = df_final[0].replace(np.nan, '-')

primeiro_campo = df_final[0]
segundo_campo = df_final[1]
terceiro_campo = df_final[2]
quarto_campo = df_final[3]
quinto_campo = df_final[4]
sexto_campo = df_final[5]

lista_campo = [primeiro_campo[0], segundo_campo[0], terceiro_campo[0]
                ,quarto_campo[0], quinto_campo[0], sexto_campo[0]]

df_final = df_final.rename(columns={0:lista_campo[0], 1:lista_campo[1], 2:lista_campo[2],
                                     3:lista_campo[3], 4:lista_campo[4], 5:lista_campo[5]})
df_final = df_final.drop(0)

df_final.to_excel("Integrantes_Vingadores.xlsx", encoding='utf-8', index=False)







