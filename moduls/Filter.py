import streamlit as st
import pandas as pd


st.set_page_config(page_title="test_App",layout="wide") #Сначала выставляем стиль для страницы
st.sidebar.subheader('Filter') #Потом создаю боковую панель

if 'Check' not in st.session_state:
    st.session_state.Check = 0
st.write(st.session_state.Check)


all_column = ['Ссылка','Ответственный','Проектировщик','Количество','Номенклатура','ПроцентСкидкиНаценки',
    'Сумма','СуммаНДС','Цена','ХарактеристикаНоменклатуры','ПроцентАвтоматическихСкидок','СуммаНаценки','КоличествоВЗапуске',
    'ДатаЗапускаВПроизводство','Подразделение','Группа',]

Data_frame = pd.read_excel('C:\\Users\\test\\Desktop\\test_app\\test_table.xlsx')

List_unic_link = list(Data_frame['Ссылка'].drop_duplicates()) #Список из уникальных ссылок
List_unic_otvet= list(Data_frame['Ответственный'].drop_duplicates()) #Список из уникальных ссылок
List_unic_project = list(Data_frame['Проектировщик'].drop_duplicates()) #Список из уникальных ссылок



check_col = [False]*len(List_unic_link)
Link_df = pd.DataFrame({'Ссылка':List_unic_link,'check':check_col})
check_col = [False]*len(List_unic_otvet)
otvet_df = pd.DataFrame({'Ответственный':List_unic_otvet,'check':check_col})
check_col = [False]*len(List_unic_project)
project_df = pd.DataFrame({'Проектировщик':List_unic_project,'check':check_col})


#df = Data_frame.loc[Data_frame['Ссылка'] == '00000654212'] - Пример вывода фрейма по условию

col = st.columns([5,5])

########### Если флажок уже стоит

all_dis = ['Ссылка','Ответственный','Проектировщик']
if st.session_state.Check:
    all_dis = ['Ссылка','Ответственный','Проектировщик','check']


with st.sidebar.expander("Cсылка"):
    edit_df_link = st.data_editor(
    Link_df,
    column_config={
        "Сгруппировать": st.column_config.CheckboxColumn(
            "Your favorite?",
            help="Select your **favorite** widgets",
            default=False,
        )
    },
    disabled=all_dis,
    hide_index=True,
)

with st.sidebar.expander("Ответственный"):
    edit_df_otvet = st.data_editor(
    otvet_df,
    column_config={
        "Сгруппировать": st.column_config.CheckboxColumn(
            "Your favorite?",
            help="Select your **favorite** widgets",
            default=False,
        )
    },
    disabled=all_dis,
    hide_index=True,
)

with st.sidebar.expander("Проектировщик"):
    edit_df_project = st.data_editor(
    project_df,
    column_config={
        "Сгруппировать": st.column_config.CheckboxColumn(
            "Your favorite?",
            help="Select your **favorite** widgets",
            default=False,
        )
    },
    disabled=all_dis,
    hide_index=True,
)


########### Если флажок уже стоит
#edit_df_link
#edit_df_otvet
#edit_df_project

st.write(edit_df_link['check'])
st.write(edit_df_otvet['check'])
st.write(edit_df_project['check'])

#if True in set(edit_df_link['check']) or True in set(edit_df_otvet['check']) or True in set(edit_df_project['check']):
#    st.session_state.Check += 1
#else:
#    st.session_state.Check -= 1

df = Data_frame.loc[Data_frame['Ссылка'] == '00000654212'] #- Пример вывода фрейма по условию

st.dataframe(df)
