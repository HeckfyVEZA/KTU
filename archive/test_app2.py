import streamlit as st
import pandas as pd


st.set_page_config(page_title="test_App",layout="wide") #Сначала выставляем стиль для страницы
st.sidebar.subheader('Filter') #Потом создаю боковую панель

#Здесь прописываем категории
Category_set = set() 
category_1 = st.sidebar.checkbox('checkbox1') #Прописываю флажки выбора категории (Возможно потом в виде списка)
category_2 = st.sidebar.checkbox('checkbox2')
category_3 = st.sidebar.checkbox('checkbox3')


col = st.columns([5,5])

all_column = ['Ссылка','Ответственный','Проектировщик','Количество','Номенклатура','ПроцентСкидкиНаценки',
    'Сумма','СуммаНДС','Цена','ХарактеристикаНоменклатуры','ПроцентАвтоматическихСкидок','СуммаНаценки','КоличествоВЗапуске',
    'ДатаЗапускаВПроизводство','Подразделение','Группа',]

col[0].title('Здесь могла бы быть ваша реклама')
options = col[1].multiselect('Параметры выгрузки', all_column , placeholder = "Выберите параметры выгрузки")


main_tab = st.tabs(['page1', 'page2', 'page3','page4'])


Data_frame = pd.read_excel('C:\\Users\\kushhov\\Desktop\\test_app\\test_table.xlsx')

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


