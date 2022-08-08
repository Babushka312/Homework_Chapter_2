# 1) Из данного ниже текста извлечь
# a) IP-адрес
# b) Дату и время запроса
# c) HTTP-метод “GET”
# Условие: нужно извлекать вышеуказанную информацию только из GET-запросов.
# POST-запросы игнорируем.

import re
p = re.compile(r'\d+\.\d+\.\d+\.\d+|\d+/Dec/\d+\:\d+\:\d+\:\d+\ \+\d+|GET')
data = ("""
109.169.248.247 - - [12/Dec/2015:18:25:11 +0100] "GET /administrator/ HTTP/1.1" 200 4263 "-" "Mozilla/5.0 (Windows NT 6.0; rv:34.0) Gecko/20100101 Firefox/34.0" "-"
109.169.248.247 - - [12/Dec/2015:18:25:11 +0100] "POST /administrator/index.php HTTP/1.1" 200 4494 "http://almhuette-raith.at/administrator/" "Mozilla/5.0 (Windows NT 6.0; rv:34.0) Gecko/20100101 Firefox/34.0" "-"
46.72.177.4 - - [12/Dec/2015:18:31:08 +0100] "GET /administrator/ HTTP/1.1" 200 4263 "-" "Mozilla/5.0 (Windows NT 6.0; rv:34.0) Gecko/20100101 Firefox/34.0" "-"
46.72.177.4 - - [12/Dec/2015:18:31:08 +0100] "POST /administrator/index.php HTTP/1.1" 200 4494 "http://almhuette-raith.at/administrator/" "Mozilla/5.0 (Windows NT 6.0; rv:34.0) Gecko/20100101 Firefox/34.0" "-"
""")
a = p.findall(data)

for i in a:
    if i == 'GET':
        index = int(a.index('GET'))
        index_date = index - 1
        index_id = index - 2
        print(f'{a[index_id]} {a[index_date]} {a[index]}')
        a.remove('GET')
    else:
        continue