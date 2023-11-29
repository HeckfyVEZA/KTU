import streamlit as st
import pandas as pd

st.set_page_config(page_title="test_App",layout="wide") #Сначала выставляем стиль для страницы
st.sidebar.subheader('Filter') #Потом создаю боковую панель

#Здесь прописываем категории
Category_set = set() 
category_1 = st.sidebar.checkbox('checkbox1') #Прописываю флажки выбора категории (Возможно потом в виде списка)
category_2 = st.sidebar.checkbox('checkbox2')
category_3 = st.sidebar.checkbox('checkbox3')

Data_table = {'Column1':[1,2,3,4,5],'Column2':[1,2,3,4,5],'Column3':[1,2,3,4,5],'Column4':[1,2,3,4,5],'Column5':[1,2,3,4,5],'Column6':[1,2,3,4,5],'Column7':[1,2,3,4,5],'Column8':[1,2,3,4,5],} #Пустные столбцы

Data_frame = pd.DataFrame(Data_table)

col = st.columns([5,2,2,2,2])


col[0].title('Здесь может быть ваша реклама')
col[2].checkbox('filter1')
col[3].selectbox('filter2',('A','B', 'C', 'D','E'))
col[4].checkbox('filter3')


main_tab = st.tabs(['page1', 'page2', 'page3','page4'])


edit_frame = st.data_editor(
    Data_frame,
    use_container_width=True,
    hide_index=True,
    column_config={
    'Column1': st.column_config.SelectboxColumn(
    width="small",
    options=['0', '1'],
    required=True,
    ),
    "Column2": st.column_config.SelectboxColumn(
    width="small",
    options=['1', '2', '3','4','4М','5','5М','6','6М'],
    required=True,
    ),
    "Column3": st.column_config.SelectboxColumn(
    width="small",
    options=['С', 'Ш'],
    required=True,
    ),
    "Column5": st.column_config.SelectboxColumn(
    width="small",
    options=['П', 'Л'],
    required=True,
    )},
    disabled=["Column4","Column6","Column7","Column8"],
    #Попробуем через session state
     )