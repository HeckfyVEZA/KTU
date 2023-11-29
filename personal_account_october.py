import streamlit as st
import pandas as pd
import pickle
from pathlib import Path
import Valid_modul as stauth

st.set_page_config(page_title="test_App",layout="wide") #Сначала выставляем стиль для страницы

#Этап валидации 
names = ['Азаров Владислав Евгеньевич',
              'Варданян Тигран Арамович',
              'Лоскутов Глеб Алексеевич',
              'Петров Михаил Александрович',
              'Бахтеев Павел Юрьевич',
              'Кохно Георгий Андреевич',
              'Фролов Антон Сергеевич',
              'Калантаров Андрей Викторович',
              'Гаврилов Константин Валерьевич',
              'Гулина Наталья Александровна',
              'Денисов Денис Владимирович',
              'Грибач Павел Александрович',
              'Здейкович Стефан',
              'Мельников Ефим Владимирович',
              'Влазнев Константин Александрович',
              'Моклюк Максим Олегович',
              'Пращук Андрей Юрьевич',
              'Кондратьев Александр Иванович',
              'Муханчиков Иван Михайлович',
              'Гулин Сергей Михайлович',
              'Дутов Александр Васильевич',
              'Життеев Тимур Юрьевич',
              'Бычков Максим Юрьевич',
              'Каспир Евгений Владимирович',
              'Мякиньков Виктор Сергеевич',
              'Тагиров Максим Адимович', 
              'Данилов Павел Валерьевич',
              'Мумладзе Александр Мевлудиевич',
              'Омельченко Юрий Анатольевич',
              'Туманов Виталий Юрьевич', 
              'Королев Михаил Вячеславович',
              'Життеев Юрий Бузжигитович',
              'Горбунов Максим Максимович',
              'Цуканов Роман Евгеньевич']
usernames = ['Азаров Владислав Евгеньевич',
              'Варданян Тигран Арамович',
              'Лоскутов Глеб Алексеевич',
              'Петров Михаил Александрович',
              'Бахтеев Павел Юрьевич',
              'Кохно Георгий Андреевич',
              'Фролов Антон Сергеевич',
              'Калантаров Андрей Викторович',
              'Гаврилов Константин Валерьевич',
              'Гулина Наталья Александровна',
              'Денисов Денис Владимирович',
              'Грибач Павел Александрович',
              'Здейкович Стефан',
              'Мельников Ефим Владимирович',
              'Влазнев Константин Александрович',
              'Моклюк Максим Олегович',
              'Пращук Андрей Юрьевич',
              'Кондратьев Александр Иванович',
              'Муханчиков Иван Михайлович',
              'Гулин Сергей Михайлович',
              'Дутов Александр Васильевич',
              'Життеев Тимур Юрьевич',
              'Бычков Максим Юрьевич',
              'Каспир Евгений Владимирович',
              'Мякиньков Виктор Сергеевич',
              'Тагиров Максим Адимович', 
              'Данилов Павел Валерьевич',
              'Мумладзе Александр Мевлудиевич',
              'Омельченко Юрий Анатольевич',
              'Туманов Виталий Юрьевич', 
              'Королев Михаил Вячеславович',
              'Життеев Юрий Бузжигитович',
              'Горбунов Максим Максимович',
              'Цуканов Роман Евгеньевич']

file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(names, usernames, hashed_passwords, "sales_dashboard","abcdef", cookie_expiry_days = 1)

name, authentication_status, username = authenticator.login("Вход","main")



if authentication_status == False:
    st.error("Неверный логин или пароль")

if authentication_status == None:
    st.warning("Пожалуйста, введите ваш логин и пароль")

#Блок работы после прохождения валидации
if authentication_status: 
    authenticator.logout("Выйти из ЛК","sidebar")
    col = st.columns([10,5])

    all_column=['Участник','Проектный институт','КТУ','Бонус менеджера','Тип участия']

    col[0].title(name)
    #options = col[1].multiselect('Параметры выгрузки', all_column , placeholder = "Выберите параметры выгрузки")

    if 'key' not in st.session_state:
        st.session_state['key'] = 0

    origin_key = st.session_state['key']
    
    Data_frame = pd.read_excel('C:\\Users\\kushhov\\Desktop\\personal_account\\tables\\october3.xlsx') #Оригинальная выгрузка
    Data_frame  =  Data_frame.fillna(0)                    


    parameters = all_column


    main_tab = st.tabs(['Продажа', 'Проектирование'])

    with main_tab[0]:
        #_____________________________________ Блок работы с новой таблицей
        #Контрагент
        auth_frame = pd.read_excel('C:\\Users\\kushhov\\Desktop\\personal_account\\tables\\october3.xlsx') #Первоначальная выгрузка
        auth_frame  =  auth_frame.fillna(0)    
        origin_frame = auth_frame.loc[auth_frame['Продавец'] == name]

        col = st.columns(7)

        col[0].subheader('Номер счёта')
        col[1].subheader('Клиент')
        col[2].subheader('Сумма заказа')
        col[3].subheader('Средняя скидка')
        col[4].subheader('КТУ')
        col[5].subheader('Бонус')
        col[6].subheader('Тип участия')
        st.header('',divider='rainbow')
        #Платов Дмитрий Андреевич

        for i in range(len(origin_frame)):
                origin_key +=1
                col = st.columns(7)
                col[0].write(f"0000{str(origin_frame['Номер счёта'].values[i])}")
                #col[0].write(origin_frame['Номер'].values[i])
                col[1].write(origin_frame['Клиент'].values[i])
                col[2].write(origin_frame['Сумма заказа'].values[i])
                col[3].write(origin_frame['Средняя скидка'].values[i])
                col[4].text_input('КТУ',key=origin_key+261)
                col[5].write(origin_frame['Бонус менеджера'].values[i])
                col[6].selectbox("Тип участия",[ "Продажа", "Проектирование", "Заказчик", "Другое..."],key=origin_key+51)

                with st.container():
                    with st.expander('Развернуть'):
                        temp_df = Data_frame.loc[(Data_frame['Номер счёта'] == origin_frame['Номер счёта'].values[i]) & (Data_frame['Участник'] != Data_frame['Продавец'] )]
                        temp_df["Тип участия"] = "Проектирование"
                        Big_frame = st.data_editor(
                        temp_df,
                        use_container_width=True,
                        hide_index=True,
                        column_config={
                            "Тип участия": st.column_config.SelectboxColumn(
                            "Тип участия",
                            width="medium",
                            options=[
                                "Продажа",
                                "Проектирование",
                                "Заказчик",
                                "Другое..."
                            ],
                            required=False,
                            default="Проектирование"
                            )
                        },
                        column_order=parameters,
                        key=origin_key+3,
                        num_rows="dynamic"

                        ) #Теперь настрою параметры фрейма

    with main_tab[1]:
        #Проектный институт
        auth_frame = pd.read_excel('C:\\Users\\kushhov\\Desktop\\personal_account\\tables\\october3.xlsx') #Первоначальная выгрузка
        auth_frame  =  auth_frame.fillna(0)   
        origin_frame = auth_frame.loc[auth_frame['Участник'] == name]
        parameters = ['Участник', 'Проектный институт','КТУ','Тип участия']
        col = st.columns(8)

        col[0].subheader('Номер счёта')
        col[1].subheader('Продавец')
        col[2].subheader('Клиент')
        col[3].subheader('Сумма заказа')
        col[4].subheader('Средняя скидка')
        col[5].subheader('КТУ')
        col[6].subheader('Бонус')
        col[7].subheader('Тип участия')

        st.header('',divider='rainbow')
        #Платов Дмитрий Андреевич

        for i in range(len(origin_frame)):
            if (origin_frame['Продавец'].values[i] != origin_frame['Участник'].values[i]):
                origin_key +=1
                col = st.columns(8)
                col[0].write(f"0000{str(origin_frame['Номер счёта'].values[i])}")
                col[1].write(origin_frame['Продавец'].values[i])
                col[2].write(origin_frame['Клиент'].values[i])
                col[3].write(origin_frame['Сумма заказа'].values[i])
                col[4].write(origin_frame['Средняя скидка'].values[i])
                col[5].write('out')
                col[6].write(origin_frame['Бонус менеджера'].values[i])
                col[7].write("Продажа")


                with st.container():
                    with st.expander('Развернуть'):
                        temp_df = Data_frame.loc[(Data_frame['Номер счёта'] == origin_frame['Номер счёта'].values[i]) & (Data_frame['Участник'] != Data_frame['Продавец'] )]
                        temp_df["Тип участия"] = "Продажа"
                        Big_frame = st.dataframe(
                        temp_df,
                        use_container_width=True,
                        hide_index=True,
                        column_config={},
                        column_order=parameters,
                        ) #Теперь настрою параметры фрейма