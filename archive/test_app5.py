import streamlit as st
import pandas as pd

st.set_page_config(page_title="test_App",layout="wide") #Сначала выставляем стиль для страницы

#Этап валидации
if 'valid_check' not in st.session_state:
    st.session_state['valid_check'] = False

if not st.session_state['valid_check']:
    
    Dict_valid = {'Азаров Владислав Евгеньевич': '1111',
              'Варданян Тигран Арамович': '1111',
              'Лоскутов Глеб Алексеевич': '1111',
              'Петров Михаил Александрович': '1111',
              'Бахтеев Павел Юрьевич': '1111',
              'Кохно Георгий Андреевич': '1111',
              'Фролов Антон Сергеевич': '1111',
              'Калантаров Андрей Викторович': '1111',
              'Гаврилов Константин Валерьевич': '1111',
              'Гулина Наталья Александровна': '1111',
              'Денисов Денис Владимирович': '1111',
              'Грибач Павел Александрович': '1111',
              'Здейкович Стефан': '1111',
              'Мельников Ефим Владимирович': '1111',
              'Влазнев Константин Александрович': '1111',
              'Моклюк Максим Олегович': '1111',
              'Пращук Андрей Юрьевич': '1111',
              'Кондратьев Александр Иванович': '1111',
              'Муханчиков Иван Михайлович': '1111',
              'Гулин Сергей Михайлович': '1111',
              'Дутов Александр Васильевич': '1111',
              'Життеев Тимур Юрьевич': '1111',
              'Бычков Максим Юрьевич': '1111',
              'Каспир Евгений Владимирович': '1111',
              'Мякиньков Виктор Сергеевич': '1111',
              'Тагиров Максим Адимович': '1111', 
              'Данилов Павел Валерьевич': '1111',
              'Мумладзе Александр Мевлудиевич': '1111',
              'Омельченко Юрий Анатольевич': '1111',
              'Туманов Виталий Юрьевич': '1111', 
              'Королев Михаил Вячеславович': '1111',
              'Життеев Юрий Бузжигитович': '1111',
              'Горбунов Максим Максимович': '1111',
              'Цуканов Роман Евгеньевич': '1111'}
    with st.form("validation_form"):
        def authentication(json_employees_login_password):
            login_auth = st.selectbox('ФИО сотрудника', json_employees_login_password.keys())
            password_auth = st.text_input('Пароль', type='password')
            return password_auth == json_employees_login_password[login_auth], password_auth

        valid_check,password = authentication(Dict_valid)
        if not valid_check and password != "":
            st.write('Неверный пароль')

        submitted = st.form_submit_button("Войти",type="primary")
        if submitted:
            st.session_state['valid_check'] = valid_check
            st.rerun()

#Блок работы после прохождения валидации
if  st.session_state['valid_check']:
    st.sidebar.subheader('Группировать по:') #Потом создаю боковую панель
    reset = st.sidebar.button('Сбросить фильтры',type="primary") #Кнопка сброса всех флажков
    col = st.columns([5,5])

    all_column = ['Ссылка','Ответственный','Проектировщик','Количество','Номенклатура','ПроцентСкидкиНаценки',
        'Сумма','СуммаНДС','Цена','ХарактеристикаНоменклатуры','ПроцентАвтоматическихСкидок','СуммаНаценки','КоличествоВЗапуске',
        'ДатаЗапускаВПроизводство','Подразделение','Группа',]

    col[0].title('Здесь могла бы быть ваша реклама')
    options = col[1].multiselect('Параметры выгрузки', all_column , placeholder = "Выберите параметры выгрузки")

    main_tab = st.tabs(['page1', 'page2', 'page3','page4'])

    ### Блок работы с таблицей и фильтрами

    if 'key' not in st.session_state:
        st.session_state['key'] = 0

    if reset:
        st.session_state['key'] +=1

    origin_key = st.session_state['key']
    Data_frame = pd.read_excel('C:\\Users\\kushhov\\Desktop\\test_app\\test_table.xlsx') #Оригинальная выгрузка

    List_unic_link = list(Data_frame['Ссылка'].drop_duplicates()) #Список из уникальных ссылок
    List_unic_otvet= list(Data_frame['Ответственный'].drop_duplicates()) #Список из уникальных ссылок
    List_unic_project = list(Data_frame['Проектировщик'].drop_duplicates()) #Список из уникальных ссылок

    check_col = [False]*len(List_unic_link)
    Link_df = pd.DataFrame({'Ссылка':List_unic_link,'check':check_col})
    check_col = [False]*len(List_unic_otvet)
    otvet_df = pd.DataFrame({'Ответственный':List_unic_otvet,'check':check_col})
    check_col = [False]*len(List_unic_project)
    project_df = pd.DataFrame({'Проектировщик':List_unic_project,'check':check_col})

    all_dis = ['Ссылка','Ответственный','Проектировщик']

    with st.sidebar.expander("Cсылка"):
        edit_df_link = st.data_editor(
        Link_df,
        column_config={
            "Сгруппировать": st.column_config.CheckboxColumn(
                "Your favorite?",
                help="Select your **favorite** widgets",
                default=None,
            )
    },
    disabled=all_dis,
    hide_index=True,
    key=origin_key
)

    with st.sidebar.expander("Ответственный"):
        edit_df_otvet = st.data_editor(
        otvet_df,
        column_config={
            "Сгруппировать": st.column_config.CheckboxColumn(
                "Your favorite?",
                help="Select your **favorite** widgets",
                default=None,
            )
    },
    disabled=all_dis,
    hide_index=True,
    key=origin_key + 1
)

    with st.sidebar.expander("Проектировщик"):
        edit_df_project = st.data_editor(
        project_df,
        column_config={
            "Сгруппировать": st.column_config.CheckboxColumn(
                "Your favorite?",
                help="Select your **favorite** widgets",
                default=None,
            )
    },
    disabled=all_dis,
    hide_index=True,
    key=origin_key + 2
)

    #Ищем поднятые флажки

    #Списки ссылок и имён
    list_link = []
    list_otvet = []
    list_project= []
    #Немного оптимизирую процесс (Здесь много тестов)
    nn = max(len(List_unic_link),len(List_unic_otvet),len(List_unic_project))

    for i in range(nn):
        try:
            if edit_df_link['check'].values[i]:
                list_link.append(edit_df_link['Ссылка'].values[i])
        except:
             pass
        try:
            if edit_df_otvet['check'].values[i]:
                list_otvet.append(edit_df_otvet['Ответственный'].values[i])
        except:
            pass
        try:
            if edit_df_project['check'].values[i]:
                list_project.append(edit_df_project['Проектировщик'].values[i])
        except:
            pass

    all_df = {}
    all_df = pd.DataFrame(all_df) #Создаём пустой начальный df

    for i in range(len(list_link)):
        temp_df = Data_frame.loc[Data_frame['Ссылка'] == list_link[i]]
        all_df = pd.concat([all_df,temp_df])

    for i in range(len(list_otvet)):
        temp_df = Data_frame.loc[Data_frame['Ответственный'] == list_otvet[i]]
        all_df = pd.concat([all_df,temp_df])

    for i in range(len(list_project)):
        temp_df = Data_frame.loc[Data_frame['Проектировщик'] == list_project[i]]
        all_df = pd.concat([all_df,temp_df])

    if not len(options): #Если срезов нет
        parameters = all_column
    else:
        parameters = options

    #Big_frame = st.data_editor(
    #    all_df,
    #    use_container_width=True,
    #    hide_index=True,
    #    column_config={},
    #    column_order=parameters
    #    )

    #_____________________________________ Блок работы с новой таблицей
    origin_frame = pd.read_excel('C:\\Users\\kushhov\\Desktop\\test_app\\origin_table.xlsx') #Первоначальная выгрузка

    col = st.columns(6)
    col[0].write('Ссылка')
    col[1].write('Ответственный')
    col[2].write('Сумма')
    col[3].write('СуммаНДС')
    col[4].write('Подразделение')
    col[5].write('Группа')

    st.header('',divider='rainbow')

    
    for i in range(len(origin_frame)):
        col = st.columns(6)
        col[0].write(origin_frame['Ссылка'].values[i])
        with st.container():
            with st.expander('Развернуть'):
                temp_df = Data_frame.loc[Data_frame['Ссылка'] == origin_frame['Ссылка'].values[i]]
                Big_frame = st.data_editor(
                temp_df,
                use_container_width=True,
                hide_index=True,
                column_config={},
                column_order=parameters
                ) #Теперь настрою параметры фрейма

        col[1].write(origin_frame['Ответственный'].values[i])
        col[2].write(origin_frame['Сумма'].values[i])
        col[3].write(origin_frame['СуммаНДС'].values[i])
        col[4].write(origin_frame['Подразделение'].values[i])
        col[5].write(origin_frame['Группа'].values[i])

