import json
import requests
from bs4 import BeautifulSoup

# URL сайта
url = 'https://quotes.toscrape.com/'
# Получение содержимого страницы
response = requests.get(url)
# Проверка успешности запроса
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'lxml')
    # Поиск всех цитат
    quotes = soup.find_all(class_='quote')
    #создание списка для хранения цитат
    quotes_list = []
    # Перебор и вывод каждой цитаты
    for quote in quotes:
        text = quote.find(class_='text').get_text()
        author = quote.find(class_='author').get_text()
        tags = [tag.get_text() for tag in quote.find_all(class_='tag')]
        # Создание словаря для хранения информации о цитате
        quotes_list.append({
            'text': text,
            'author': author,
            'tags': tags
        })
        # Запись данных в JSON файл
    with open('quotes.json', 'w', encoding='utf-8') as json_file:
        json.dump(quotes_list, json_file, ensure_ascii=False, indent=4)
else:
    print(f"Ошибка при получении страницы: {response.status_code}")