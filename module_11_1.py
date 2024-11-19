from bs4 import BeautifulSoup
import requests
import pandas as pd

# # Получаем страницу через requests.
# url = 'https://e-disclosure.azipi.ru/messages/4249051/'
# response = requests.get(url, verify=False)
#
# print(response.content)
#
# #парсим сайт библиотекой bs4
# soup = BeautifulSoup(response.text, 'html.parser')
#
# title = soup.find('title').text
# b = soup.find('b').text
# print(title)
# print(b)

#попробую прочитать файл csv библиотекой pandas
# Открываем csv, игнорируем плохие строки

data = pd.read_csv('fund_structure(20).csv',  delimiter=';',
	    names=['fund_id', 'fund_name_short', 'structure_date', 'asset_name', 'asset_issuer', 'asset_ISIN', 'asset_type', 'asset_sector', 'asset_value', 'net_asset_value_on_date	asset_amount', 'asset_pct'])
# print(data)
# Вывод 10 верхних строк
# print(data.head(10))

# Выведем элементы с нужным нам значением в одной из колонок
# print(data[data.fund_name_short == '"ОПИФ Будущее 2030"'])
# Получаем нужную колонку
print(data[["structure_date"]])

