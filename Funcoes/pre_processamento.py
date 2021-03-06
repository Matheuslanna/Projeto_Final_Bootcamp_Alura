# -*- coding: utf-8 -*-
"""pre_processamento.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pIAmElMKuzHOV9YnGVRT7CCD-99bMydI

Importação das bibliotecas utilizadas
"""

from numpy import any as numpy_any

"""Criação da funções para o pré-processamento de dados"""

def bfill_ffill_table(rows):
    '''
    Função utilizada para preencher os valores nulos com dados passados ou
    futuros utlizando os comandos "bfill" e "ffill", partindo do princípio que 
    os dados do paciente não variaram muito dentro da janela de 2 horas de 
    admissão.

    Parâmetros:
    -----------
    rows : linhas que correspondem a um mesmo paciente.
    
    Retorno:
    --------
    Retorna as linhas preenchidas pelo "bfill" e "ffill".
    '''
    rows[rows.select_dtypes('float64').columns] = rows[rows.select_dtypes('float64').columns].fillna(method='bfill').fillna(method='ffill')
    return rows

def select_window(rows, window='0-2', target_variable='ICU'):
    '''
    Função usada para selecionar as janelas de admissão e verificar se o
    foi admitido na UTI em algum momento. Caso tenha sido admitido na UTI, irá
    alterar o estado das janelas anteriores.
    
    Parâmetros:
    -----------
    rows : linhas que correspondem a um mesmo paciente.
    window : coluna correspondente à janela que será mantida
    target_variable : nome da variável dependente, padrão : 'ICU'
    
    Retono:
    -------
    Retorna o conjunto de dados preenchido
    '''
    if(numpy_any(rows[target_variable])):
        rows.loc[rows["WINDOW"]== window, target_variable] = 1
    return rows.loc[rows["WINDOW"] == window]