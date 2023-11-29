import streamlit as st
import pandas as pd

all_column = ['Ссылка','Ответственный','Проектировщик','Количество','Номенклатура','ПроцентСкидкиНаценки',
    'Сумма','СуммаНДС','Цена','ХарактеристикаНоменклатуры','ПроцентАвтоматическихСкидок','СуммаНаценки','КоличествоВЗапуске',
    'ДатаЗапускаВПроизводство','Подразделение','Группа',]


options = st.multiselect(
    'Параметры выгрузки', all_column , placeholder = "Выберите параметры выгрузки")

Data_frame = pd.read_excel('C:\\Users\\test\\Desktop\\test_app\\test_table.xlsx')


if not len(options): #Если срезов нет
    parameters = all_column
else:
    parameters = options


edit_frame = st.data_editor(
Data_frame,
use_container_width=True,
hide_index=True,
column_config={},
column_order=parameters
#Попробуем через session state
 )
