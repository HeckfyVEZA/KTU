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
    col = st.columns([5,5])

    all_column=['Менеджер проекта','Заказ покупателя.Проектный институт','КТУ','Бонус менеджера','Тип участия']

    col[0].title(name)
    options = col[1].multiselect('Параметры выгрузки', all_column , placeholder = "Выберите параметры выгрузки")

    if 'key' not in st.session_state:
        st.session_state['key'] = 0

    origin_key = st.session_state['key']
    
    Data_frame = pd.read_excel('C:\\Users\\kushhov\\Desktop\\personal_account\\tables\\october3.xlsx') #Оригинальная выгрузка
                                    

    if not len(options): #Если срезов нет
        parameters = all_column
    else:
        parameters = options

    main_tab = st.tabs(['Продавец (ответсвенный)', 'Менеджер проекта'])

    with main_tab[0]:
        #_____________________________________ Блок работы с новой таблицей
        #Контрагент
        auth_frame = pd.read_excel('C:\\Users\\kushhov\\Desktop\\personal_account\\tables\\october3.xlsx') #Первоначальная выгрузка
        origin_frame = auth_frame.loc[auth_frame['Заказ покупателя.Ответственный'] == name]

        col = st.columns(7)

        col[0].write('Номер счёта')
        col[1].write('Клиент')
        col[2].write('Сумма заказа')
        col[3].write('Средняя скидки')
        col[4].write('КТУ')
        col[5].write('Бонус')
        col[6].write('Тип участия')
        st.header('',divider='rainbow')
        #Платов Дмитрий Андреевич

        for i in range(len(origin_frame)):
            if (origin_frame['Заказ покупателя.Ответственный'].values[i] != origin_frame['Менеджер проекта'].values[i]):
                origin_key +=1
                col = st.columns(7)
                col[0].write(f"0000{str(origin_frame['Номер'].values[i])[:-2]}")
                col[1].write(origin_frame['Контрагент'].values[i])
                col[2].write(origin_frame['Сумма заказа'].values[i])
                col[3].write(origin_frame['Средний % скидки'].values[i])
                col[4].write(origin_frame['КТУ'].values[i])
                col[5].write(origin_frame['Бонус менеджера'].values[i])
                col[6].selectbox("Тип участия",[ "Продажа", "Проектирование", "Заказчик", "Другое..."],key=origin_key+51)

                with st.container():
                    with st.expander('Развернуть'):
                        temp_df = Data_frame.loc[(Data_frame['Номер'] == origin_frame['Номер'].values[i]) & (Data_frame['Менеджер проекта'] != Data_frame['Заказ покупателя.Ответственный'] )]
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
                            required=True,
                            )
                        },
                        column_order=parameters,
                        key=origin_key+3,
                        num_rows="dynamic"
                        ) #Теперь настрою параметры фрейма

    with main_tab[1]:
        #Проектный институт
        auth_frame = pd.read_excel('C:\\Users\\kushhov\\Desktop\\personal_account\\tables\\october.xlsx') #Первоначальная выгрузка
        origin_frame = auth_frame.loc[auth_frame['Менеджер проекта'] == name]

        col = st.columns(5)

        col[0].write('Номер')
        col[1].write('Заказ покупателя.Ответственный')
        col[2].write('Сумма заказа')
        col[3].write('Средний % скидки')
        col[4].write('Сумма заказа без скидки')

        st.header('',divider='rainbow')
        #Платов Дмитрий Андреевич

        for i in range(len(origin_frame)):
            if (origin_frame['Заказ покупателя.Ответственный'].values[i] != origin_frame['Менеджер проекта'].values[i]):
                origin_key +=1
                col = st.columns(5)
                col[0].write(f"0000{str(origin_frame['Номер'].values[i])[:-2]}")
                col[1].write(origin_frame['Заказ покупателя.Ответственный'].values[i])
                col[2].write(origin_frame['Сумма заказа'].values[i])
                col[3].write(origin_frame['Средний % скидки'].values[i])
                col[4].write(origin_frame['Сумма заказа без скидки'].values[i])

                with st.container():
                    with st.expander('Развернуть'):
                        temp_df = Data_frame.loc[(Data_frame['Номер'] == origin_frame['Номер'].values[i]) & (Data_frame['Менеджер проекта'] != Data_frame['Заказ покупателя.Ответственный'] )]
                        Big_frame = st.data_editor(
                        temp_df,
                        use_container_width=True,
                        hide_index=True,
                        column_config={},
                        column_order=parameters,
                        key=origin_key+3,
                        num_rows="dynamic"
                        ) #Теперь настрою параметры фрейма