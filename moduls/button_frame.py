import streamlit as st
import pandas as pd

all_column = ['Ссылка','Ответственный','Проектировщик','Количество','Номенклатура','ПроцентСкидкиНаценки',
    'Сумма','СуммаНДС','Цена','ХарактеристикаНоменклатуры','ПроцентАвтоматическихСкидок','СуммаНаценки','КоличествоВЗапуске',
    'ДатаЗапускаВПроизводство','Подразделение','Группа',]

Data_frame = pd.read_excel('C:\\Users\\test\\Desktop\\test_app\\test_table.xlsx')

List_unic_link = list(Data_frame['Ссылка'].drop_duplicates()) #Список из уникальных ссылок

List_unic_otvet= list(Data_frame['Ответственный'].drop_duplicates()) #Список из уникальных ссылок

List_unic_project = list(Data_frame['Проектировщик'].drop_duplicates()) #Список из уникальных ссылок





#df = Data_frame.loc[Data_frame['Ссылка'] == '00000654212'] - Пример вывода фрейма по условию

col = st.columns([5,5])


column_filter = ['Ссылка','Ответственный','Проектировщик']
options_filter = col[0].selectbox('Параметры группировки выгрузки', column_filter)

match options_filter:
    case 'Ссылка': 
        #radio_list = [len[List_unic_link]*]
        table_unic_x = {'Ссылка:':List_unic_link,'Перейти:':[]}
    case 'Ответственный': 
        radio_list = []
        table_unic_x = {'Ссылка:':List_unic_link,'Перейти:':[]}
    case 'Проектировщик': 
        radio_list = []
        table_unic_x = {'Ссылка:':List_unic_link,'Перейти:':[]}







df_unic_link = pd.DataFrame()
