### 1) Что было сделано
В данном коде реализован веб-парсер, который извлекает цитаты с сайта https://quotes.toscrape.com/. Цитаты собираются в виде списка словарей, где каждое значение соответствует тексту цитаты, автору и тегам. Далее собранные данные сохраняются в файл формата JSON, что позволяет удобно хранить и обрабатывать информацию.

### 2) Откуда были получены данные
Данные были получены с веб-сайта https://quotes.toscrape.com/. Этот сайт специально создан для практики веб-парсинга и содержит множество цитат, оформленных с помощью HTML-контейнеров. Сайт предоставляет открытый доступ к контенту, что делает его идеальным источником для непосредственного сбора данных.

### 3) Как осуществлялся сбор
Сбор данных осуществлялся в нескольких этапах:
- Сначала с помощью библиотеки `requests` выполняется HTTP-запрос на указанный URL, и получаем содержимое страницы.
- После успешного ответа (код состояния 200) содержимое страницы передается в библиотеку `BeautifulSoup`, которая парсит HTML.
- Далее с помощью методов `find_all` и `find` из библиотеки `BeautifulSoup` извлекаются все элементы с классом `quote`, содержащие текст цитаты, автора и теги.
- Собранные данные организуются в список словарей, где каждый словарь содержит информацию о конкретной цитате.
- В конце данные записываются в файл `quotes.json` с использованием модуля `json`, который сохраняет список в формате JSON с поддержкой кодировки UTF-8.

### 4) Почему был выбран тот или иной метод/инструмент, а не другой
- **`requests`**: Эта библиотека была выбрана для выполнения HTTP-запросов благодаря своей простоте и удобочитаемости. `requests` позволяет легко отправлять запросы, обрабатывать ответы и работать с различными HTTP-методами.
  
- **`BeautifulSoup`**: Данная библиотека идеально подходит для парсинга HTML-кода, так как она предоставляет множество методов для извлечения данных из тегов. Она проста в использовании и хорошо документирована, что делает её подходящей для веб-скрейпинга.

- **Формат JSON**: Выбор формата JSON для сохранения данных объясняется его популярностью и удобством. JSON легко читается как людьми, так и программами, а также хорошо поддерживается во многих языках программирования, что упрощает дальнейшую обработку и передачу данных.

Таким образом, использование этих инструментов и методов обеспечило эффективное и простое решение для сбора и хранения данных с веб-сайта.