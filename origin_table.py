import pandas as pd
from pandas.io.excel import ExcelWriter

Data_frame = pd.read_excel('C:\\Users\\kushhov\\Desktop\\test_app\\test_table.xlsx') #Оригинальная выгрузка

unic_df = Data_frame.drop_duplicates(subset='Ссылка') #Получаем фрейм из дубликатов (но без суммы) 

#sum_plan = datPerson['План, ч.'].sum()
#sum_fact = datPerson['Факт, ч.'].sum()
#datPerson = dataframe_ishod.loc[dataframe_ishod['Исполнитель'] == Person[i]]

#Ссылка
#Ответственный
#Сумма 
#СуммаНДС
#Подразделение
#Группа

df_list = [None,None,[],[],None,None]

df_list[0] = list(unic_df['Ссылка'])
df_list[1] = list(unic_df['Ответственный'])
df_list[4] = list(unic_df['Подразделение'])
df_list[5] = list(unic_df['Группа'])


Link = list(unic_df['Ссылка'])


Table = []
for i in range(len(Link)):
    datLink= Data_frame.loc[Data_frame['Ссылка'] == Link[i]]
    sum_all = datLink['Сумма'].sum()
    sum_nds = datLink['СуммаНДС'].sum()
    df_list[2].append(sum_all)
    df_list[3].append(sum_nds)


df_dict = {'Ссылка':df_list[0],'Ответственный':df_list[1],'Сумма':df_list[2],'СуммаНДС':df_list[3],'Подразделение':df_list[4],'Группа':df_list[5]}

new_dataframe = pd.DataFrame(df_dict)     
with ExcelWriter('C:\\Users\\kushhov\\Desktop\\test_app\\origin_table.xlsx') as writer:
    new_dataframe.to_excel(writer,index=False)
