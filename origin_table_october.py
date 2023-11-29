import pandas as pd
from pandas.io.excel import ExcelWriter

Data_frame = pd.read_excel('C:\\Users\\kushhov\\Desktop\\personal_account\\tables\\october2.xlsx') #Оригинальная выгрузка

unic_df = Data_frame.drop_duplicates(subset='Номер') #Получаем фрейм из дубликатов (но без суммы) 

#sum_plan = datPerson['План, ч.'].sum()
#sum_fact = datPerson['Факт, ч.'].sum()
#datPerson = dataframe_ishod.loc[dataframe_ishod['Исполнитель'] == Person[i]]

#Ссылка
#Ответственный
#Сумма 
#СуммаНДС
#Подразделение
#Группа

df_list = [None,None,[],[],[]]

df_list[0] = list(unic_df['Номер'])
df_list[1] = list(unic_df['Заказ покупателя.Ответственный'])



Link = list(unic_df['Номер'])


Table = []
for i in range(len(Link)):
    datLink= Data_frame.loc[Data_frame['Номер'] == Link[i]]
    sum_all = datLink['Сумма заказа'].sum()
    sum_skidka = datLink['Средний % скидки'].sum()
    sum_dont_skidka = datLink['Сумма заказа без скидки'].sum()



    df_list[2].append(sum_all)
    df_list[3].append(sum_skidka)
    df_list[4].append(sum_dont_skidka)


df_dict = {'Номер':df_list[0],'Заказ покупателя.Ответственный':df_list[1],'Сумма заказа':df_list[2],'Средний % скидки':df_list[3],'Сумма заказа без скидки':df_list[4]}

new_dataframe = pd.DataFrame(df_dict)     
with ExcelWriter('C:\\Users\\kushhov\\Desktop\\personal_account\\tables\\origin_table_october.xlsx') as writer:
    new_dataframe.to_excel(writer,index=False)
