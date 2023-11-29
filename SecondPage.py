import streamlit as st
from PIL import Image
import pandas as pd
import webbrowser
import PySimpleGUI as sg
import os

st.set_page_config(layout="wide") #Сначала выставляем стиль для страницы


col = st.columns(4) # Создадим четыре (пусть будет 4) столбца
Data_frame = pd.read_excel('C:\\Users\kushhov\\Desktop\\Streamlit_lesson\\BD.xlsx') #Обращаемся к таблице (наша база данных:))
ch = -1 # Заводим счётчик, который должен быть не больше 4 (Начинаем  -1, чтобы потом было -1 + 1 = 0) 
#Блок получения ссылки исходя из нужного номера (а также выбор, что будем видеть: категорию или имя)
Long = len(list(Data_frame['root'])) #Получаем длину наших столбцов

# Блок вывода картинок 
for i in range(Long): 
        root = Data_frame['root'].values[i] # Передаём путь к картинке (Слеши сами преобразуются в нужный вид)
        original = Image.open(root+'.jpg') # Открываем изображение (Теперь проблема с высотой)
        ch +=1
        if ch == 4: # Сбрасываем счётчик
            ch = 0
        name = Data_frame['Name'].values[i] #Передаю имя ячейки
        col[ch].image(original,caption=name, use_column_width=True)
 
#os.system('streamlit run c:\\Users\\kushhov\\Desktop\\Streamlit_lesson\\MyGallery3.py')
